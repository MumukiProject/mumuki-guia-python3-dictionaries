
  
  flanCasero = { "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tiempoDeCoccion": 50 }
  cheesecake = { "ingredientes": ["queso crema", "frambuesas"], "tiempoDeCoccion": 80 }
  lemonPie = { "ingredientes": ["jugo de limón", "almidón de maíz", "leche", "huevos"], "tiempoDeCoccion": 65 }

  def test_El_flan_casero_es_más_difícil_de_cocinar_que_el_cheesecake(self):
    self.assertEqual(masDificilDeCocinar(flanCasero, cheesecake), flanCasero)
  
  def test_El_lemonPie_es_más_difícil_de_cocinar_que_el_cheesecake(self):
    self.assertEqual(masDificilDeCocinar(cheesecake, lemonPie), lemonPie)
  
  def test_Si_dos_postres_son_igual_de_difíciles_de_cocinar_devuelve_cualquiera_de_los_dos(self):
    masDificil = masDificilDeCocinar(flanCasero, lemonPie)
    self.assertTrue(masDificil == flanCasero or masDificil == lemonPie)