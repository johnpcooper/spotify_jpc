# Notes on using spotipy

It is important to develop in linux on this project, because setting environment variables is much easier in bash. To get started:

```bash
$ cd /home
$ python3 -m venv spotify_env
$ source spotify_env/bin/activate
```

Thesea are my actual credentials being stored as environment variables. Go to spotify account to check them:

```sh
$ export SPOTIPY_CLIENT_ID='7702757ddac74f70a0a35fa98b56b494'
$ export SPOTIPY_CLIENT_SECRET='f1964dd2a1614253bb37c395e39e645c'
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