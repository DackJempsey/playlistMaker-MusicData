![Package](https://img.shields.io/pypi/pyversions/Django.svg)
[![License](https://img.shields.io/badge/license-GNU-blue.svg)](https://github.com/DackJempsey/playlistMaker/blob/master/LICENSE.md)
[![Spotipy](https://img.shields.io/badge/library-spotipy-brightgreen.svg)](https://spotipy.readthedocs.io/en/latest/)
[![Matplotlib](https://img.shields.io/badge/library-matplotlib-brightgreen.svg)](https://matplotlib.org/index.html)
![Package](https://img.shields.io/badge/for-fun-orange.svg)

# playlistMaker-MusicData
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
I heavily rely on the spotipy: https://spotipy.readthedocs.io/en/latest/ library, and its great. I have been told that updates stopped about a year ago, however it still works great!

## Examples of Data
![example](https://github.com/DackJempsey/playlistMaker/blob/master/examples/LetItHappen.png)

### Looking at Recomendations
Here are four graphs that represent 4 different recomendation requests. What we are looking at is how similare are some features of the song "seeds" to the one spotify gives. The higher the feature on the graph the less likely it is that recomendations uses that feature of a song. The closer to 1 that the feature is the more likey that it is used. Some are labled for observation.

![example](https://github.com/DackJempsey/playlistMaker-MusicData/blob/master/examples/ratios1.png)
![example](https://github.com/DackJempsey/playlistMaker-MusicData/blob/master/examples/ratios2.png)
![example](https://github.com/DackJempsey/playlistMaker-MusicData/blob/master/examples/ratios3.png)
![example](https://github.com/DackJempsey/playlistMaker-MusicData/blob/master/examples/ratios4.png)



## Todo
Decide stats to use on making playlist.

Want solid data analysis

can do make type of playlist: Sad, Happy, Workout, Study

LOOK INTO KEY AND MODE on the effects on mood for more analysis

Workout tracks should have: high energy, High danceability, High Energy, high loudness\
Study/Chill tracks should have: High Valence, low tempo, low loudness, high instrumentalness\
Sad tracks should have: Low Valence, low tempo, low loudness, low energy\
Happy tracks should have: High Valence, High liveness (Key and mode need to be researched more)

Get solid UI done, with stats display and such.

Need to chanege some if statements to exeptions for error
