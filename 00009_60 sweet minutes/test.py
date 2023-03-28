
  def test_dessert_of_one_hour_and_a_half_is_not_fast(self):
    postres_rapidos = [ { "ingredients": ["galletitas", "dulceDeLeche", "crema"], "cook_time": 20 }, { "ingredients": ["huevos", "leche", "azúcar", "vainilla"], "cook_time": 50 } ]
    postre_de_leche = {"ingredients":["leche"], "cook_time":90}
    add_fast_dessert(postres_rapidos, postre_de_leche)
    self.assertEqual(len(postres_rapidos), 2)

  def test_dessert_of_a_half_hour_is_fast(self):
    postres_rapidos = [ { "ingredients": ["galletitas", "dulceDeLeche", "crema"], "cook_time": 20 }, { "ingredients": ["huevos", "leche", "azúcar", "vainilla"], "cook_time": 50 } ]
    postre_de_leche = {"ingredients":["leche"], "cook_time":30}
    add_fast_dessert(postres_rapidos, postre_de_leche)
    self.assertEqual(len(postres_rapidos), 3)
    self.assertEqual(postres_rapidos[-1], postre_de_leche)

  def test_dessert_of_one_hour_is_fast(self):
    postres_rapidos = [ { "ingredients": ["galletitas", "dulceDeLeche", "crema"], "cook_time": 20 }, { "ingredients": ["huevos", "leche", "azúcar", "vainilla"], "cook_time": 50 } ]
    postre_de_leche = {"ingredients":["leche"], "cook_time": 60}
    add_fast_dessert(postres_rapidos, postre_de_leche)
    self.assertEqual(len(postres_rapidos), 3)
    self.assertEqual(postres_rapidos[-1], postre_de_leche)