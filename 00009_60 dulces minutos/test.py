
  def test_un postre_de_una_hora_y_media_no_es_rapido(self):
    postreDeLeche = {"ingredientes":["leche"], "tiempo_de_coccion":90}
    self.assertEqual(len(postres_rapidos), 2)
  
  def test_un postre_de_media_hora_es_rapido(self):
    postreDeLeche = {"ingredientes":["leche"], "tiempo_de_coccion":30}
    agregar_a_postres_rapidos(postreDeLeche)
    self.assertEqual(len(postres_rapidos), 3)
    self.assertEqual(postres_rapidos[-1], postreDeLeche)