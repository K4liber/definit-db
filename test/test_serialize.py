from definit.db.md import DatabaseMd

from definit_db.serialize import serialize


def test_generate_and_load() -> None:
    db_path = serialize()
    assert db_path.exists()
    db = DatabaseMd(data_md_path=db_path, load_cache=True)
    index = db.get_index()
    assert len(index) == 182
