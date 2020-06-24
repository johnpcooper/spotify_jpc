# spotify_jpc

This project is developed in the Windows subsystem for Linux, so there are some quirks specific to the WSL in these docs. Making it work in Windows is straightforward.

## Windows installation

```sh
cd C:\
git clone https://github.com/johnpcooper/spotify_jpc
cd spotify_jpc
```

Before installing the package, you need to get credentials configured with spotify and add them to `spotify_jpc\constants.py`. Create a spotify app on the [spotify developer dashboard](https://developer.spotify.com/dashboard/applications). Get your client ID and client secret and set up a redirect URI. I recommend using the one that's already in `spotify_jpc/constants_example.py`. Change the name of `spotify_jpc/constants_example.py` to `spotify_jpc/constants.py` after adding the above information. Should look something like this:

```python
env_vars = {'SPOTIPY_CLIENT_ID': '770adfb757ddac74f730a65fa6b56b496',
            'SPOTIPY_CLIENT_SECRET': 'f1964dd3424bb37c395e39e645c',
            'SPOTIPY_REDIRECT_URI': 'http://localhost:9090',
            'DISPLAY': ':0'}

user_vars = {'username': 'anothergriningsoul',
             'playlist_db_path': r"C:\spotify_jpc\notebooks\playlist_db.csv"}
```

Now that `constants.py` is properly configured, you can install `spotify_jpc` and the use the .ahk shortcuts.

```sh
pip install virtualenv
# Create a virtual environment in which to install the package. You could also
# just install it outside of a venv, but you'll need to update the ahk scripts 
# accordingly
cd C:\
python -m venv .spotify
.spotify\Scripts\activate
cd spotify_jpc
pip install -r requirements.txt
# Install the package in .spotify venv
python setup.py install
```

## Running Tkinter in the windows subsystem for linux

It was pretty annoying to make tkinter work in the WSL, but I wanted it for a more universal form of OS clipboard access. You must install tkinter with the following:

```sh
$ sudo apt-get update
$ sudo apt-get install python3-tk
```

Then in order to get the tkinter root object (`Tk`), you need to install [Ximing X server for Windows](https://virtualizationreview.com/articles/2017/02/08/graphical-programs-on-windows-subsystem-on-linux.aspx) explained in this [tutorial](https://virtualizationreview.com/articles/2017/02/08/graphical-programs-on-windows-subsystem-on-linux.aspx).

## Future functionality

Create database of all the artist names already in my playlists (or a more refined version of this list) and automatically scrape music blogs for new posts about them. Also could just search spotify and see if there are any new track results since last search, if so add them to playlist. 

Need to make my google docs/sheets best albums etc. lists accessible. Will put them in box sync as csvs.

database module would construct dictionaries (or dataframes) of playlists with:

```python
playlist_dict = {'name': "2020 June",
                 'type': "singles",
                 'spotify_id', 'xyz321'}
```

Create dataframe with each `playlist_dict` then `pd.concat` them to create master `playlists_df`.

Should also create tracks_df for each playlist with track_id, artist, album, release date etc.

