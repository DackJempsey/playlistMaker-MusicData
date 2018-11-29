#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
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
#


import os,sys, spotipy, json, webbrowser, time, userProf, extras
import songStats
import spotipy.util as util
from json.decoder import JSONDecodeError



import spotipy.util as util

def login(username, scope):
	client_id = '845e268204ee4704bb1e441090062f85'
	client_secret = 'd945e2adad244d769c4f71d2e640937c'
	redirect_uri = 'https://github.com/DackJempsey/playlistMaker'
	try:
		token = util.prompt_for_user_token(username,scope, client_id, client_secret, redirect_uri)
	except:#(AttributeError, JSONDecodeError):
		os.remove(f".cache-{username}")
		token = util.prompt_for_user_token(username,scope,client_id, client_secret, redirect_uri)

	#creates spotipy object
	#sp = spotipy.Spotify(auth=token)
	if token:
		sp = spotipy.Spotify(auth=token)
		return sp
	else:
		print( "Can't get token for", username)
		return -1

def createPlaylist(sp,user):
	PLname = input("Enter playlist name you wish to create: ")
	print("creating Playlist "+PLname+ " now")
	
	Info = sp.user_playlist_create(user, PLname, public=False,description="Made with Python")
	PLid = Info['id']
	print(PLid)
	return PLid
	
def deletePlaylist(sp,PLid,username):
	sp.user_playlist_unfollow(username, PLid)



def addSongs(sp, user, PLid,tracks):
	sp.user_playlist_add_tracks(user, PLid, tracks, position = 0)


def main(args):

	#make this a user input
	username ='1210610133'
	scope = 'user-library-read user-read-private user-read-playback-state\
		user-modify-playback-state playlist-modify-public playlist-modify-private'
	sp = login(username, scope)
	
	#extras.getTracks(sp)
	#extras.currPlaying(sp)
	#print("search: ",sp.search("Mac Miller",limit=5,offset=0,type='artist',market=None))
	songStats.Analysis(sp)

	
	'''
	if(len(args)>1):
		PLid = args[1]
		deletePlaylist(sp,PLid,username)
	else:
		PLid = createPlaylist(sp,username)
		addSongs(sp, username, PLid, tracks)
	'''


if __name__ == '__main__':

    sys.exit(main(sys.argv))
