#coding: utf-8

from db_api import api, db
from parse_text import parse_text
from dict_vector import DictVector


class KeywordCounter:
    def __init__(self, text):
        self.keyword = {};
        parsed_data = parse_text(text.encode("utf-8"));
        for data in parsed_data:
            if (data["POS"] == u"名詞"):
                key = data["Surface"].replace(".", "_");
                if (self.keyword.has_key(key)):
                    self.keyword[key] += 1;
                else:
                    self.keyword[key] = 1;
        self.keyword = DictVector(self.keyword);
        self.keyword.nomalize();


def crawl(username):
    since_id = db.tweets.find({"username": username}).sort("_id", -1).limit(1)[0]["_id"];
    tweets = api.user_timeline(screen_name=username, since_id=since_id);
    records = [{"created_at": tweet.created_at, "_id": tweet.id, "text": tweet.text, "username": username, "keywords": KeywordCounter(tweet.text).keyword} for tweet in tweets];

    recommentds = [];
    for tweet in tweets:
        keywords = KeywordCounter(tweet.text).keyword;
        old_tweets = db.tweets.find({"username":username});
        for old_tweet in old_tweets:
            r = keywords * DictVector(old_tweet["keywords"]);
            if r != 0.0:
                data = (old_tweet["text"], r);
                recommentds.append(data);
        recommentds.sort(lambda x, y: int((y[1] - x[1]) * 100000));
        try:
            if (recommentds[0][1] > 0.3 and recommentds[1][1] > 0.3):
                db.recommends.insert({
                    "username": username,
                    "text1": tweet.text,
                    "text2": recommentds[0][0],
                    "text3": recommentds[1][0],
                    "time": tweet.created_at.strftime("%Y-%m-%d"),
                });
        except IndexError:
            pass;

    if records:
        db.tweets.insert(records);

if __name__ == "__main__":
    crawl("higumachan725");
