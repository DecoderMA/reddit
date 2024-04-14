import streamlit as st
from textblob import TextBlob
import praw
import pandas as pd
import plotly.express as px

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
    st.sidebar.write(f'Recent posts in subreddit: {subreddit_name}')
    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.new(limit=None)

    post_data = {'Title': [], 'Sentiment': [], 'Created At': []}
    for post in posts:
        # Check if the post is after April 1st
        if post.created_utc >= 1617235200:  # April 1st, 2022 in UTC timestamp
            post_data['Title'].append(post.title)
            post_data['Sentiment'].append(analyze_sentiment(post.title))
            post_data['Created At'].append(pd.to_datetime(post.created_utc, unit='s'))

    df = pd.DataFrame(post_data)
    
    st.sidebar.write('## Latest Posts About Chatgpt:')
    for i, row in df.head(5).iterrows():
        st.sidebar.write(f'Title: {row["Title"]}')
        st.sidebar.write(f'Sentiment: {row["Sentiment"]}')
        
    # Plot time series graph using Plotly
    st.write('## Sentiment Over Time:')
    sentiment_counts = df.groupby([df['Created At'].dt.date, 'Sentiment']).size().unstack(fill_value=0)
    fig = px.line(sentiment_counts, x=sentiment_counts.index, y=sentiment_counts.columns,
                  title='Sentiment Distribution Over Time',
                  labels={'value': 'Count', 'index': 'Date', 'variable': 'Sentiment'})
    fig.update_layout(hovermode="x unified")  # Display hover info for all points on the x-axis
    st.plotly_chart(fig, use_container_width=True)
