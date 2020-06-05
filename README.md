# Notes on using spotipy

It is important to develop in linux on this project, because setting environment variables is much easier in bash. To get started:

```bash
$ cd /home
$ python3 -m venv spotify_env
$ source spotify_env/bin/activate
```

First thing to do before using spotipy is to create a spotify developer dashboard and find your client ID and client secret. Then set your redirect URI according to spotify guidelines. The one here will work just fine and won't interfere with the port running your jupyter notebook.:

```sh
$ export SPOTIPY_CLIENT_ID=''
$ export SPOTIPY_CLIENT_SECRET=''
$ export SPOTIPY_REDIRECT_URI='http://example.com/callback/'
```

The above functionality is now implemened in utlities.py as bart of this project. Upon running anything with spotify_jpc or spotipy, always start with:

```python
from importlib import reload
from spotify_jpc import utilities
reload(utilities)
utilities.set_env_vars()
```

I think a better practice would be to put this in the .bashrc script, but I want it to be specific to this environment and don't know how to do that.

## Running Tkinter in the windows subsystem for linux

It's crazy how annoying this was to make happen, but I wanted it for a more universal form of OS clipboard access. You must install tkinter with the following:

```sh
$ sudo apt-get update
$ sudo apt-get install python3-tk
```

Then in order to get the tkinter root object (`Tk`), you need to install [Ximing X server for Windows](https://virtualizationreview.com/articles/2017/02/08/graphical-programs-on-windows-subsystem-on-linux.aspx) explained in this [tutorial](https://virtualizationreview.com/articles/2017/02/08/graphical-programs-on-windows-subsystem-on-linux.aspx). 