import time


def getTracks(sp):
	#saved tracks
	results = sp.current_user_saved_tracks()
	for item in results['items']:
		track = item['track']
		print (track['name'] + ' - ' + track['artists'][0]['name'])

def currPlaying(sp):
	#https://spotipy.readthedocs.io/en/latest/#spotipy.client.Spotify.current_user_playing_track		
	track = sp.current_user_playing_track()
	artist = track['item']['artists'][0]['name']
	track = track['item']['name']
	while(artist != ""):
		print("Updates every 2 minutes\n")
		print("Currently playing " + artist + " - " + track+"\n")
		time.sleep(120)#wait 2 minutes before checking again
	print("Nothing Playing")	
	


