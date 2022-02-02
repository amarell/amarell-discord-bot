from re import sub
import asyncpraw
import random

reddit = asyncpraw.Reddit(
    client_id="zRz7g1nCkdYbL8954UCong",
    client_secret="gqbxdWjbVqfnzmz0Ovyc0vGiaoJ8gA",
    user_agent="discord:com.amarellBot:v1.0.0 (by /u/Snoopy34)",
)

print(reddit.read_only)
async def getsubreddit():
    subreddit = await reddit.subreddit("redditdev", fetch=True)
    print(subreddit.display_name)



# Output: redditdev




