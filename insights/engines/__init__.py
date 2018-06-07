from .citellus import CitellusEngine

engines = { "citellus": CitellusEngine }

def get_engine(name):
    return engines[name]

