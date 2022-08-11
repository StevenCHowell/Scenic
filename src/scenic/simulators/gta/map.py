# stub to allow changing the map without having to alter gta_model.sc
import pathlib

module_path = pathlib.Path(__file__)
scenic_path = module_path.parent.parent.parent.parent.parent
mapPath = str(list(scenic_path.rglob("map.npz"))[0])


def setLocalMap(module, relpath):
    import os

    global mapPath
    base = os.path.dirname(module)
    mapPath = os.path.join(base, relpath)
