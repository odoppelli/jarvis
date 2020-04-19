import vlc
import time
import os

# VLC
def play_track():
    player.play()


def pause_track():
    player.pause()


def stop_track():
    player.pause()
    player.stop()


def next_track():
    player.next()


def previous_track():
    player.previous()
    

def play_this_track(audiobook_playlist, track):
    if track not in playlist:
        print("nonexistend track.")
    else:
        player.play_item_at_index(url_list.index(track))
        print('now playing:', track ,'\n')

# for Känguru Chroniken
def get_list_kanguru():
    kanguru_list = os.listdir('/home/pi/Audiobooks/Die_Känguru_Chroniken_[all]')
    kanguru_list.sort()
    kanguru_list_path = []
    for track in kanguru_list:
        kanguru_list_path.append(os.path.abspath(track))
    kanguru = {}
    intertvall = 5
    abteilungen_counter = 1
    tracks = len(kanguru_list_path)
    tracks_counter = 1
    abteilungen = (tracks // intervall) +1
    while abteilungen_counter <= abteilungen:
        tmp = str(abteilungen_counter)
        kanguru[tmp] = []
        abteilungen_counter += 1
    kanguru['1'] = [kanguru_list_path[0]]
    abteilungen_counter = 1
    while tracks_counter < tracks:
        if (tracks_counter % intervall) == 0:
            abteilungen_counter += 1
        abteilung = str(abteilungen_counter)
        kanguru[abteilung].append(kanguru_list_path[tracks_counter])
        tracks_counter +=1
    return kanguru


# for the hitchhikers guide to the galaxy
def get_list_hitchhiker():
    hitchhiker_list = os.listdir('/home/pi/Audiobooks/The_Hitchhiker_Guide_to_the_Galaxy_[all]')
    hitchhiker_list.sort()
    hitchhiker_list_path = []
    for track in hitchhiker_list:
        hitchhiker_list_path.append(os.path.abspath(track))
    hitchhiker = {}
    intervall = 5
    abteilungen_counter = 1
    tracks = len(hitchhiker_list_path)
    tracks_counter = 1
    abteilungen = (tracks // intervall) +1
    while abteilungen_counter <= abteilungen:
        tmp = str(abteilungen_counter)
        hitchhiker[tmp] = []
        abteilungen_counter += 1
    hitchhiker['1'] = [hitchhiker_list_path[0]]
    abteilungen_counter = 1
    while tracks_counter < tracks:
        if (tracks_counter % intervall) == 0:
            abteilungen_counter += 1
        abteilung = str(abteilungen_counter)
        hitchhiker[abteilung].append(hitchhiker_list_path[tracks_counter])
        tracks_counter +=1
    return hitchhiker


# VLC
def playlist_erstellen(audiobook_playlist):
    instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
    abteilung_counter = 1
    track_counter = 1
    MediaList = instance.media_list_new()
    for track in audiobook_playlist:
        MediaList.add_media(instance.media_new(track))
    global player
    player = instance.media_list_player_new()
    player.set_media_list(MediaList)



        
# EXAMPLE             
h= get_list_hitchhiker()
for x,y in h.items():
    print(x)
    for value in y:
        print (value)
k= get_list_kanguru()
for x,y in k.items():
    print(x)
    for value in y:
        print (value)

