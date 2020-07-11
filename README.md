# spotify_jpc

This project is developed in the Windows subsystem for Linux, so there are some quirks specific to the WSL in these docs. Making it work in Windows is straightforward.

## Windows installation

```sh
cd C:\
git clone https://github.com/johnpcooper/spotify_jpc
cd spotify_jpc
```

Before installing the package, you need to get credentials configured with spotify and add them to `spotify_jpc\constants.py`:

1.  Create a spotify app on the [spotify developer dashboard](https://developer.spotify.com/dashboard/applications).
2. Get your client ID and client secret from the dashboard page
3. set up a redirect URI in dashboard page > edit settings. I recommend using the one that's already in `spotify_jpc/constants_example.py`
4. Change the name of `spotify_jpc/constants_example.py` to `spotify_jpc/constants.py` after adding the above information. Should look something like this:

```python
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
```

Now that `constants.py` is properly configured, you can install `spotify_jpc` and then use .ahk shortcuts:

```sh
pip install virtualenv
# Create a virtual environment in which to install the package. You could also
# just install it outside of a venv, but you'll need to remove the environment activation part of the ahk functions
cd C:\
python -m venv .spotify
.spotify\Scripts\activate
cd spotify_jpc
pip install -r requirements.txt
# Install the package in .spotify venv
python setup.py install
```

## Running Tkinter in the windows subsystem for linux

It was pretty annoying to make tkinter work in the WSL, but I wanted tkinter for a more universal form of OS clipboard access. You must install tkinter with the following:

```sh
$ sudo apt-get update
$ sudo apt-get install python3-tk
```

Then in order to get the tkinter root object (`Tk`), you need to install [Ximing X server for Windows](https://virtualizationreview.com/articles/2017/02/08/graphical-programs-on-windows-subsystem-on-linux.aspx) explained in this [tutorial](https://virtualizationreview.com/articles/2017/02/08/graphical-programs-on-windows-subsystem-on-linux.aspx).

## Future functionality

Need to make a function (`playlist.new_playlist`), which creates a playlist then adds it to `playlist.database()`. Then, if I only ever create new playlists with this function, I won't have to use `playlist.update_database(`) anymore.

Update `playlist.add_track_to_playlist()` so that it always checks for duplicate track in the playlist and asks for confirmation if the track is already there.