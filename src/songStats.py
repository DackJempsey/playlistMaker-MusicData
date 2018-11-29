#this file will be were I take a look at all the stats
#for songs

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
	print("# Segements:\n",num) 
	
	
	
	
def Features(sp, tracks):	
	tracks = ["3VmrLy4WZLHDgTXENCIz2p"]#Mac Miller: Kool Aid and Forzen Pizza
	#print("audio features:\n",sp.audio_features(tracks))
	info = sp.audio_features(tracks)
	
