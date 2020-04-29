import vlc
import time
import os


class WeckerPlayer:
    def __init__(self, playlist):
        self.Playlist = playlist
        self.MediaList = self.Instance.media_list_new()

        for track in self.Playlist:
            self.MediaList.add_media(self.Instance.media_new(track))

        self.player = self.Instance.media_list_player_new()
        self.player.set_media_list(self.MediaList)

    def play_media(self):
        self.player.play()

    def pause_media(self):
        self.player.pause()

    def stop_media(self):
        self.player.pause()
        self.player.stop()

    def next_media(self):
        self.player.next()

    def previous_media(self):
        self.player.previous()


class WeckerRadio(WeckerPlayer):
    def __init__(self):
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
        }
        url_list = []
        for sender_url in radiosender:
            url_list.append(radiosender[sender_url])
        super().__init__(url_list)


class HitchhikersGuide(WeckerPlayer):
    def __init__(self, cd_number):
        cds = {
            '1': "/home/pi/Audiobooks/The_Hitchhikers_Guide_to_the_Galaxy/The_Hitchhiker's_Guide_To_The_Galaxy_Disc1",
            '2': "/home/pi/Audiobooks/The Hitchhikers Guide to the Galaxy/The Hitchhiker's Guide To The Galaxy [Disc 2]",
            '3': "/home/pi/Audiobooks/The Hitchhikers Guide to the Galaxy/The Hitchhiker's Guide To The Galaxy [Disc 3]",
            '4': "/home/pi/Audiobooks/The Hitchhikers Guide to the Galaxy/The Hitchhiker's Guide To The Galaxy [Disc 4]",
            '5': "/home/pi/Audiobooks/The Hitchhikers Guide to the Galaxy/The Hitchhiker's Guide To The Galaxy [Disc 5]"
            }
        hitchhiker_list = os.listdir(cds.get(str(cd_number)))
        hitchhiker_list.sort()
        hitchhiker_list_path = []
        for track in hitchhiker_list:
            hitchhiker_list_path.append(os.path.abspath(track))
        super().__init__(hitchhiker_list_path)

# BEISPIEL
#wecker = WeckerRadio()
#wecker.play_media()
#time.sleep(20)
#wecker.stop_media()

hitchhiker = HitchhikersGuide(1)
hitchhiker.play_media()
time.sleep(40)
hitchhiker.stop_media()
