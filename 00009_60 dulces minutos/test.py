
  def test_Un postre de una hora y media no es rápido(self):
    postreDeLeche = {"ingredientes":["leche"], "tiempoDeCoccion":90}
    self.assertEqual(len(postresRapidos), 2)
  
  def test_Un postre de media hora es rápido(self):
    postreDeLeche = {"ingredientes":["leche"], "tiempoDeCoccion":30}
    agregarAPostresRapidos(postreDeLeche)
    self.assertEqual(len(postresRapidos), 3)
    self.assertEqual(postresRapidos[-1], postreDeLeche)