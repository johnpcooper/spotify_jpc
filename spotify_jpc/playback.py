from spotify_jpc.utilities import get_user_sp, get_clipboard_uri, set_env_vars

def play_clipboard(**kwargs):
    """
    Search spotify for whatever's on the clipboard and
    play the first resulting track
    """
    set_env_vars()
    track_uri = get_clipboard_uri()
    sp = get_user_sp()

    if track_uri:
        sp.start_playback(uris=[track_uri])
        print(f"Playing track")
    else:
        print("Couldn't find a track with this clipboard query")