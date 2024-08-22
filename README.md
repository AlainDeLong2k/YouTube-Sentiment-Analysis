# YouTube Sentiment Analysis  

## Overview  
YouTube Sentiment Analysis is a web application that allows users to input a YouTube video link and retrieve comments along with their sentiment analysis. The application employs a machine learning model to determine whether the comments are positive, negative, or neutral, providing insights into the general opinion of the viewers.  

## Features  
- **Input Video Link**: Users can enter any valid YouTube video link.  
- **Sentiment Analysis**: The application analyzes comments' sentiment using AI and provides a detailed summary.  
- **Styled Comments Table**: Comments are displayed in a table, color-coded based on their sentiment.  
- **User-Friendly Interface**: Built with Streamlit, providing an intuitive web interface.  

## Technologies Used  
- **Python**: The primary programming language for the application.  
- **Streamlit**: For creating interactive web applications.  
- **Pandas**: For data manipulation and analysis.  
- **Machine Learning Model**: For predicting the sentiment of the comments.  
- **YouTube API**: To fetch comments from the specified YouTube videos.  

## Installation  
To set up the project locally, follow these steps:  

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/yourusername/youtube-sentiment-analysis.git  
   cd youtube-sentiment-analysis

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv  
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   
4. **Run the application**:
   ```bash
   streamlit run app.py 


