import pandas as pd
import twint
import matplotlib.pyplot as plt
import re
from wordcloud import WordCloud


def scrape_tweets(username):
    c = twint.Config()
    c.Username = username
    c.Store_csv = True
    c.Output = "tweets"
    c.Limit = 50
    twint.run.Search(c)


def remove_content(text):
    text = re.sub(r"@\S+", "", text)  # remove mentions
    text = re.sub(r"#\S+", "", text)  # remove hashtags
    text = re.sub(r"https\S+", "", text)  # remove links
    text = re.sub(r"http\S+", "", text)
    return text


scrape_tweets("CDU")

df = pd.read_csv(r".\tweets\tweets.csv")
df.drop_duplicates(inplace=True)
df_tweets = df["tweet"].apply(lambda x: remove_content(x))
df_wc = "".join(df_tweets)

wc = WordCloud().generate(df_wc)

plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
