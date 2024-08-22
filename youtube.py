# Import necessary libraries and modules
import os
import googleapiclient.discovery
import googleapiclient.errors
import streamlit as st

api_key = st.secrets['API_KEY']  # Retrieve the YouTube API key from Streamlit's secrets


def get_comments(youtube, **kwargs):
    """
    Fetch comments from a YouTube video using the YouTube API.
    Parameters:
        youtube (Resource): A resource object for interacting with the YouTube API.
        **kwargs: Additional parameters for the API request.
    Returns:
        list: A list of comments from the video.
    """
    comments = []  # Initialize an empty list to store comments
    results = youtube.commentThreads().list(**kwargs).execute()  # Make API call to get comment threads

    while results:  # Loop until there are no more results to fetch
        for item in results['items']:  # Iterate over each item in the results
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']  # Extract the comment text
            comments.append(comment)  # Add the comment to the list

        # Check if there are more comments by looking for a next page token
        if 'nextPageToken' in results:
            kwargs['pageToken'] = results['nextPageToken']  # Update the kwargs with the next page token
            results = youtube.commentThreads().list(**kwargs).execute()  # Fetch the next page of comments
        else:
            break  # Exit the loop if there are no more pages
    # Return the list of comments
    return comments


def main(video_id, api_key):
    """
    Main function to retrieve comments from a specific YouTube video.
    Parameters:
        video_id (str): The ID of the YouTube video.
        api_key (str): The API key for accessing YouTube API.
    Returns:
        list: A list of comments from the specified video.
    """
    # Disable OAuthlib's HTTPs verification when running locally (only for testing)
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # Build the YouTube resource object with the provided API key
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=api_key)

    # Call the get_comments function to fetch comments for the given video ID
    comments = get_comments(youtube, part="snippet", videoId=video_id, textFormat="plainText")
    return comments


def get_video_comments(video_id):
    """
    Wrapper function to get comments for a video using the main function.
    Parameters:
        video_id (str): The ID of the YouTube video.
    Returns:
        list: A list of comments from the specified video.
    """
    # Call the main function with the video ID and API key.
    return main(video_id, api_key)
