# Amarell Discord Bot

Amarell is a Discord bot built using the discord.py framework. I started this project for fun and just wanted to learn more about Python and how to integrate various APIs into my application. 

The bot is currently deployed and running on Heroku, and you can invite it using the following [link]([Discord](https://discord.com/api/oauth2/authorize?client_id=797609174644424714&permissions=8&scope=bot)). 

# Main features/commands

First of all, the prefix for all commands is `-`. 

Some of commands that the bot supports are the following:

- `-help` - displays a list of commands and what they are used for.

- `-check_spotify_activity @some_user` - will check wether the tagged user is listening to spotify and if they are, it will show what they are listening to and type out the lyrics of that song in the chat.

- `-hs` - starts a new game of hangman.

- `-define {length}` - defines the provided word using definitions by Merriam Webster's dictionary.

- `-generate_password {length}` - generates a sequence of random ASCII characters with the provided length

- `-meme` - responds with a random "hot" meme from the subreddit r/memes

- `-wallpaper` - responds with a random wallpaper from the r/wallpapers subreddit's "hot" section

- `-art` - responds with a random artwork from the r/art subreddit

- a lot few more commands that work with the Reddit's API, commands for memes from different subreddits

- `-lookup {some_term}` - find the Wikipedia article that matches the given term and type out first couple of sentences in the chat. For example `-lookup Obama` will find the article about Obama type some information about him in the chat where the command was called from.

- etc.

# APIs used:

- [PRAW]([GitHub - praw-dev/praw: PRAW, an acronym for &quot;Python Reddit API Wrapper&quot;, is a python package that allows for simple access to Reddit&#39;s API.](https://github.com/praw-dev/praw)) - Python Reddit API Wrapper

- [Wikipedia ]([GitHub - goldsmith/Wikipedia: A Pythonic wrapper for the Wikipedia API](https://github.com/goldsmith/Wikipedia))- Wikipedia API Wrapper

- MERRIAM-WEBSTER'S COLLEGIATE DICTIONARY


