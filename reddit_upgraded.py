import streamlit as st
from textblob import TextBlob
import praw
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

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

# Function to retrieve posts and update sentiment data
def refresh_data():
    post_data = {'Title': [], 'Sentiment': [], 'Created At': []}
    subreddit_name = "Chatgpt"
    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.new(limit=100)  # Fetching latest 100 posts
    
    for post in posts:
        created_at = datetime.utcfromtimestamp(post.created_utc).date()
        if created_at >= datetime(2024, 4, 4).date():  # Retrieve posts from April 4th onwards
            post_data['Title'].append(post.title)
            post_data['Sentiment'].append(analyze_sentiment(post.title))
            post_data['Created At'].append(created_at)

    return pd.DataFrame(post_data)

# Initial data retrieval
df = refresh_data()

# Displaying latest posts and sentiments
st.write('Latest Chatgpt Posts:')
for i, row in df.head(5).iterrows():  # Displaying only 5 latest posts
    st.write(f'Title: {row["Title"]}')
    st.write(f'Sentiment: {row["Sentiment"]}')

# Time series analysis and plotting
time_series_df = df.groupby('Created At')['Sentiment'].value_counts().unstack().fillna(0)
time_series_df.plot(kind='line', figsize=(10, 6))
plt.title('Sentiment Time Series')
plt.xlabel('Date')
plt.ylabel('Number of Posts')
plt.xticks(rotation=45)
plt.legend(title='Sentiment')
st.pyplot()

