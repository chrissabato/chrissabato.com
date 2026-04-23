---
Title: Tennis SRT Scorebug Gateway 
Date: 2026-03-14
Summary: I wanted a way to automate score overlays for our tennis broadcasts without the massive overhead of traditional production software and hardware for every single court.
Tags: featured
---


# Tennis SRT Scorebug Gateway 
I wanted a way to automate score overlays for our tennis broadcasts without the massive overhead of traditional production software and hardware for every single court. So, I tasked Claude Code to build the [Tennis SRT Scorebug Gateway](https://github.com/chrissabato/Tennis-SRT-Scorebug-Gateway).

<a href="{static}/20260314/20260314.jpg"><img src="{static}/20260314/20260314.jpg"></a>

<div class="ratio ratio-16x9">
    <iframe src="https://www.youtube.com/embed/hDnOuzhvTUk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>


## The Stack
- Node.js (Management & UI)
- FFmpeg (NVIDIA Hardware Encoding)
- Vultr (Ubuntu + NVIDIA GPUs) - A simple and affordable alternative to AWS
- SRT (Secure Reliable Transport)

## The Workflow:
- SRT Input (Direct from Court Cam) -> Real-time JPEG Overlay Injection (from live results software) -> - NVENC Hardware Encode -> SRT Output to FloSports.

## The Results:
- Handles 6 courts simultaneously
- Dedicated monitoring & config UI
- Automated deployment scripts
- Stable, scalable, and ultra-low latency (500ms buffer)

It’s awesome seeing how AI-assisted coding can help build robust, high-performance infrastructure that solves real-world broadcast challenges!

<a href="{static}/20260314/Tennis Court Scorebug Sample.jpg"><img src="{static}/20260314/Tennis Court Scorebug Sample.jpg"></a>