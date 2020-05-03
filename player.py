import vlc
import time
import os


class WeckerPlayer:
    def __init__(self, playlist, tracklist):
        self.Playlist = playlist
        self.Tracklist = tracklist
        self.Instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
        self.MediaList = self.Instance.media_list_new()

        for track in self.Playlist:
            self.MediaList.add_media(self.Instance.media_new(track))

        self.player = self.Instance.media_list_player_new()
        self.player.set_media_list(self.MediaList)
        self.player.set_playback_mode(vlc.PlaybackMode.loop)

    def get_current_track_audiobook(self):
        current_track_mrl = self.player.get_media_player().get_media().get_mrl()
        current_track_mrl = current_track_mrl.replace("%20", " ")
        current_track_mrl = current_track_mrl.replace("%C3%A4", "ä")
        current_track_mrl = current_track_mrl.replace("file://", "")
        current_track = self.Tracklist.get(current_track_mrl)
        return current_track

    def get_current_track_radio(self):
        current_radio_mrl = self.player.get_media_player().get_media().get_mrl()
        current_radio = self.Tracklist.get(current_radio_mrl)
        return current_radio
        

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
        super().__init__(url_list, radiosender)


class KanguruChroniken(WeckerPlayer):
    def __init__(self, cd_number):
        cds = {
            '1': "/home/pi/Audiobooks/Die Känguru Chroniken/Marc-Uwe Kling- Die Känguru-Chroniken. CD 1",
            '2': "/home/pi/Audiobooks/Die Känguru Chroniken/Marc-Uwe Kling- Die Känguru-Chroniken. CD 2",
            '3': "/home/pi/Audiobooks/Die Känguru Chroniken/Marc-Uwe Kling- Die Känguru-Chroniken. CD 3",
            '4': "/home/pi/Audiobooks/Die Känguru Chroniken/Marc-Uwe Kling- Die Känguru-Chroniken. CD 4"
            }
        d = cds.get(str(cd_number))
        kanguru_paths = []
        for path in os.listdir(d):
            full_path = os.path.join(d, path)
            if os.path.isfile(full_path):
                kanguru_paths.append(full_path)

        kanguru_tracks = {}
        counter = 0
        kanguru_paths.sort()
        tracks = os.listdir(d)
        tracks.sort()
        for x in tracks:
            kanguru_tracks[kanguru_paths[counter]] = x
            counter += 1

        super().__init__(kanguru_paths, kanguru_tracks)


class KanguruManifest(WeckerPlayer):
    def __init__(self, cd_number):
        cds = {
            '1': "/home/pi/Audiobooks/Das Känguru Manifest/Marc-Uwe Kling- Das Känguru-Manifest. CD 1",
            '2': "/home/pi/Audiobooks/Das Känguru Manifest/Marc-Uwe Kling- Das Känguru-Manifest. CD 2",
            '3': "/home/pi/Audiobooks/Das Känguru Manifest/Marc-Uwe Kling- Das Känguru-Manifest. CD 3",
            '4': "/home/pi/Audiobooks/Das Känguru Manifest/Marc-Uwe Kling- Das Känguru-Manifest. CD 4"
            }
        d = cds.get(str(cd_number))
        kanguru_paths = []
        for path in os.listdir(d):
            full_path = os.path.join(d, path)
            if os.path.isfile(full_path):
                kanguru_paths.append(full_path)

        kanguru_tracks = {}
        counter = 0
        kanguru_paths.sort()
        tracks = os.listdir(d)
        tracks.sort()
        for x in tracks:
            kanguru_tracks[kanguru_paths[counter]] = x
            counter += 1

        super().__init__(kanguru_paths, kanguru_tracks)


