
  def test_planet_temperature_works_for_Mercury(self):
    self.assertEqual(planet_temperature(mercury), "Mercury has an average temperature of 67 degrees")

  def test_planet_temperature_works_for_Saturn(self):
    self.assertEqual(planet_temperature(saturn), "Saturn has an average temperature of -139 degrees")

  def test_planet_temperature_works_for_Venus(self):
    self.assertEqual(planet_temperature(venus), "Venus has an average temperature of 462 degrees")

  def test_planet_temperature_works_for_Mars(self):
    self.assertEqual(planet_temperature(mars), "Mars has an average temperature of -63 degrees")

  def test_planet_temperature_works_for_any_planet(self):
    self.assertEqual(planet_temperature({"name": "Earth", "average_temperature": 25}), "Earth has an average temperature of 25 degrees")

  def test_has_no_type_errors(self):
    try:
      planet_temperature(mars)
    except TypeError as e:
      if "can only concatenate str" in str(e): 
        self.fail("Should not throw TypeError")
