from definit_db.data.track import get_track_list
from definit_db.data.track.track import Track


def test_get_track_list() -> None:
    track_to_length = {Track.DATA_STRUCTURES: 70, Track.ALGORITHMS: 22}

    for track, expected_length in track_to_length.items():
        track_list = get_track_list(track=track)
        assert len(track_list) == expected_length
