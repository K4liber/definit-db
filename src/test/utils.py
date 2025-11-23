import importlib
import pkgutil
from collections import deque

import definit_db
from definit_db.definition.definition import Definition


def get_all_definitions() -> set[Definition]:
    """Collect and return Definition subclasses recursively."""
    for _, name, _ in pkgutil.walk_packages(definit_db.__path__, definit_db.__name__ + "."):
        importlib.import_module(name)

    all_definitions: set[Definition] = set()
    q = deque([Definition])

    while q:
        cls = q.popleft()
        for definition_class in cls.__subclasses__():
            # search for all instances of the definition class
            definition_class_module_path = definition_class.__module__
            definition_class_module = __import__(definition_class_module_path, fromlist=[""])
            definitions = {
                definition_class_module.__dict__[name]
                for name in dir(definition_class_module)
                if isinstance(definition_class_module.__dict__[name], Definition)
                and definition_class_module.__dict__[name].__module__ == definition_class_module_path
            }
            assert len(definitions) == 1, (
                f"Expected exactly one instance of {definition_class.__name__}, found {len(definitions)}, "
                f"module: {definition_class_module_path}."
            )
            definition = definitions.pop()

            if definition not in all_definitions:
                all_definitions.add(definition)
                q.append(definition_class)

    return all_definitions
