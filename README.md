# YouTube Sentiment Analysis  

## Overview  
YouTube Sentiment Analysis is a web application that allows users to input a YouTube video link and retrieve comments along with their sentiment analysis. The application employs a machine learning model to determine whether the comments are positive or negative, providing insights into the general opinion of the viewers.  

## Features  
- **Input Video Link**: Users can enter any valid YouTube video link.  
- **Sentiment Analysis**: The application analyzes comments' sentiment using AI and provides a detailed summary.  
- **Styled Comments Table**: Comments are displayed in a table, color-coded based on their sentiment.  
- **User-Friendly Interface**: Built with Streamlit, providing an intuitive web interface.  

## Technologies Used  
- **Python**: The primary programming language for the application.
- **Streamlit**: For creating interactive web applications.  
- **YouTube API**: To fetch comments from the specified YouTube videos.  
- **Jupyter Notebook**: Used for analyzing the problem and training the model, providing an interactive environment for experimentation and visualization of data insights.
- **TensorFlow and Keras**: For developing and training the machine learning model to predict the sentiment of the comments.

## Deploying
- Youtube Sentiment Analysis deployed website: [Youtube Sentiment Analysis](https://alaindelong-youtube-sentiment-analysis.hf.space/)
- Published Model: https://huggingface.co/spaces/AlainDeLong/youtube-sentiment-analysis/tree/main
- Due to the large size of the model, it cannot be included here; it will be available at the huggingface link mentioned above.

## Note
Due to the limited quota of the YouTube API, the website only displays comments from the video itself, and replies to comments (also known as responses) will not be shown. As a result, the number of comments displayed on the website will often be less than the actual number of comments on the YouTube video.

## Installation  
To set up the project locally, follow these steps:  

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/AlainDeLong2k/demo-youtube-sentiment-analysis.git
   cd demo-youtube-sentiment-analysis

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

## Usage
1. Open a web browser and navigate to http://localhost:8501 (this is the default Streamlit port).
2. Enter a valid YouTube video link in the input field. Examples of valid links include:
   - https://www.youtube.com/watch?v=b5k8bkWYyPQ
   - https://youtu.be/b5k8bkWYyPQ?si=gABWBqKdjo_um6nk
3. Click on the `Analyze` button to retrieve and analyze comments for sentiment.
4. View the summary and comments in the application.

## Contributing
Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---
For any further questions or issues, feel free to open an issue in the repository.
