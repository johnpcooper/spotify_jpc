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