from definit_db.data.track import get_track_list
from definit_db.data.track.track import Track
from definit_db.definition.definition_key import DefinitionKey
from test.utils import get_all_definitions


def test_get_track_list() -> None:
    track_to_length = {Track.DATA_STRUCTURES: 73, Track.ALGORITHMS: 35}
    defintions_in_tracks: set[DefinitionKey] = set()

    for track, expected_length in track_to_length.items():
        track_list = get_track_list(track=track)
        assert len(track_list) == expected_length
        defintions_in_tracks.update({item for item in track_list})

    all_definition_keys = {definition.key for definition in get_all_definitions()}
    definitions_diff = all_definition_keys - defintions_in_tracks
    assert not definitions_diff, (
        f"The following definitions are missing in the tracks: "
        f"{', '.join(definition_key.name for definition_key in definitions_diff)}"
    )
