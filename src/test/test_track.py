from definit_db.data.track.track import Track
from definit_db.data.track.track import get_track_list


def test_get_track_list() -> None:
    data_structure_track = get_track_list(track=Track.DATA_STRUCTURES)
    assert len(data_structure_track) == 62
