
  def test_un_postre_de_una_hora_y_media_no_es_rapido(self):
    postre_de_leche = {"ingredientes":["leche"], "tiempo_de_coccion":90}
    self.assertEqual(len(postres_rapidos), 2)
  
