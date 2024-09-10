import pytest
from src.main import Person

@pytest.fixture
def person():
    return Person("Carlos Sainz", 30, ["Ferrari Driver"])

def test_firstname(person):
    assert person.get_forename == "Carlos"

def test_lastname(person):
    assert person.get_lastname == "Sainz"

def test_age(person):
    assert person.age == 30
    person.celebrate_birthday()
    assert person.age == 31

def test_add_occupation(person):
    person.add_occupation('Williams Driver')
    assert "Williams Driver" in person.occupation