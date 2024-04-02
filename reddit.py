import streamlit as st
from textblob import TextBlob
import praw
import pandas as pd
import matplotlib.pyplot as plt

pip install textblob==0.15.3

# Reddit API credentials
client_id = 'eYFGVlKjL-cBrrg6VZOmqQ'
client_secret = 'TnP_BYPDsdzUbm1w5oYlcipzQMHQ6w'
user_agent = 'sentiments/1.0 by YourUsername'

# Authenticate with Reddit API
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

# Function to perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Streamlit app
st.title('Live Sentiment Analysis of Reddit Posts about Chatgpt')

# Get posts based on subreddit
subreddit_name ="Chatgpt"
if True:
    st.write(f'Recent posts in subreddit: {subreddit_name}')
    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.hot(limit=25)

    post_data = {'Title': [], 'Sentiment': [], 'Created At': []}
    i=1
    for post in posts:
        i=i+1
        post_data['Title'].append(post.title)
        post_data['Sentiment'].append(analyze_sentiment(post.title))
        post_data['Created At'].append(post.created_utc)
        if i>=5:
            break

    df = pd.DataFrame(post_data)

    st.write('Latest Chatgpt Posts:')
    for i, row in df.iterrows():
        st.write(f'Title: {row["Title"]}')
        st.write(f'Sentiment: {row["Sentiment"]}')

    # Plot time series sentiment
    st.write('Sentiment Over Time:')
    df['Created At'] = pd.to_datetime(df['Created At'], unit='s')
    df['Sentiment'].value_counts().plot(kind='bar')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    st.pyplot(plt)
