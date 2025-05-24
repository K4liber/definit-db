from definit_db.data.track.track import Track
from definit_db.data.track.track import get_track_list


def test_get_track_list() -> None:
    track_to_length = {Track.DATA_STRUCTURES: 70, Track.ALGORITHMS: 14}

    for track, expected_length in track_to_length.items():
        track_list = get_track_list(track=track)
        assert len(track_list) == expected_length
