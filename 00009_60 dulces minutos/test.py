
  def test_Un postre de una hora y media no es rápido(self):
    postreDeLeche = {"ingredientes":["leche"], "tiempo_de_coccion":90}
    self.assertEqual(len(postres_rapidos), 2)
  
  def test_Un postre de media hora es rápido(self):
    postreDeLeche = {"ingredientes":["leche"], "tiempo_de_coccion":30}
    agregar_a_postres_rapidos(postreDeLeche)
    self.assertEqual(len(postres_rapidos), 3)
    self.assertEqual(postres_rapidos[-1], postreDeLeche)