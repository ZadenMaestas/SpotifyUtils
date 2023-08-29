import spotipy
from spotipy.oauth2 import SpotifyOAuth


def authenticate_spotify():
    # Initialize the SpotifyOAuth object
    sp_oauth = SpotifyOAuth(
        client_id='CLIENT_ID',
        client_secret='CLIENT_SECRET',
        redirect_uri='https://localhost:8888/callback',
        scope='user-library-read playlist-read-private'
    )

    # Attempt to load a previously obtained token from a file
    token_info = sp_oauth.get_cached_token()

    # If a cached token is not available or it has expired, prompt the user to authorize
    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        print(f"Please visit this URL to authorize your application: {auth_url}")
        auth_response = input("Enter the URL you were redirected to: ")

        # Parse the URL to get the authorization code
        code = sp_oauth.parse_response_code(auth_response)

        # Request an access token using the authorization code
        token_info = sp_oauth.get_access_token(code)

    # Initialize the Spotify client with the obtained access token
    if token_info:
        return spotipy.Spotify(auth=token_info['access_token'])
    else:
        return None


def get_playlist_tracks_as_text_file(sp, playlist_id, playlist_name):
    # Get the playlist tracks
    tracks = []
    offset = 0
    limit = 100  # You can adjust this value based on your needs

    while True:
        results = sp.playlist_items(playlist_id, offset=offset, limit=limit)
        if not results['items']:
            break

        for track in results['items']:
            track_name = track['track']['name']
            artist_name = track['track']['artists'][0]['name']
            tracks.append(f"{track_name} - {artist_name}")

        offset += limit

    # Save the tracks to a text file
    file_name = f"{playlist_id}.txt"
    with open(file_name, 'w', encoding='utf-8') as text_file:
        text_file.write('\n'.join(tracks))

    print(f"Playlist tracks saved to '{file_name}'")


def archive_collaborative_playlist(sp, playlist_id):
    # Get the playlist tracks
    tracks = []
    offset = 0
    limit = 100  # You can adjust this value based on your needs

    while True:
        results = sp.playlist_items(playlist_id, offset=offset, limit=limit)
        if not results['items']:
            break

        for track in results['items']:
            track_name = track['track']['name']
            artists = [artist['name'] for artist in track['track']['artists']]
            added_by = track['added_by']['id']
            tracks.append(f"{track_name} - {' & '.join(artists)} (Added by {added_by})")

        offset += limit

    # Save the tracks to a text file
    file_name = f"{playlist_id}_archive.txt"
    with open(file_name, 'w', encoding='utf-8') as text_file:
        text_file.write('\n'.join(tracks))

    print(f"Collaborative playlist tracks archived to '{file_name}'")


def get_playlists(sp):
    # Get the user's playlists
    playlists = []
    offset = 0
    limit = 50  # You can adjust this value based on your needs

    while True:
        results = sp.current_user_playlists(offset=offset, limit=limit)
        if not results['items']:
            break

        for playlist in results['items']:
            playlists.append({
                'name': playlist['name'],
                'id': playlist['id']
            })

        offset += limit

    # Print the user's playlists
    for i, playlist in enumerate(playlists, start=1):
        print(f"{i}. {playlist['name']} (ID: {playlist['id']}")

    return playlists


def main():
    sp = authenticate_spotify()
    if not sp:
        print("Unable to obtain access token")
        return

    playlists = get_playlists(sp)

    try:
        selected_playlist = input("Please enter a playlist number (or manually specify ID)> ")
        selected_playlist = int(selected_playlist)
        selected = playlists[selected_playlist]
        print(f"Selected {selected['name']}")
    except ValueError:
        selected_playlist = input("Please enter the playlist ID> ")  # Manually specify the playlist ID
        selected = sp.playlist(selected_playlist)
        print(f"Selected {selected['name']}")

    print(
        "\nAvailable options:\n1. Get playlist as a text file\n2. Archive collaborative playlist as a text file\n\n(More options coming soon)")
    chosen_option = input("Option number > ")
    chosen_option = int(chosen_option)

    if chosen_option == 1:
        get_playlist_tracks_as_text_file(sp, selected["id"], selected["name"])
    elif chosen_option == 2:
        archive_collaborative_playlist(sp, selected["id"])


if __name__ == "__main__":
    main()
