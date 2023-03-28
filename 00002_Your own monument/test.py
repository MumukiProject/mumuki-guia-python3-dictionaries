
  def test_azadi_tower_is_called_Torre_Azadi(self):
    self.assertEqual(azadi_tower["name"].lower(), "azadi tower")

  def test_azadi_tower_is_from_Teheran_Iran(self):
    self.assertEqual(azadi_tower["location"], "Tehran, Iran")

  def test_azadi_tower_has_year_of_construction(self):
    self.assertEqual(azadi_tower["year_of_construction"], 1971)

  def test_national_flag_memorial_is_called_Monumento_Nacional_a_la_Bandera(self):
    self.assertEqual(national_flag_memorial["name"].lower(), "national flag memorial")

  def test_national_flag_memorial_is_from_Rosario_Argentina(self):
    self.assertEqual(national_flag_memorial["location"], "Rosario, Argentina")

  def test_national_flag_memorial_has_year_of_construction(self):
self.assertEqual(national_flag_memorial["year_of_construction"], 1957)

