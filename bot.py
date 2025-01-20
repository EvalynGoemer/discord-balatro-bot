import re
import praw
from os import environ
from jokers import jokers
from Levenshtein import distance
import time

reddit = praw.Reddit(client_id=os.environ["REDDIT_CLIENT_ID"],
                     client_secret=os.environ["REDDIT_SECRET"],
                     password=os.environ["REDDIT_PASSWORD"],
                     user_agent=os.environ["USER_AGENT"],
                     username=os.environ["REDDIT_USERNAME"])

def parse_jokers_from_comment(comment):
    return re.findall(r'\\\[\\\[([^][]+?)\\\]\\\]', comment)

def build_reply_with_jokers(jokers_from_comment):
    matches_per_joker = {}
    levenshtein_start = time.time()
    for key, value in jokers.items():
        for requested_joker in jokers_from_comment:
            jokerDistance = distance(value["name"].lower(), requested_joker.lower(), score_cutoff=int(os.environ["MAX_DISTANCE"]))
            if jokerDistance <= int(os.environ["MAX_DISTANCE"]):
                if not requested_joker in matches_per_joker:
                    matches_per_joker[requested_joker] = []
                matches_per_joker[requested_joker].append({ "match": value, "distance": jokerDistance })
    levenshtein_end = time.time()
    print(f"Fuzzy string matching for all jokers took: {levenshtein_end - levenshtein_start} seconds")
    reply = ""
    for key, value in matches_per_joker.items():
        value.sort(key=lambda x: x["distance"])
        reply += (
            f"[{value[0]['match']['name']}]({os.environ["FANDOM_LINK"] + value[0]['match']['name'].replace(' ', '_')}) ({value[0]['match']['rarity'] if 'rarity' in value[0]['match'] else 'Common'} Joker)\n"
            f"- **Effect**: {value[0]['match']['text']}\n"
            f"- **To Unlock**: {value[0]['match']['unlock'] if 'unlock' in value[0]['match'] else 'Available by default'}\n\n"
        )
    reply += '^(Data sourced directly from Balatro\'s localization files)'

    return reply

def main():
    for comment in reddit.subreddit(os.environ["SUBREDDITS"]).stream.comments(skip_existing=True):
        print(f"Rate limiting info: {reddit.auth.limits}")
        print(f"Comment received: {comment.body}")
        jokers_from_comment = parse_jokers_from_comment(comment.body)
        print(f"Jokers from comment: {jokers_from_comment}")
        if len(jokers_from_comment) > 0:
            print(build_reply_with_jokers(jokers_from_comment))
            if os.environ["SHOULD_REPLY"] == "true"
                try:
                    comment.reply(build_reply_with_jokers(jokers_from_comment))
                except praw.exceptions.APIException as e:
                    print(e)
                    continue
            else:
                print("The bot is merely spectating subreddit traffic.")
        else:
            print("No jokers, skipping...")

if __name__ == "__main__":
    main()
