"""Let Pelican read posts saved by the web CMS (Sveltia CMS at /admin/).

Posts on this site use a `---` fenced block of `Key: value` lines, which
Pelican's Markdown reader handles natively. The CMS writes that same block as
real YAML, so it sometimes:

  * wraps a value in quotes  (Summary: "Note: this has a colon")
  * uses a block scalar       (Summary: >-  followed by indented lines)
  * writes a list             (Tags: [a, b]  or  "- a" lines)

Pelican would keep the quotes literally and mangle the other two. This plugin
normalises the front matter back into plain one-line `Key: value` form before
the normal Markdown reader runs. Files whose front matter is already plain are
passed through byte-for-byte, so hand-written posts are unaffected.
"""

import re

import yaml
from markdown import Markdown
from pelican import signals
from pelican.readers import MarkdownReader
from pelican.utils import pelican_open

FRONT_MATTER = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(\r?\n|\Z)", re.S)
KEY_LINE = re.compile(r"^([A-Za-z0-9_-]+):[ \t]*(.*?)[ \t]*$")
NEEDS_YAML = ('"', "'", "[", "{", "|", ">")


def _to_text(value):
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return ", ".join(_to_text(v) for v in value)
    if hasattr(value, "isoformat"):
        return value.isoformat(sep=" ") if hasattr(value, "hour") else value.isoformat()
    if isinstance(value, bool):
        return "true" if value else "false"
    return " ".join(str(value).split())  # collapse newlines from folded text


def normalise(text):
    match = FRONT_MATTER.match(text)
    if not match:
        return text
    block = match.group(1)
    if not any(
        (m and m.group(2).startswith(NEEDS_YAML)) or line.lstrip().startswith("- ")
        for line in block.splitlines()
        for m in [KEY_LINE.match(line)]
    ):
        return text  # already plain Key: value lines: leave the file untouched
    try:
        data = yaml.safe_load(block)
    except yaml.YAMLError:
        return text  # not valid YAML: leave it for Pelican as before
    if not isinstance(data, dict):
        return text

    raw = {}
    for line in block.splitlines():
        m = KEY_LINE.match(line)
        if m:
            raw.setdefault(m.group(1), m.group(2))

    lines = []
    for key, value in data.items():
        original = raw.get(str(key), "")
        if original and not original.startswith(NEEDS_YAML):
            lines.append(f"{key}: {original}")  # plain value: keep verbatim
        else:
            text_value = _to_text(value)
            if text_value:  # drop empty fields rather than emit "Key: "
                lines.append(f"{key}: {text_value}")
    return "---\n" + "\n".join(lines) + "\n---\n" + text[match.end():]


class CMSMarkdownReader(MarkdownReader):
    def read(self, source_path):
        self._source_path = source_path
        self._md = Markdown(**self.settings["MARKDOWN"])
        with pelican_open(source_path) as text:
            content = self._md.convert(normalise(text))
        metadata = self._parse_metadata(self._md.Meta) if hasattr(self._md, "Meta") else {}
        return content, metadata


def add_reader(readers):
    for ext in CMSMarkdownReader.file_extensions:
        readers.reader_classes[ext] = CMSMarkdownReader


def register():
    signals.readers_init.connect(add_reader)
