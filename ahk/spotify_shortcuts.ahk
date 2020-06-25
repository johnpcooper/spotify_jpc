; Use spotify_jpc to search spotify for whatever's on the clipboard and, if any tracks show
; up in results, play the first one. Won't work if spotify isn't active on a device

; This is a good example of how to activate an environment and then run a function from a
; package that's installed in that environment using AHK.

; This way, I can just script like in Ipython in working environment
^!1::

  env = C:\.spotify\Scripts\activate
  pycommand := "from spotify_jpc import playback; playback.play_clipboard()"
  run, %comspec% /c %env% & python -c "%pycommand%"

return

; Add currently playing track to the singles playlist
; corresponding to its release date
^!2::

  env = C:\.spotify\Scripts\activate
  pycommand := "from spotify_jpc.playlist import add_current_track_to_playlist; add_current_track_to_playlist()"
  run, %comspec% /c %env% & python -c "%pycommand%"

return