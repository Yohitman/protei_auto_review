import pytest
from geopy.geocoders import Nominatim


@pytest.fixture(scope="function")
def get_conn():
    geolocator = Nominatim(user_agent="test_api_geopy_protei_konstantinov")
    yield geolocator
