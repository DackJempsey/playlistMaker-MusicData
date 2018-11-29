#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  userProf.py
#  
#  Copyright 2018 Jack Dempsey <jackdempsey@rgnt2-102-74-dhcp.int.colorado.edu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  This portion of the code creates a user profile based on saved songs
#	things to do: take random sample of tracks from user.
#	Get the type of song, and can also get related artists.


def userProf(sp, user):
	#can use affinity score to help profile
	print("test")
	
	
	
def getSample(sp, user, numberOfTracks):
	#lets say people add aprox 3 songs within the same artist or style, 
	#lets do every third song. If they have a whole album then that would
	#skew the stats towards that artist/style
	#can also use spotifys afinity score 
	print("test")

def getPLaylistsID(sp,username):
	PLName = input("Please enter the Name of playlist you wish to look at:")
	playlists = sp.user_playlists(username, limit=50, offset=0)
	for items in playlists['items']:
		if(PLName == items['name']):
			return items['id']
	
	



