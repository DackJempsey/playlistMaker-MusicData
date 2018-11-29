#this file will be were I take a look at all the stats
#for songs
import numpy as np
import matplotlib as mpl
import userProf

def songInfo(sp):
	#id = '3VmrLy4WZLHDgTXENCIz2p'
	#print("audio analysis:\n",sp.audio_analysis(id))
	#tracks = ["3VmrLy4WZLHDgTXENCIz2p"]
	#print("audio features:\n",sp.audio_features(tracks))
	print("done nothing")

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
	
	print("Dancability: ",info[1]['danceability'])
	print("Energy: ",info[1]['energy'])
	print("Valence: ",info[1]['valence'])
	
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
	for stuff in info['tracks']['items']:
		#print(stuff['track']['name'])
		songID = stuff['track']['id']
		#print(classifySong(sp, songID))
		if(classifySong(sp, songID) == "HAPPY"):
			score+=1
		else:
			score-=1
		n+=1
	print(score)
	if(score >0 ):
		return "HAPPY"
	else:
		return "Less HAPPY"
		
	#print(n)
	

'''
LOOK INTO KEY AND MODE on the effects on mood for more analysis

Workout tracks should have: high energy, High danceability, High Energy, high loudness
Study/Chill tracks should have: High Valence, low tempo, low loudness, high instrumentalness
Sad tracks should have: Low Valence, low tempo, low loudness, low energy
Happy tracks should have: High Valence, High liveness (Key and mode need to be researched more)
'''





