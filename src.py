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


import os,sys, spotipy, json, webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError



import spotipy.util as util

def main(args):


	username ='1210610133'
	scope = 'user-read-library user-read-private user-read-playback-state user-modify-playback-state'

	'''
	if len(sys.argv) > 1:
		username = sys.argv[1]
	else:
		print ("Usage: %s username" % (sys.argv[0],))
		sys.exit()
	'''

	try:
		token = util.prompt_for_user_token(username,scope)
	except:#(AttributeError, JSONDecodeError):
		os.remove(f".cache-{username}")
		token = util.prompt_for_user_token(username,scope)

		#creates spotipy object
	#sp = spotipy.Spotify(auth=token)
	if token:
		sp = spotipy.Spotify(auth=token)
		results = sp.current_user_saved_tracks()
		for item in results['items']:
			track = item['track']
			print (track['name'] + ' - ' + track['artists'][0]['name'])
	else:
		print( "Can't get token for", username)

	#https://spotipy.readthedocs.io/en/latest/#spotipy.client.Spotify.current_user_playing_track
	track = sp.current_user_playing_track()
	artist = track['item']['artists'][0]['name']
	track = track['item']['name']

	if artist != "":
		print("Currently playing " + artist + " - " + track)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
