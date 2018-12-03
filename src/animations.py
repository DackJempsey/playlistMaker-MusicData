import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import os,sys


def baseAnimation():# take base vector and valence 
	fig2 = plt.figure()

	x = np.arange(-25, 25)
	y = np.arange(-25,25).reshape(-1, 1)#(y vecter )
	x = np.linspace(0, 2 * np.pi, 120)
	y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
	
	base = np.hypot(x, y)#returns hypotnues of (sqrt(x**2 + y ** 2))
	#the key to all of this is creating an ims that is the correct pattern of bases
	ims = []
	
	#change colors depending on "valence"
	for add in np.arange(60):
		#ims.append((plt.pcolor(x, y, base+ add, norm=plt.Normalize(15, 50),snap=True),))
		x += np.pi / 15.
		y += np.pi / 20.
		im = plt.imshow((np.sin(x)+np.cos(y)), animated=True)
		ims.append([im])
		
	#interval needs to be length of song
	#repeat dealay needs to be length of base
	im_ani= animation.ArtistAnimation(fig2, ims, interval=5, repeat=True, blit=False)
	#animation.new_frame_seq()
	plt.show()

	# To save this second animation with some metadata, use the following command:
	# im_ani.save('im.mp4', metadata={'artist':'Guido'})

	



def main(args):
	baseAnimation()

	

if __name__ == '__main__':

    sys.exit(main(sys.argv))
