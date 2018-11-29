# playlistMaker
With this program, witten in python, you can import your spotify playlist and it will create one for you.

If you would like to run this program you will need to do some legwork before hand since I have yet to build a 
solid UI. Go Here:https://developer.spotify.com/documentation/general/guides/authorization-guide/ and create a spotify app, to get your personla identification to use. Then export those stats by following these directions: https://spotipy.readthedocs.io/en/latest/#authorization-code-flow

It would also be good to have your Spotify user-Id(not your name) at hand.

## Usage 
Make Playlist:
```
python3 main.py Playlist
```
Delete Playlist with playlist id:(Used for unit testing when creating multiple playlists in a row)
```
python3 main.py Playlist playlist-id-here
```
Get some data on songs and such:
```
python3 main.py GetData
```

## Libraries
I heavily rely on the spotipy: https://spotipy.readthedocs.io/en/latest/ library, and its great. Big thanks to those people that work on it and keep it up to date.

## Todo
Decide stats to use on making playlist.

Want solid data analysis

can do make type of playlist: Sad, Happy, Workout, Study

Get solid UI done, with stats display and such.
