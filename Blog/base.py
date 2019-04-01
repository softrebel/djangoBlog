import os, importlib, importlib.util
from Blog.apps import BlogConfig

APP_PATH = os.path.dirname(os.path.abspath(__file__))
modelsPath = os.path.join(APP_PATH, 'Models')
viewsPath = os.path.join(APP_PATH, 'Views')


def import_file(file,entity):
    entity=entity.title()
    path = os.path.join(os.path.join(APP_PATH, entity), file)
    package = '.'.join([ BlogConfig.name, entity])
    if not os.path.isfile(path):
        return
    spec = importlib.util.spec_from_file_location(package, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    globals().update(module.__dict__)
