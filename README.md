![Package](https://img.shields.io/pypi/pyversions/Django.svg)
[![License](https://img.shields.io/badge/license-GNU-blue.svg)](https://github.com/DackJempsey/playlistMaker/blob/master/LICENSE.md)
[![Spotipy](https://img.shields.io/badge/library-spotipy-brightgreen.svg)](https://spotipy.readthedocs.io/en/latest/)
[![Matplotlib](https://img.shields.io/badge/library-matplotlib-brightgreen.svg)](https://matplotlib.org/index.html)
![Package](https://img.shields.io/badge/for-fun-orange.svg)

# playlistMaker-MusicData
With this program, witten in python, you can import your spotify playlist and it will create one for you.(That is the goal) Right now it is mainly used as a data gathering app, then that data will be used to created the playlist. By reverse engineering how spotify makes recomendations, I am hoping to improve upon their system of recomendations and user options.

If you would like to run this program you will need to do some legwork before hand since I have yet to build a 
solid UI. Go Here:https://developer.spotify.com/documentation/general/guides/authorization-guide/ and create a spotify app, to get your personla identification to use. Then export those stats by following these directions: https://spotipy.readthedocs.io/en/latest/#authorization-code-flow

It would also be good to have your Spotify user-Id(not your name) at hand.

There is a lot of data anylisis right now, becuase I would like to make sure that I get a good understanding about the data before I start using it to create the playlists.

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
#### Why is Loudness Important?
Loudness throughout a song is important when making a playlist becuase, you can make it so that the user has one song that begins with the same loudness as one song ends, for a better listening experience.

### Looking at Recomendations
Here are four graphs that represent 4 different recomendation requests. What we are looking at is how similar are the features of the song "seeds" to the songs that spotify recomends. The higher the feature on the graph the less likely it is that recomendations uses that feature of a song. The closer to 1 that the feature is the more likey that it is used. Some are labled for observation. I used my 5 top tracks, and then asked for recomendations based on those 5 tracks.

![example](https://github.com/DackJempsey/playlistMaker-MusicData/blob/master/examples/ratios1.png)
![example](https://github.com/DackJempsey/playlistMaker-MusicData/blob/master/examples/ratios2.png)
![example](https://github.com/DackJempsey/playlistMaker-MusicData/blob/master/examples/ratios3.png)
![example](https://github.com/DackJempsey/playlistMaker-MusicData/blob/master/examples/ratios4.png)

We can see that Danceability, Valence and Instrumentalness are usually very close to one, therfore they may be used more in recomendations. While Tempo and Key are usually quite high/different, and are therefore likely less used when making recomendations.
#### Why look at the recomendations?
Recomendations is how spotify gets new songs for users. This is usefull in a playlist becuase if a person is partial to a specific key, or tempo of a song, then they may want their playlist to reflect that. However right now it seems that spotify does not take those features into account. While those features may not be as important as valence or energy, I think it should be taken into account.


## Todo
Decide stats to use on making playlist.

Want solid data analysis

can do make type of playlist: Sad, Happy, Workout, Study

LOOK INTO KEY AND MODE on the effects on mood for more analysis

Workout tracks should have: high energy, High danceability, High Energy, high loudness\
Study/Chill tracks should have: High Valence, low tempo, low loudness, high instrumentalness\
Sad tracks should have: Low Valence, low tempo, low loudness, low energy\
Happy tracks should have: High Valence, High liveness (Key and mode need to be researched more)

If someone wants a playlist that takes a certain amount of time to finish

Get solid UI done, with stats display and such.
