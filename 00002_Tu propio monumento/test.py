
  def test_torre_azadi_se_llama_Torre_Azadi(self):
    self.assertEqual(torre_azadi["nombre"].lower(), "torre azadi")

  def test_torre_azadi_es_de_Teheran_Iran(self):
    self.assertEqual(torre_azadi["locacion"], "Teherán, Irán")

  def test_torre_azadi_tiene_su_anio_de_construccion(self):
    self.assertEqual(torre_azadi["anio_de_construccion"], 1971)

  def test_monumento_nacional_a_la_bandera_se_llama_Monumento_Nacional_a_la_Bandera(self):
    self.assertEqual(monumento_nacional_a_la_bandera["nombre"].lower(), "monumento nacional a la bandera")

  def test_monumento_nacional_a_la_bandera_es_de_Rosario_Argentina(self):
    self.assertEqual(monumento_nacional_a_la_bandera["locacion"], "Rosario, Argentina")

  def test_monumento_nacional_a_la_bandera_tiene_su_anio_de_construccion(self):
    self.assertEqual(monumento_nacional_a_la_bandera["anio_de_construccion"], 1957)