
  def test_torreAzadi_se_llama_Torre_Azadi(self):
    self.assertEqual(torreAzadi["nombre"].lower(), "torre azadi")

  def test_torreAzadi_es_de_Teherán_Irán(self):
    self.assertEqual(torreAzadi["locacion"], "Teherán, Irán")

  def test_torreAzadi_tiene_su_año_de_construcción(self):
    self.assertEqual(torreAzadi["anioDeConstruccion"], 1971)

  def test_monumentoNacionalALaBandera_se_llama_Monumento_Nacional_a_la_Bandera(self):
    self.assertEqual(monumentoNacionalALaBandera["nombre"].lower(), "monumento nacional a la bandera")

  def test_monumentoNacionalALaBandera_es_de_Rosario_Argentina(self):
    self.assertEqual(monumentoNacionalALaBandera["locacion"], "Rosario, Argentina")

  def test_monumentoNacionalALaBandera_tiene_su_año_de_construcción(self):
    self.assertEqual(monumentoNacionalALaBandera["anioDeConstruccion"], 1957)