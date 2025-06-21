# discord-balatro-bot
A Discord bot that monitors a discord server and replies with Balatro info to discord messagesthat contain a Balatro Joker/Tarot Card/Spectral Card/Planet Card/etc. in double square brackets. Forked from https://github.com/AlecM33/balatro-joker-bot

The bot uses [discord.py](https://pypi.org/project/discord.py/) observe and reply to messages. It uses fuzzy string matching via Levenshtein distance to get the closest Joker/Tarot/etc. and remove the need for exact spelling.

@AlecM33 on github sourced the information from Balatro's files and version controlled it here to avoid any web scraping. The bot still provides a link to https://balatrowiki.org/ for a given item, so users can see an image and an expanded description.

When ran you need to set the following ENV vars
- MAX_DISTANCE=2
- WIKI_LINK=https://balatrogame.fandom.com/wiki/ 
- TOKEN=YOUR DISCORD BOT TOKEN

The bot also needs the message content intent enabled.

To add a pre hosted version of the bot use [this](https://discord.com/oauth2/authorize?client_id=1385792138696065066&permissions=83968&integration_type=0&scope=bot) invite link.
