import os
APP_PATH = os.path.dirname(os.path.abspath(__file__))
modelsPath = APP_PATH + os.sep + 'Models'
import os, importlib, importlib.util


def import_file(file):
    path = modelsPath + os.sep + file
    if not os.path.isfile(path):
        return
    spec = importlib.util.spec_from_file_location("Blog.Models", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    globals().update(module.__dict__)
