# TwitchHUD
Twitch HUD for Elite Dangerous Market Connector Overlay

I was trying to build a plugin that retrieved chat messages from Twitch bot and displayed them in the Elite Dangerous Market Connector Overlay.

I have now realized that it has to be 2 different things running so right now I am working on making the chatbot write to a chatlog.txt and then I will build the overlay plugin to read from that chat log at a set intreval.

The plugin has to run from the load.py My test bot is Run.py

To install copy the files into AppData\Local\EDMarketConnector\plugins\TwitchHUD\


The refrences I have been looking at are:
https://github.com/Marginal/EDMarketConnector/blob/master/PLUGINS.md
https://github.com/inorton/EDMCHits
