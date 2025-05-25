from abc import abstractmethod

from definit_db.definition.definition_key import DefinitionKey


class TrackDefinitionsAbstract:
    @staticmethod
    @abstractmethod
    def get_track_definition_keys() -> tuple[DefinitionKey, ...]:
        """Get the track definition keys."""
        raise NotImplementedError
