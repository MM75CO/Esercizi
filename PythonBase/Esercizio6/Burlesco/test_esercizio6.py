# To run test suite install pytest and pytest-cov
# >pip install pytest
# >pip install pytest-cov
# and run 
# >py.test
# to check test coverage
# >pytest --cov

from esercizio6 import Country, Continent

def test_country():
    canada = Country('Canada', 34482779, 9984670)
    assert canada.name == 'Canada'
    assert canada.population == 34482779
    assert canada.area == 9984670
  
def test_country_is_larger():
    canada = Country('Canada', 34482779, 9984670)
    usa = Country('United States of America', 313914040, 9826675)
    assert canada.is_larger(usa) == True
    assert usa.is_larger(canada) == False

def test_country_pop_density():
    canada = Country('Canada', 34482779, 9984670)
    assert canada.population_density() == 3.4535722262227995

def test_country_str():
    usa = Country('United States of America', 313914040, 9826675)
    assert str(usa) == "United States of America has a population of 313914040 and is 9826675 square km."

def test_country_repr():
    canada = Country('Canada', 34482779, 9984670)
    assert repr(canada) == "Country('Canada', 34482779, 9984670)"
    assert repr([canada]) == "[Country('Canada', 34482779, 9984670)]"

def create_north_america():
    canada = Country('Canada', 34482779, 9984670)
    usa = Country('United States of America', 313914040,9826675)
    mexico = Country('Mexico', 112336538, 1943950)
    countries = [canada, usa, mexico]
    return Continent('North America', countries)

def test_continent():
    north_america = create_north_america()
    assert north_america.name == 'North America'

def test_continent_total_population():
    north_america = create_north_america()
    assert north_america.total_population() == 460733357

def test_contintent_str():
    north_america = create_north_america()
    assert str(north_america) == "North America\nCanada has a population of 34482779 and is 9984670 square km.\nUnited States of America has a population of 313914040 and is 9826675 square km.\nMexico has a population of 112336538 and is 1943950 square km."