class KanguruOffenbarung(WeckerPlayer):
    def __init__(self, cd_number):
        cds = {
            '1': "/home/pi/Audiobooks/Die Känguru Offenbarung/Die Känguru-Offenbarung- Live Und Ungekürzt [Disc 1]",
            '2': "/home/pi/Audiobooks/Die Känguru Offenbarung/Die Känguru-Offenbarung- Live Und Ungekürzt [Disc 2]",
            '3': "/home/pi/Audiobooks/Die Känguru Offenbarung/Die Känguru-Offenbarung- Live Und Ungekürzt [Disc 3]",
            '4': "/home/pi/Audiobooks/Die Känguru Offenbarung/Die Känguru-Offenbarung- Live Und Ungekürzt [Disc 4]",
            '5': "/home/pi/Audiobooks/Die Känguru Offenbarung/Die Känguru-Offenbarung- Live Und Ungekürzt [Disc 5]",
            '6': "/home/pi/Audiobooks/Die Känguru Offenbarung/Die Känguru-Offenbarung- Live Und Ungekürzt [Disc 6]"
        }
        d = cds.get(str(cd_number))
        kanguru_paths = []
        for path in os.listdir(d):
            full_path = os.path.join(d, path)
            if os.path.isfile(full_path):
                kanguru_paths.append(full_path)

        kanguru_tracks = {}
        counter = 0
        kanguru_paths.sort()
        tracks = os.listdir(d)
        tracks.sort()
        for x in tracks:
            kanguru_tracks[kanguru_paths[counter]] = x
            counter += 1

        super().__init__(kanguru_paths, kanguru_tracks)


class KanguruApokryphen(WeckerPlayer):
    def __init__(self, cd_number):
        cds = {
            '1': "/home/pi/Audiobooks/Die Känguru Apokryphen/CD 1",
            '2': "/home/pi/Audiobooks/Die Känguru Apokryphen/CD 2",
            '3': "/home/pi/Audiobooks/Die Känguru Apokryphen/CD 3",
            '4': "/home/pi/Audiobooks/Die Känguru Apokryphen/CD 4"
        }
        d = cds.get(str(cd_number))
        kanguru_paths = []
        for path in os.listdir(d):
            full_path = os.path.join(d, path)
            if os.path.isfile(full_path):
                kanguru_paths.append(full_path)

        kanguru_tracks = {}
        counter = 0
        kanguru_paths.sort()
        tracks = os.listdir(d)
        tracks.sort()
        for x in tracks:
            kanguru_tracks[kanguru_paths[counter]] = x
            counter += 1

        super().__init__(kanguru_paths, kanguru_tracks)


class HitchhikersGuide(WeckerPlayer):
    def __init__(self, cd_number):
        cds = {
            '1': "/home/pi/Audiobooks/The Hitchhikers Guide to the Galaxy/The Hitchhiker's Guide To The Galaxy [Disc 1]",
            '2': "/home/pi/Audiobooks/The Hitchhikers Guide to the Galaxy/The Hitchhiker's Guide To The Galaxy [Disc 2]",
            '3': "/home/pi/Audiobooks/The Hitchhikers Guide to the Galaxy/The Hitchhiker's Guide To The Galaxy [Disc 3]",
            '4': "/home/pi/Audiobooks/The Hitchhikers Guide to the Galaxy/The Hitchhiker's Guide To The Galaxy [Disc 4]"
        }
        d = cds.get(str(cd_number))
        hitchhiker_paths = []
        for path in os.listdir(d):
            full_path = os.path.join(d, path)
            if os.path.isfile(full_path):
                hitchhiker_paths.append(full_path)

        hitchhiker_tracks = {}
        counter = 0
        hitchhiker_paths.sort()
        tracks = os.listdir(d)
        tracks.sort()
        for x in tracks:
            hitchhiker_tracks[hitchhiker_paths[counter]] = x
            counter += 1

        super().__init__(hitchhiker_paths, hitchhiker_tracks)


# BEISPIEL | TEST
'''
wecker = WeckerRadio()
wecker.play_media()
track = wecker.get_current_track()
print(track)
time.sleep(10)
wecker.stop_media()
'''
'''
kanguru1 = KanguruChroniken(1)
kanguru1.play_media()
time.sleep(20)
kanguru1.next_media()
time.sleep(20)
kanguru1.stop_media()
'''
kanguru2 = KanguruManifest(1)
kanguru2.play_media()
time.sleep(5)
print(kanguru2.get_current_track())
time.sleep(5)
kanguru2.next_media()
print(kanguru2.get_current_track())
time.sleep(5)
print(kanguru2.get_current_track())
kanguru2.stop_media()

'''
kanguru3 = KanguruOffenbarung(1)
kanguru3.play_media()
time.sleep(10)
kanguru3.next_media()
time.sleep(10)
kanguru3.stop_media()

kanguru4 = KanguruApokryphen(1)
kanguru4.play_media()
time.sleep(10)
kanguru4.next_media()
time.sleep(10)
kanguru4.stop_media()

hitchhiker = HitchhikersGuide(1)
hitchhiker.play_media()
time.sleep(10)
hitchhiker.next_media()
time.sleep(10)
hitchhiker.stop_media()
'''
