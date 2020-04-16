import vlc
import time
url = 'http://streams.radiobob.de/bob-live/mp3-192/mediaplayer'
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
player=instance.media_player_new()
media=instance.media_new(url)
media.get_mrl()
player.set_media(media)
player.play()
