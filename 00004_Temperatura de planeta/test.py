
  def test_temperatura_de_planeta_funciona_para_Mercurio(self):
    self.assertEqual(temperatura_de_planeta(mercurio), "Mercurio tiene una temperatura promedio de 67 grados")

  def test_temperatura_de_planeta_funciona_para_Saturno(self):
    self.assertEqual(temperatura_de_planeta(saturno), "Saturno tiene una temperatura promedio de -139 grados")

  def test_temperatura_de_planeta_funciona_para_Venus(self):
    self.assertEqual(temperatura_de_planeta(venus), "Venus tiene una temperatura promedio de 462 grados")

  def test_temperatura_de_planeta_funciona_para_Marte(self):
    self.assertEqual(temperatura_de_planeta(marte), "Marte tiene una temperatura promedio de -63 grados")

  def test_temperatura_de_planeta_funciona_para_cualquier_planeta(self):
    self.assertEqual(temperatura_de_planeta({"nombre":"cualquier planeta", "temperatura_promedio":999}), "cualquier planeta tiene una temperatura promedio de 999 grados")