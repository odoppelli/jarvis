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
charts_musik = 'http://charthits-high.rautemusik.fm/'
trance_musik = 'http://trance-high.rautemusik.fm/'
deutschrap_musik = 'http://deutschrap-high.rautemusik.fm/'
rock_musik = 'http://rock-high.rautemusik.fm/'
house_musik = 'http://house-high.rautemusik.fm/'
sex_musik = 'http://sex-high.rautemusik.fm/'
happy_musik = 'http://happy-high.rautemusik.fm/'
eins_live = 'http://wdr-1live-live.icecast.wdr.de/wdr/1live/live/mp3/128/stream.mp3'
wdr2 = 'http://wdr-wdr2-aachenundregion.icecast.wdr.de/wdr2/aachenundregion/mp3/128/stream.mp3'

url_list = [hochschulradio, eins_live, wdr2, charts_musik, trance_musik, deutschrap_musik, rock_musik, house_musik, happy_musik, sex_musik]


instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

MediaList = instance.media_list_new()
for url in url_list:
    MediaList.add_media(instance.media_new(url))

player = instance.media_list_player_new()
player.set_media_list(MediaList)


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
time.sleep(15)
pause_radio()
time.sleep(5)
play_radio()
time.sleep(10)
next_radio()
time.sleep(10)
player.play_item_at_index(9)
time.sleep(10)
player.play_item_at_index(0)
time.sleep(10)
stop_radio()



print('beendet')
