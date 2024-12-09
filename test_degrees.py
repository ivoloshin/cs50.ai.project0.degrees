import pytest
from degrees import *

def test_load_data():
    load_data("small")
    assert people["102"]["name"] == "Kevin Bacon"

    # Kevin Bacon was in two movies in the small dataset
    assert people["102"]["movies"] == {"104257", "112384" }

    # neighbor of Kevin Bacon in the small dataset
    neighbors = neighbors_for_person("102")
    assert neighbors == { ('104257', '102'), ('104257','129'), ('104257','193'), ('104257','197'), ('112384', '102'), ('112384', '158'), ('112384', '200'), ('112384', '641') }

def test_test():
    assert True


def test_test3():
    assert True

    


