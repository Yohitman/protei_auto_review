import pytest


class TestStraightForm:
    @pytest.mark.parametrize('address', ["175 5th Avenue NYC",])
    def test_get_coord_from_address(self, get_conn, address):
        location = get_conn.geocode('address')
        assert (round(location.latitude, 5), round(location.longitude, 5)) == (39.83919, -75.46378)


class TestReverseForm:
    @pytest.mark.parametrize('coords', [("52.509669,13.376294"),])
    def test_get_address_from_coord(self, get_conn, coords):
        location = get_conn.reverse("52.509669,13.376294")
        assert location.address == 'Potsdamer Platz, Tiergarten, Mitte, Berlin, 10785, Deutschland'
