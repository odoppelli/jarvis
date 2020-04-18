import vlc
import time

action_play = False
action_pause = False
action_stop = False
action_next = False
action_previous = False

def play_radio():
    player.play()

def pause_radio():
    player.pause()

def stop_radio():
    player.pause()
    player.stop()

def next_radio():
    player.next()

hochschulradio = 'http://evans.hochschulradio.rwth-aachen.de:8000/radio_low.mp3'
club_musik = 'http://club-high.rautemusik.fm/'
url_list = [hochschulradio, club_musik]


instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

MediaList = instance.media_list_new()
for url in url_list:
    MediaList.add_media(instance.media_new(url))

list_player = instance.media_list_player_new()
list_player.set_media_list(MediaList)


'''
player = instance.media_player_new()
media = instance.media_new(url)
player.set_media_list(url_list)
media.get_mrl()
player.set_media(media)
player.play()
'''



# EXAMPLE
play_radio()
time.sleep(10)
pause_radio()
time.sleep(5)
play_radio()
time.sleep(10)
next_radio()
time.sleep(10)
play_radio(10)
time.sleep(10)
stop_radio()


print('beendet')
