import vlc
import time

def min_to_sec(minutes):
    seconds = (minutes * 60) // 1
    return seconds

def hour_to_sec(hours):
    minutes = hours * 60
    seconds = min_to_sec(minutes)
    return seconds


def play_radio():
    player.play()


def pause_radio():
    player.pause()


def stop_radio():
    player.pause()
    player.stop()


def next_radio():
    player.next()


def previous_radio():
    player.previous()


def play_this_radio(radioid):
    if radioid not in radiosender:
        print("nonexistend radio ID.")
    else:
        player.play_item_at_index(url_list.index(radiosender.get(radioid)))
        print('now playing:', radioid ,'\n')


radiosender = {
    'hochschulradio': 'http://evans.hochschulradio.rwth-aachen.de:8000/radio_low.mp3',
    'charts_musik': 'http://charthits-high.rautemusik.fm/',
    'trance_musik': 'http://trance-high.rautemusik.fm/',
    'deutschrap_musik': 'http://deutschrap-high.rautemusik.fm/',
    'rock_musik': 'http://rock-high.rautemusik.fm/',
    'house_musik': 'http://house-high.rautemusik.fm/',
    'sex_musik': 'http://sex-high.rautemusik.fm/',
    'happy_musik': 'http://happy-high.rautemusik.fm/',
    'eins_live': 'http://wdr-1live-live.icecast.wdr.de/wdr/1live/live/mp3/128/stream.mp3',
    'wdr2': 'http://wdr-wdr2-aachenundregion.icecast.wdr.de/wdr2/aachenundregion/mp3/128/stream.mp3'
}

url_list = []
for sender_url in radiosender:
    url_list.append(radiosender[sender_url])

instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

MediaList = instance.media_list_new()
for url in url_list:
    MediaList.add_media(instance.media_new(url))

player = instance.media_list_player_new()
player.set_media_list(MediaList)


# EXAMPLE
print('Radio IDs:')
for sender in radiosender:
    print(sender)
print()

play_radio()
time.sleep(15)
pause_radio()
time.sleep(5)
play_radio()
time.sleep(10)
next_radio()
time.sleep(10)
play_this_radio('sex_musik')
time.sleep(min_to_sec(1.5))
play_this_radio('hochschulradio')
time.sleep(min_to_sec(1))
stop_radio()

