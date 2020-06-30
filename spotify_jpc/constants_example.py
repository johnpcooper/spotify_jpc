env_vars = {'SPOTIPY_CLIENT_ID': 'your-spotify-client-id',
            'SPOTIPY_CLIENT_SECRET': 'your-spotify-client-secret',
            'SPOTIPY_REDIRECT_URI': 'http://localhost:9090',
            'DISPLAY': ':0'}

scope_list = ['user-modify-playback-state',
              'user-read-recently-played',
              'user-read-currently-playing',
              'playlist-modify-private',
              'playlist-modify-public']
              
scope = " ".join(scope_list)

user_vars = {'username': 'your-username',
             'playlist_db_path': r"C:\spotify_jpc\notebooks\playlist_db.csv",
			 'cache_path': r"C:\.spotify\.usercache"}

def package_path(**kwargs):
    """
    Return the path to the local installation
    of spotify_jpc
    """
    import spotify_jpc
    file = spotify_jpc.__file__
    try: # this will work on linux based OS
        end = file.rindex('/')
    except ValueError: # this will work on windows
        end = file.rindex('\\')
    package_path = file[:end+1]
    
    return package_path
    
package_path = package_path()

env_vars = {'SPOTIPY_CLIENT_ID': 'your-spotify-client-id',
            'SPOTIPY_CLIENT_SECRET': 'your-spotify-client-secret',
            'SPOTIPY_REDIRECT_URI': 'http://localhost:9090',
            'DISPLAY': ':0'}

scope_list = ['user-modify-playback-state',
			  'user-read-recently-played',
			  'user-read-playback-state',
			  'playlist-read-private',
			  'playlist-read-collaborative',
			  'user-read-currently-playing',
			  'playlist-modify-private',
			  'playlist-modify-public',
			  'user-top-read',
			  'user-read-playback-position']
scope = " ".join(scope_list)


user_vars = {'username': 'your-username',
             'playlist_db_path': f'{package_path}playlists_db.csv',
             'playlist_df_path': f'{package_path}playlists_df.csv',
             'cache_path': f'{package_path}.usercache'}