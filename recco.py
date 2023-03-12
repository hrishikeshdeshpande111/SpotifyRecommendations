import requests
import json

def get_recommendations(artist):
    """Given an artist name, returns a list of similar artists."""
    
    url = f'https://api.spotify.com/v1/search?q={artist}&type=artist'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        artists = data['artists']['items']
        if len(artists) > 0:
            artist_id = artists[0]['id']
            url = f'https://api.spotify.com/v1/artists/{artist_id}/related-artists'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                recommendations = data['artists']
                return [rec['name'] for rec in recommendations]
    
    return []

# Get user input
favorite_artist = input("What is your favorite music artist? ")

# Set up headers for Spotify API request
with open('recco/secrets.json') as f:
    secrets = json.load(f)
    access_token = secrets['access_token']
    headers = {'Authorization': f'Bearer {access_token}'}

# Get recommendations
recommendations = get_recommendations(favorite_artist)

# Print recommendations
if len(recommendations) > 0:
    print(f"Here are some similar artists to {favorite_artist}:")
    for artist in recommendations:
        print(artist)
else:
    print(f"Sorry, we could not find any similar artists to {favorite_artist}.")
