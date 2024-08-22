# Import necessary libraries and modules
import streamlit as st
import pandas as pd
from youtube import get_video_comments
from predict import predict_sentiments

# Set the page title and layout for the Streamlit app
st.set_page_config(
    page_title="Youtube Sentiment Analysis",  # Title of the app displayed on the browser tab
    layout="centered"  # Layout configuration to center the content
)


# Function to fetch video comments and analyze their sentiment
def get_video(video_id):
    # Check if a video ID has been provided; if not, return an error message
    if not video_id:
        return {"error": "video_id is required"}

    comments = get_video_comments(video_id)  # Fetch comments from the specified YouTube video
    predictions = predict_sentiments(comments)  # Analyze sentiment of the fetched comments

    positive = predictions.count("Positive")  # Count the number of positive sentiments
    negative = predictions.count("Negative")  # Count the number of negative sentiments

    # Create a summary dictionary of the sentiment analysis
    summary = {
        "num_comments": len(comments),  # Total number of comments retrieved
        "positive": positive,  # Total number of positive comments detected
        "negative": negative,  # Total number of negative comments detected
        "rating": (positive / len(comments)) * 100 if len(comments) > 0 else 0
        # Calculate the percentage rating of positive sentiments
    }
    # Return the predictions, original comments, and summary
    return {"predictions": predictions, "comments": comments, "summary": summary}


# Function to style DataFrame rows based on sentiment (color coding)
def highlight_sentiment(row):
    # Highlighting rows based on sentiment type using specific colors
    if row['Sentiment'] == 'Positive':
        return ['background-color: #d1e7dd; color: #0f5132;'] * len(row)  # Light green for positive sentiment
    elif row['Sentiment'] == 'Negative':
        return ['background-color: #f5c6cb; color: #842b2e;'] * len(row)  # Light red for negative sentiment


# Title of the Streamlit application
st.title("YOUTUBE SENTIMENT ANALYSIS")  # Set the main title of the application

# Create a form to input a YouTube video URL
video_url = st.text_input("**Enter A YouTube Video Link**")  # Text input field for the video URL

# Provide examples of valid YouTube links for user reference
st.markdown("**Examples of Valid YouTube Links:**")
st.markdown("- https://www.youtube.com/watch?v=b5k8bkWYyPQ")
st.markdown("- https://www.youtube.com/watch?v=b5k8bkWYyPQ&t=30s")
st.markdown("- https://youtu.be/b5k8bkWYyPQ?si=gABWBqKdjo_um6nk")

# Analyze the video when the button is clicked
if st.button("Analyze"):
    if video_url:  # Check if the user has entered a video URL
        try:
            video_id = None  # Initialize video_id variable
            # Extract video ID from different possible URL formats
            if "youtube.com/watch?v=" in video_url:
                video_id = video_url.split("v=")[1].split("&")[0]  # Extract video ID from full YouTube link
            elif "youtu.be" in video_url:
                video_id = video_url.split('/')[-1].split('?')[0]  # Extract video ID from shortened YouTube link
            else:
                raise ValueError("Invalid YouTube link format!!!")  # Raise ValueError if the link format is invalid

            data = get_video(video_id)  # Fetch video comments and analyze sentiment
            # Check if we received valid data or an error
            if "error" in data:
                st.warning("Please enter a valid YouTube link!!!")  # Display a warning if the video link is invalid
            else:
                summary = data['summary']  # Retrieve the summary of sentiment analysis
                comments = list(
                    zip(data['comments'], data['predictions']))  # Pair comments with their sentiment predictions

                # Display the summary of the sentiment analysis
                st.header("Summary")
                st.markdown(f"**Number of Comments:** {summary['num_comments']}")
                st.markdown(f"**Positive:** {summary['positive']}")
                st.markdown(f"**Negative:** {summary['negative']}")
                st.markdown(f"**Rating:** {summary['rating']:.2f}%")

                # Display comments along with their sentiment in a DataFrame
                st.subheader("Comments")
                comments_df = pd.DataFrame(comments, columns=['Comment', 'Sentiment'])

                # Apply color coding for sentiment and display styled DataFrame
                styled_comments_df = comments_df.style.apply(highlight_sentiment, axis=1)
                # Render the styled DataFrame in the app
                st.dataframe(styled_comments_df, width=700, use_container_width=True)

        except ValueError as ve:
            st.error(str(ve))  # Display warning for invalid YouTube link format
        except (Exception,) as e:
            # General error message for any exceptions
            st.warning("An error occurred while processing your request. Please try again later!!!")
    else:
        st.warning("Please enter a valid YouTube link!!!")  # Prompt user to enter a link if the input is empty
