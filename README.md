Here is a README file for the provided code:

---

# Live Sentiment Analysis of Reddit Posts about ChatGPT

This Streamlit application performs live sentiment analysis of Reddit posts related to ChatGPT and visualizes the sentiment trends over time.

## Features

- **Live Data Fetching**: Retrieves recent posts from the specified Reddit subreddit.
- **Sentiment Analysis**: Uses the TextBlob library to analyze the sentiment of the post titles (positive, neutral, or negative).
- **Time Series Visualization**: Visualizes the sentiment distribution over time using Plotly.

## Prerequisites

- Python 3.x
- Required Python packages (install them using the command: `pip install -r requirements.txt`):
  - streamlit
  - textblob
  - praw
  - pandas
  - plotly

## Reddit API Credentials

To use the Reddit API, you need to have a Reddit account and create a Reddit application to obtain the necessary credentials:

1. Go to [Reddit's App Settings](https://www.reddit.com/prefs/apps) and create a new application.
2. Choose "script" for the app type and provide the necessary details.
3. Note down your **Client ID**, **Client Secret**, and **User Agent**.

## How to Run the Application

1. Clone the repository or download the code.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Update the code with your Reddit API credentials:
    ```python
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    user_agent = 'your_user_agent'
    ```
4. Run the Streamlit application using the following command:
    ```bash
    streamlit run app.py
    ```
5. The application will start, and you can access it in your browser at `http://localhost:8501`.

## Usage

- Once the application starts, you will see the title and latest posts from the specified subreddit (default: ChatGPT).
- The application displays the sentiment (positive, neutral, negative) of the recent posts in the sidebar.
- The time series graph shows the distribution of sentiments over time.

## Notes

- You can customize the subreddit by changing the `subreddit_name` variable in the code.
- Adjust the date filter in the code according to your preference.

## License

This code is open source and available under the [MIT License](LICENSE).

---
