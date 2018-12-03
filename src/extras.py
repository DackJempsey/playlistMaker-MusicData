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
	


def showTimbre(sp, songID):
	analysis = sp.audio_analysis(songID)
	segments = analysis['segments']
	length = []
	timbre = []
	for info in segments:
		length.append(info['start'])
		timbre.append(info['timbre'])
		
	
	for i in range(0,11):
		stuff=[]
		for items in timbre:
			stuff.append(items[i])
		plt.plot(length, stuff)

		plt.hold(True)
	plt.title("Timbre of Your Song")
	plt.xlabel("Time in seconds")
	plt.ylabel("Some Random Stuff")
	plt.hold(False)
	plt.show()

def showTimeSig(sp, songID):
	analysis = sp.audio_analysis(songID)
	segments = analysis['sections']
	length = []
	timeSig = []
	for info in segments:
		timeSig.append(info['time_signature'])
		length.append(info['start'])
	plt.plot(length, timeSig)
	plt.title("Time Signature of a Song")
	plt.xlabel("Time in Seconds")
	plt.ylabel("Over 7")
	plt.show()
	
