Spotify Music Recommendations:
This Python program utilizes the Spotify API to find similar music artists to a user's favorite artist.

Prerequisites:
Python 3 installed
Spotify API account with access to the "Client Credentials Flow"
Spotify API access token stored in secrets.json file

Setup:
Clone or download the repository
Install required packages with pip install -r requirements.txt
Obtain a Spotify API access token by following the steps outlined in the official documentation
Store the access token in a secrets.json file with the following format:
{
    "access_token": "YOUR_ACCESS_TOKEN_HERE"
}


Usage:
Run the program with python main.py
Enter your favorite music artist when prompted
The program will display a list of similar artists, if any were found.
