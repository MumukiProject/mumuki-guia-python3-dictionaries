  
  def __init__(self):
    self.postres_rapidos = [ { "ingredientes": ["galletitas", "dulceDeLeche", "crema"], "tiempo_de_coccion": 20 }, { "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tiempo_de_coccion": 50 } ]

  def test_un_postre_de_una_hora_y_media_no_es_rapido(self):
    postre_de_leche = {"ingredientes":["leche"], "tiempo_de_coccion":90}
    self.assertEqual(len(postres_rapidos), 2)
  
  def test_un_postre_de_media_hora_es_rapido(self):
    postre_de_leche = {"ingredientes":["leche"], "tiempo_de_coccion":30}
    agregar_a_postres_rapidos(postre_de_leche)
    self.assertEqual(len(postres_rapidos), 3)
    self.assertEqual(postres_rapidos[-1], postre_de_leche)