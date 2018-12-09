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
	
def Analysis(sp):#, id):
	id = '3VmrLy4WZLHDgTXENCIz2p'#Mac Miller: Kool Aid and Forzen Pizza
	#print("audio analysis:\n",sp.audio_analysis(id))
	info = sp.audio_analysis(id)
	
	segments = info['segments']
	num =0
	for stuff in segments:
		if(stuff['start']):
			num+=1
	print("# of Segements: ",num) 
	
	
	
	
def Features(sp):#, tracks):	
	tracks = ["3VmrLy4WZLHDgTXENCIz2p","4fbvXwMTXPWaFyaMWUm9CR"]#Mac Miller: Kool Aid and Forzen Pizza and Bon Iver Holocene
	#print("audio features:\n",sp.audio_features(tracks))
	info = sp.audio_features(tracks)
	print("Dancability: ",info[0]['danceability'])
	print("Energy: ",info[0]['energy'])
	print("Valence: ",info[0]['valence'])
	#print("Popularity: ",info[0]['popularity'])
	
	print("Dancability: ",info[1]['danceability'])
	print("Energy: ",info[1]['energy'])
	print("Valence: ",info[1]['valence'])
	#print("Popularity: ",info[1]['popularity'])
	
	
def tempoGraph(sp,albumID):
		#dunkirk analysis
		
		tempo = []
		if albumID==None:
			albumID = '56hnQxU8h3Upf1nqR0fXYi'
		album = sp.album_tracks(albumID)#dunkirk album
		#get songs from the album
		for songs in album['items']:
			songID = userProf.getSongID(sp, songs['name']+' dunkirk')
			tempo.append(songStats.getTempo(sp, songID))
		for i in range(0,len(tempo)):
			x = numpy.arange(0,len(tempo[i]))
			plt.figure(i)
			plt.plot(x , tempo[i])
			plt.title("Song Tempo through time")
			plt.savefig('../examples/songTempo'+str(i))


	
	
	
	
	
	
	
