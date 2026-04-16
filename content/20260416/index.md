---
Title: Dakbot — AllSport 5000 Data
Date: 2026-04-16
Summary: A compact ESP32-powered device that extracts scoreboard data from Daktronics AllSport 5000 systems, serving JSON feeds with MQTT support and remote updates for live streaming applications.
---

# Dakbot — AllSport 5000 Data

Several years ago, I built my own Daktronics AllSport data parser. I found some code on GitHub to get me started. At the time I was using Wirecast and the program I built generated PNG score bug files. I’ve since moved to vMix and just generated JSON data files. I some point I added some serial ethernet converters, so I didn’t have to connect the computer directly to the AllSport. It’s occasionally finicky, but solid for the most part. At the time we were just starting to stream, and the cost of the AllSport CG might as well be $100k. The Sportzcast Scorebots came along, but $500 a year for xml, and I need three, was too much when I had something that worked.

One of the drawbacks to this solution is that using the serial port on Windows can be a pain. Sometimes serial port lock ups would require a computer reboot, not ideal during the middle of a live stream. I’ve thought about building a dedicated Raspberry PI, but it always seemed to pricey, too convoluted, what I had worked… mostly. 

Recently I came across an ESP32 with a POE network interface. This small cheap board might be the solution to the problem I’d been pushing off. I gave Claude Code my original python code and asked it to convert it for use on the ESP32. In less than 30 minutes, with a little back and forth, it gave me the new code with instructions for getting it set up.

I pulled the trigger and spent $40 on ESP32-S3 Ethernet Development Board and a MAX3232 with a DB9. Thanks to a local Amazon warehouse, within 24 hours of the idea I was extracting data from an AllSport 5000 with a tiny ESP32 board. 

<img class="mx-auto d-block img-thumbnail" style="max-width:600px;" src="{static}/20260416/dakbot.jpg">

After about a week of on and off tweaking I have a neat little device. POE Ethernet on one side and a DB9 Serial port on the other. A simple inline device the size of a snickers bar. With the help of J.J.  Mc Kenna, a Willamette Alum who I met through Office Hours Global, I even have a custom 3D printed case.

<img class="mx-auto d-block img-thumbnail" style="max-width:600px;" src="{static}/20260416/20260416.jpg">

Now what about the details? Well at its core it takes the data from the AllSport and serves up a JSON file. Just enter the IP of the device and you’ve got a JSON data feed. A couple of years ago that would have been enough and I would have stopped. With how fast I’m able to create with Claude, I fleshed out more features. I built a settings page where I can change the sport, the network details, and reboot the device. I added an update process that pulls updates from the GitHub Repository. I implemented MQTT, which lets me access the data from anywhere in the world in real time. My unscientific test showed about 300ms of latency. 

<img class="mx-auto d-block img-thumbnail" style="max-width:600px;" src="{static}/20260416/dakbot-latency.jpg">

Yesterday was the maiden voyage. I installed it at the baseball stadium in the morning. Before the game in the evening someone turned on the AllSport and boom the data was there, sending to vMix on the local network and available on the public internet.

I noticed a small logic bug on the top/bottom inning indicators. I was able to fix the code and then remotely update the device from the settings page. It worked as expected which was mostly great. One of the gotchas working with the AllSport serial data is it only sends updates. When something changes, it sends just that change. So, when you reboot the ESP32, all the data is empty until that field is changed. There are some sequences that push all the data: when the console starts up, when the clock stops, I haven’t figured out what that is for baseball, so we were without a bug for a little bit, but that was expected. 

All in all, this was a successful test. I will probably be building a couple more of these during the summer. They are cheap enough to just have one in every facility.

All the instructions are available on the GitHub Repository including amazon links and the .3mf file for the case. If you have a Daktronics AllSport 5000 and want data, give it a try. A small investment, a little programing, some soldering and your be on your way to adding scoreboard data to your project.

<a target="_blank" class="btn btn-primary" href="https://github.com/chrissabato/dakbot">Dakbot GitHub Repo</a>