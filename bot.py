import praw
import os
from modules.utils import build_reply_with_items, parse_items_from_comment

reddit = praw.Reddit(client_id=os.environ["REDDIT_CLIENT_ID"],
                     client_secret=os.environ["REDDIT_SECRET"],
                     password=os.environ["REDDIT_PASSWORD"],
                     user_agent=os.environ["USER_AGENT"],
                     username=os.environ["REDDIT_USERNAME"])

def main():
    for comment in reddit.subreddit(os.environ["SUBREDDITS"]).stream.comments(skip_existing=True):
        print(f"Rate limiting info: {reddit.auth.limits}")
        print(f"Comment received: {comment.body}")
        items_from_comment = parse_items_from_comment(comment.body)
        print(f"items from comment: {items_from_comment}")
        if len(items_from_comment) > 0:
            if os.environ["SHOULD_REPLY"] == "true":
                try:
                    reply = build_reply_with_items(items_from_comment)
                    if (len(reply) > 0):
                        comment.reply(reply)
                except praw.exceptions.APIException as e:
                    print(e)
                    continue
            else:
                print("The bot is merely spectating subreddit traffic.")
        else:
            print("No items, skipping...")

if __name__ == "__main__":
    main()
