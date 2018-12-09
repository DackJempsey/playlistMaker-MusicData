#this file will be were I take a look at all the stats
#for songs
import numpy as np
import matplotlib.pyplot as plt
import userProf, time, animations

	
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

def getTempo(sp, songID):
	analysis = sp.audio_analysis(songID)
	section = analysis['sections']
	tempo=[]
	for info in section:
		tempo.append(info['tempo'])
	return tempo
	
	
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

#What I will try to do is reverse engineer the recomendations to see what
#values my top tracks have in common with recomended to see how
#spotify gets recomended and see if there can be improvment

def getFeatureAvg(sp,songIDs):
	Features=[]
	for songID in songIDs:
		Features.append(sp.audio_features(songID))
	
	#get averages of each and plot each average
	avgDance = avgEnergy=avgKey = avgMode = avgTimeSig =avgAcoust = avgInst =avgLive = avgLoud =avgSpeech = 0
	avgVal = avgTemp = 0
	ret = []
	for items in Features:
		avgDance = avgDance + items[0]['danceability']
		avgEnergy = avgEnergy + items[0]['energy']
		avgKey = avgKey + items[0]['key']
		avgMode= avgMode + items[0]['mode']
		avgTimeSig = avgTimeSig + items[0]['time_signature']
		avgAcoust = avgAcoust + items[0]['acousticness']
		avgInst = avgInst + items[0]['instrumentalness']
		avgLive = avgLive + items[0]['liveness']
		avgLoud = avgLoud + items[0]['loudness']
		avgSpeech = avgSpeech + items[0]['speechiness']
		avgVal = avgVal + items[0]['valence']
		avgTemp = avgTemp + items[0]['tempo']
	
	ret = [avgDance,avgEnergy,avgKey,avgMode,avgTimeSig,avgAcoust,avgInst,avgLive,avgLoud,avgSpeech,avgVal,avgTemp ]
	ret[:] = [i / 5 for i in ret]
	return ret
	

def reversRec(sp, userID):
	#need to get my top tracks
	#get a list of recomended
	#get features data for each song in each list
	topIds =[]
	tracks = sp.current_user_top_tracks(limit=5, offset=0,time_range='short_term')
	for items in tracks['items']:
		topIds.append(items['id'])
	
	recIDs=[]
	recom = sp.recommendations(seed_artists=None , seed_genres=None , seed_tracks=topIds , limit=5 , country=None)
	for items in recom['tracks']:
		recIDs.append(items['id'])
		
	topTrackAvg = getFeatureAvg(sp,topIds)
	recAvg = getFeatureAvg(sp,recIDs)
	diff = [i-j for i,j in zip(topTrackAvg, recAvg)]
	#Here we are essentially using the relative errors to compare stats
	TruDiff = [(i+1)/(j+1) for i,j in zip(topTrackAvg, diff)]
	num = np.arange(0,12)
	plt.plot(num,TruDiff,'g*')
	plt.hold(True)
	plt.axhline(y=1,xmin=0,xmax=1)
	plt.text(num[10],TruDiff[10],'10:valence')
	plt.text(num[2],TruDiff[2],'2:Key')
	plt.text(num[11],TruDiff[11],'11:Tempo')
	plt.text(num[0],TruDiff[0],'0:Danceability')
	plt.text(num[6],TruDiff[6], '6:Instrumentalness')
	plt.title("How different are the features between Top songs and Recomended songs")
	plt.xlabel("Various Song features")
	plt.ylabel("Ratio of values")
	plt.hold(False)
	plt.savefig('../examples/ratios4.png')





'''
LOOK INTO KEY AND MODE on the effects on mood for more analysis

Workout tracks should have: high energy, High danceability, High Energy, high loudness
Study/Chill tracks should have: High Valence, low tempo, low loudness, high instrumentalness
Sad tracks should have: Low Valence, low tempo, low loudness, low energy
Happy tracks should have: High Valence, High liveness (Key and mode need to be researched more)
'''





