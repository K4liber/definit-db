from definit_db.data.track.definitions.algorithms import TrackDefinitionsAlgorithms
from definit_db.data.track.definitions.data_structures import TrackDefinitionsDataStructures
from definit_db.data.track.definitions.track_definitions_abstract import TrackDefinitionsAbstract
from definit_db.data.track.track import Track
from definit_db.definition.definition_key import DefinitionKey

_track_to_get_definition_keys: dict[Track, type[TrackDefinitionsAbstract]] = {
    Track.DATA_STRUCTURES: TrackDefinitionsDataStructures,
    Track.ALGORITHMS: TrackDefinitionsAlgorithms,
}


def get_track_list(track: Track) -> tuple[DefinitionKey, ...]:
    return _track_to_get_definition_keys[track].get_track_definition_keys()
