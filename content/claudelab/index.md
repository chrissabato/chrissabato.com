---
Title: After Hours Lab: Claud Code Website
Date: 2026-03-01
Updated: Feb 28, 2026
Summary: A beginner-friendly lab that teaches you to create, commit, and publish a simple website using Claude Code, GitHub, and GitHub Pages.
Status: hidden
---


# After Hours Lab: Claude Code Website

***Sunday, March 1 at 10 a.m. PT | [After Hours Breakout Room](https://zoom.us/meeting/register/tJIocuqsqT8pHNHE6mRQ5gMvhUAwnAd5-I2s?_x_zm_rtaid=UC5YApTMTcufbtmwcLtZnQ.1770943518775.8493840c9663bb1123334fd5c34530e1&_x_zm_rhtaid=8#/)*** 

This introductory lab will explore creating a website with Claude Code. We'll use Claude to build a simple website using html and javascript, commit it to GitHub, and publish it to the web using GitHub Pages. While the website itself may be basic, you'll become familiar with the process so you can apply it to your own projects.

## Prerequisites

Complete these steps before the lab. If you have issue pop into After Hours and ask for help 

**Create Accounts**

* [**Claude Pro Account**](https://claude.ai/) — The $20/month plan is sufficient to get started. You can cancel after one month if you'd like.
* [**GitHub Account**](https://github.com) — Create an account in advance to save time during the lab. No prior knowledge needed.

**Installations**

* [**Homebrew**](https://brew.sh/) — **[mac only]** Makes installing command-line tools on macOS easier
    * Terminal: ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```
* [**Git**](https://git-scm.com/install/windows) — Version control for communicating with GitHub
    * **Windows** 
        * Command Prompt: ```winget install --id Git.Git -e --source winget```
    * **macOS**
        * Terminal (Homebrew): ```brew install git```
* [**Claude Code**](https://code.claude.com/docs/en/quickstart) — Install Claude Code via one of the methods below
    * **macOS**
        * Terminal: ```curl -fsSL https://claude.ai/install.sh | bash```
    * **Windows**:
        * Command Prompt: ```curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd```
        * Update PATH: For some reason the installer doesn't update the PATH correctly.
            * Run in Command Prompt: ```setx PATH "%PATH%;%USERPROFILE%\.local\bin"```
            * Restart Command Prompt to load PATH
* [**GitHub CLI**](https://github.com) — This will make authenticating with GitHub easier
    * **macOS**
        * Terminal (Homebrew): ```brew install gh```
    * **Windows**
        * Command Prompt: ```winget install --id GitHub.cli```

**Optional** 

* [**Install VS Code**](https://code.visualstudio.com/) — This is optional, but you may find it helpful. If we have time will talk a little more about it.


## Claude Code Prompt

Here’s the starting prompt. This will be used during the lab, you don'y need to do anything with it adhead of time. It’s a bit vague on purpose so we can tweak whatever results we get.

```Develop a production logging tool as a single-file web application (HTML/JS) suitable for GitHub Pages. Include a 'Start' button to begin the session and a 'Log' button that allows the user to input a note. Upon clicking 'Stop,' the app should automatically generate and download a CSV file containing all notes with their respective timestamps.```
