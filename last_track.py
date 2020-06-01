import numpy as np
import pandas as pd


def get_all_last_tracks():
    data = pd.read_csv('last_track.dat', sep=" ", header=None)
    data.columns = ["audiobook", "cd_number", "track"]

    audiobook = []
    for name in data.audiobook:
        audiobook.append(name)
    cd_number = []
    for cd in data.cd_number:
        cd_number.append(cd)
    track = []
    for number in data.track:
        track.append(number)

    last_tracks = {}
    tmp_name = " "
    zeile = 0
    for name in audiobook:
        if name is not tmp_name:
            last_tracks[name] = {}
            tmp_name = name
        last_tracks[tmp_name][cd_number[zeile]] = track[zeile]
        zeile += 1
    return last_tracks


def get_last_track(audiobook, cd_number):
    last_tracks = get_all_last_tracks()
    last_track = last_tracks.get(audiobook).get(cd_number)
    return last_track

def set_last_tracks(audiobook, cd_number, track_number):
    last_tracks = get_all_last_tracks()
    last_tracks[audiobook][cd_number] = track_number

    audiobooks = []
    cd_numbers = []
    tracks = []

    for name in last_tracks:
        for cd in last_tracks.get(name):
            audiobooks.append(name)
            cd_numbers.append(cd)
            tracks.append(last_tracks.get(name).get(cd))

    np_audiobooks = np.array(audiobooks)
    np_cd_numbers = np.array(cd_numbers)
    np_tracks = np.array(tracks)

    data = np.column_stack((np_audiobooks, np_cd_numbers, np_tracks))
    np.savetxt('last_track.dat', data, delimiter=" ", fmt="%s")
