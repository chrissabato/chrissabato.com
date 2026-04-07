---
Title: AI Broadcast Tools
Date: 2026-04-07
Summary: A running list of open-source and proprietary broadcast tools I've built for live sports production.
Tags: broadcast, sports, tools, open-source
---

# AI Broadcast Tools
A running list of broadcast tools I've built for live sports production. Some are fully open-source on GitHub; others are a bit more proprietary.


<hr>

### Tennis SRT Scorebug Gateway
Manages simultaneous SRT video restreams for tennis tournaments with up to 6 court cameras. Receives SRT feeds on ports 5001–5006, fetches live scorebug images every second, overlays them onto video using FFmpeg with NVIDIA NVENC hardware encoding, and outputs to ports 6001–6006. Includes a web interface with per-court status, expandable FFmpeg logs, and optional Google Chat webhook notifications.

<a href="https://github.com/chrissabato/Tennis-SRT-Scorebug-Gateway" target="_blank">GitHub</a>

<img style="max-width:400px;" src="{static}/20260314/20260314.jpg"> <img style="max-width:400px;" src="{static}/20260314/Tennis Court Scorebug Sample.jpg">


<hr>

### AIDA SRT Controller
A PHP dashboard for managing SRT video streams from multiple AIDA cameras. Enable or disable streaming per-camera or in bulk, with real-time status polling every 5 seconds. Each camera is configured with its display name, IP, auth key, SRT destination, port, and latency.

<a href="https://github.com/chrissabato/aida-srt" target="_blank">GitHub</a>

<img style="max-width:400px;" src="{static}/ai-built-tools/aida-srt.jpg">


<hr>

### Audio Meter
A browser-based LUFS audio level meter for real-time microphone monitoring. Implements ITU-R BS.1770-4 K-weighting for accurate loudness measurement, with a rolling 3-second integrated loudness window and a 30-second scrolling history graph. Color-coded display (green/orange/red) gives instant visual feedback against a -24 LUFS broadcast reference. Supports device selection and bookmarkable `?input=` URL parameters for pre-selecting audio inputs.

<a href="https://chrissabato.github.io/audiometer/" target="_blank">Public Website</a> | <a href="https://github.com/chrissabato/audiometer" target="_blank">GitHub</a>

<img style="max-width:400px;" src="{static}/ai-built-tools/audio-meters.jpg">


<hr>

### Broadcast Stats Parser
Parses live stats XMLs and generates various data feeds for broadcast graphics systems.

<img style="max-width:400px;" src="{static}/ai-built-tools/broadcast-stats.jpg">


<hr>

### LiveCut
A browser-based HLS highlight clipper — no server uploads or software installation required. Load an `.m3u8` URL, mark in/out points with keyboard shortcuts (I/O keys), queue multiple clips, and export directly to your machine using FFmpeg.wasm. Supports frame-accurate adjustment, live stream edge jumping, and stream-copy export for fast lossless results.

<a href="https://livecut.chrissabato.com/" target="_blank">Public Website</a> | <a href="https://github.com/chrissabato/livecut" target="_blank">GitHub</a>


<hr>

### NCAA Stats XML Fixer
Upload NCAA game XML files, correct the team codes to match official NCAA values, and download the fixed files. Useful for getting broadcast graphics systems working with stats feeds that have mismatched or missing team codes.

<a href="https://rpi.chrissabato.com/" target="_blank">Public Website</a> | <a href="https://github.com/chrissabato/ncaa-rpi-xml" target="_blank">GitHub</a>


<hr>

### College Athletics Website Directory
A searchable directory of 1,300+ college athletics websites spanning NCAA Division I, II, III, and NAIA. Filter by state, division, or conference. Also available as a Chrome extension for quick access from anywhere in the browser.

<a href="https://directory.chrissabato.com" target="_blank">Public Website</a> | <a href="https://github.com/chrissabato/college-athletics-directory" target="_blank">GitHub</a>


<hr>

### Bolin PTZ Preset Controller
A web-based controller for the Bolin EXU-230NX PTZ camera. Supports pan/tilt/zoom/focus with hold-to-move controls, 16 customizable presets with thumbnail snapshots, drag-and-drop preset reordering, SRT stream toggling, and a preset-only view mode for operators.

<a href="https://github.com/chrissabato/bolin-control" target="_blank">GitHub</a>

<img style="max-width:400px;" src="{static}/ai-built-tools/bolin-ptz.jpg">


<hr>

### NDI Audio Interface Converter
An Electron-based GUI application for routing audio between a Behringer XR18 mixer and Dante Virtual Soundcard over NDI — enabling full-duplex comms over a standard network.

<a href="https://github.com/chrissabato/ndi-comms-router" target="_blank">GitHub</a>

<img style="max-width:400px;" src="{static}/ai-built-tools/ndi-audio.jpg">


<hr>

### Photo ID
A web app for crowdsourcing photo identification. Upload a gallery, share a token-based link with identifiers, and let them tag names to photos one-by-one with keyboard navigation. Exports to CSV and can write XMP metadata directly to image files via an included Windows utility.

<a href="https://github.com/chrissabato/photo-id" target="_blank">GitHub</a>

<img style="max-width:400px;" src="{static}/ai-built-tools/photo-id.jpg">

<hr>

### Dakbot
MicroPython firmware for an ESP32-S3-ETH board that reads live scoreboard data from a Daktronics AllSport 5000 controller and serves it as JSON over Ethernet. Monitors RTD serial packets at 19200 baud and supports baseball, basketball, volleyball, football, and hockey/lacrosse. Requires a MAX3232 level shifter for RS-232 conversion.

<a href="https://github.com/chrissabato/dakbot" target="_blank">GitHub</a>
