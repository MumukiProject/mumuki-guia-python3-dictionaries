
  def test_temperaturaDePlaneta_funciona_para_Mercurio(self):
    self.assertEqual(temperaturaDePlaneta(mercurio), "Mercurio tiene una temperatura promedio de 67 grados")

  def test_temperaturaDePlaneta_funciona_para_Saturno(self):
    self.assertEqual(temperaturaDePlaneta(saturno), "Saturno tiene una temperatura promedio de -139 grados")

  def test_temperaturaDePlaneta_funciona_para_Venus(self):
    self.assertEqual(temperaturaDePlaneta(venus), "Venus tiene una temperatura promedio de 462 grados")

  def test_temperaturaDePlaneta_funciona_para_Marte(self):
    self.assertEqual(temperaturaDePlaneta(marte), "Marte tiene una temperatura promedio de -63 grados")

  def test_temperaturaDePlaneta_funciona_para_cualquier_planeta(self):
    self.assertEqual(temperaturaDePlaneta({nombre:"cualquier planeta", temperaturaPromedio:999}), "cualquier planeta tiene una temperatura promedio de 999 grados")