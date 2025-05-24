# DefinIT database

## Build and upload the package
```
(just once) python -m pip install requirements-dev.txt

(optional cleanup) rm -rf dist/ build/ src/*.egg-info/

python -m build

python -m twine upload dist/*
```
## Generate tracks
```
python -m definit_db.data.track.track
```