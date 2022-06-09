import pytest


class TestStraightForm:
    @pytest.mark.parametrize('address', [
        ("Flatiron Building, 175, 5th Avenue, Flatiron District, Manhattan Community Board 5, New York County, New York, 10010, United States", 40.7411, -73.9896),
        ("Red Square, Kitay-gorod, Tverskoy District, Moscow, Central Federal District, 109012, Russia", 55.7536, 37.6214),
        ("Potsdamer Platz, Tiergarten, Mitte, Berlin, 10785, Deutschland", 52.509, 13.3756)
                                         ])
    def test_get_coord_from_address(self, get_conn, address):
        location = get_conn.geocode(address[0])
        assert (round(location.latitude, 4), round(location.longitude, 4)) == (address[1], address[2])


class TestReverseForm:
    @pytest.mark.parametrize('coords', [
        ("52.509669,13.376294", 'Potsdamer Platz, Tiergarten, Mitte, Berlin, 10785, Germany'),
        ("40.7411, -73.9896", "Flatiron Building, 175, 5th Avenue, Flatiron District, Manhattan Community Board 5, New York County, New York, 10010, United States"),
        ("55.75380, 37.62008", "Vladimir Lenin's Mausoleum, Red Square, Kitay-gorod, Tverskoy District, Moscow, Central Federal District, 109012, Russia")
                                        ])
    def test_get_address_from_coord(self, get_conn, coords):
        location = get_conn.reverse(coords[0], language="en")
        assert location.address == coords[1]
