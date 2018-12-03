#this file will be were I take a look at all the stats
#for songs
import numpy as np
import matplotlib.pyplot as plt
import userProf, time, animations

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
	
	
def getLoudnessPLot(sp,songID):
	info = sp.audio_analysis(songID)
	segments =info['segments']
	loudness =[]
	time = []
	for info in segments:
		loudness.append(info['loudness_max'])
		time.append(info['start'])	

	#take out the not so loud intro
	for i in range(0,5):
		time.pop(i)
		loudness.pop(i)

	plt.plot(time, loudness)
	plt.title("Loudness of Your Song")
	plt.xlabel("Time in seconds")
	plt.ylabel("Volume in Decebels")
	plt.savefig('LetItHappen.png')

def getBeats(sp, songID):
	analysis = sp.audio_analysis(songID)
	segments = analysis['beats']
	length = []
	beats = []
	for info in segments:
		length.append(info['duration'])
		beats.append(info['confidence'])
	songID = ['spotify:track:'+songID]
	#sp.start_playback(device_id=None,context_uri=None,uris=songID,offset=None,)
	#when testing if beats match song
	for b in range(0,len(beats)):
		for l in range(0,int(beats[b]*20)):
			print('.', end='')
		time.sleep(length[b])
		print(' ')
	
	
	
	
def classifySong(sp, songID):#takes in a string, but features api needs array
	songID = [songID]
	info = sp.audio_features(songID)
	
	stats = [info[0]['danceability'],info[0]['energy'],info[0]['valence']]
	score = np.sum(stats)/len(stats)
	#print("Score: ",score)
	if score >=.5:
		return "HAPPY"
	else:
		return"Less HAPPY"

def classifPlaylist(sp,user):
	PLid = userProf.getPLaylistsID(sp,user)
	info = sp.user_playlist(user,PLid,fields =None)
	n=0
	score =0
	if(info['tracks'] == None):
		print("problem with playlist")
		return 0
	for stuff in info['tracks']['items']:
		#print(stuff['track']['name'])
		songID = stuff['track']['id']
		if (songID == None):
			break
		if(classifySong(sp, songID) == "HAPPY"):
			score+=1
		else:
			score-=1
		n+=1
	#print(score/n)# 1 is very happy, -1 is not happy at all, 0 is neutral
	return score/n




'''
LOOK INTO KEY AND MODE on the effects on mood for more analysis

Workout tracks should have: high energy, High danceability, High Energy, high loudness
Study/Chill tracks should have: High Valence, low tempo, low loudness, high instrumentalness
Sad tracks should have: Low Valence, low tempo, low loudness, low energy
Happy tracks should have: High Valence, High liveness (Key and mode need to be researched more)
'''





