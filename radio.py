import vlc
import time
#url = 'http://streams.radiobob.de/bob-live/mp3-192/mediaplayer'
url = 'http://evans.hochschulradio.rwth-aachen.de:8000/radio_low.mp3'
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
player=instance.media_player_new()
media=instance.media_new(url)
media.get_mrl()
player.set_media(media)

def play():
    player.play()

def pause():
    player.pause()

def stop():
    player.pause()
    player.stop()

# EXAMPLE
play()
time.sleep(10)
pause()
time.sleep(5)
play()
time.sleep(5)
stop()
print('beendet')
