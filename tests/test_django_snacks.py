
import pytest
from django_snacks.django_snacks import django_snacks 


# Demo Tests

@pytest.mark.skip
def test_start():
    actual = django_snacks()
    expected = "Starter test"
    assert actual == expected

@pytest.mark.skip
def test_fixture_01(fixture_01):
    actual = django_snacks(fixture_01)
    expected = "Starter fixture"
    assert actual == expected


# Demo Fixture
        
@pytest.fixture 
def fixture_01():
    yield "Starter fixture"

