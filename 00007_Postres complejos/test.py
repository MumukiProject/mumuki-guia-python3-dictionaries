
  flan_casero = { "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tiempo_de_coccion": 50 }
  cheesecake = { "ingredientes": ["queso crema", "frambuesas"], "tiempo_de_coccion": 80 }
  lemon_pie = { "ingredientes": ["jugo de limón", "almidón de maíz", "leche", "huevos"], "tiempo_de_coccion": 65 }

  def test_el_flan_casero_es_mas_dificil_de_cocinar_que_el_cheesecake(self):
    self.assertEqual(mas_dificil_de_cocinar(flan_casero, cheesecake), flan_casero)
  
  def test_el_lemon_pie_es_mas_dificil_de_cocinar_que_el_cheesecake(self):
    self.assertEqual(mas_dificil_de_cocinar(cheesecake, lemon_pie), lemon_pie)
  
  def test_si_dos_postres_son_igual_de_dificiles_de_cocinar_devuelve_cualquiera_de_los_dos(self):
    mas_dificil = mas_dificil_de_cocinar(flan_casero, lemon_pie)
    self.assertTrue(mas_dificil == flan_casero or mas_dificil == lemon_pie)