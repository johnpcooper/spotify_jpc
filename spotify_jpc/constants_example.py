env_vars = {'SPOTIPY_CLIENT_ID': '770adfb757ddac74f730a65fa6b56b496',
            'SPOTIPY_CLIENT_SECRET': 'f1964dd3424bb37c395e7849e645c',
            'SPOTIPY_REDIRECT_URI': 'http://localhost:9090',
            'DISPLAY': ':0'}

scope_list = ['user-modify-playback-state',
              'user-read-recently-played',
              'user-read-currently-playing',
              'playlist-modify-private',
              'playlist-modify-public']
              
scope = " ".join(scope_list)

user_vars = {'username': 'anothergriningsoul',
             'playlist_db_path': r"C:\spotify_jpc\notebooks\playlist_db.csv",
			 'cache_path': r"C:\.spotify\.usercache"}