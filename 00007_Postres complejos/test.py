
  def test_el_flan_casero_es_mas_dificil_de_cocinar_que_el_cheesecake_al_derecho(self):
    self.assertEqual(mas_dificil_de_cocinar(flan_casero, cheesecake), flan_casero, "mas_dificil_de_cocinar(flan_casero, cheesecake) debe devolver flan_casero")

  def test_el_flan_casero_es_mas_dificil_de_cocinar_que_el_cheesecake_al_reves(self):
    self.assertEqual(mas_dificil_de_cocinar(cheesecake, flan_casero), flan_casero, "mas_dificil_de_cocinar(cheesecake, flan_casero) debe devolver flan_casero")

  def test_el_lemon_pie_es_mas_dificil_de_cocinar_que_el_cheesecake_al_derecho(self):
    self.assertEqual(mas_dificil_de_cocinar(cheesecake, lemon_pie), lemon_pie, "mas_dificil_de_cocinar(cheesecake, lemon_pie) debe devolver lemon_pie")

  def test_el_lemon_pie_es_mas_dificil_de_cocinar_que_el_cheesecake_al_reves(self):
    self.assertEqual(mas_dificil_de_cocinar(lemon_pie, cheesecake), lemon_pie, "mas_dificil_de_cocinar(lemon_pie, cheesecake) debe devolver lemon_pie")

  def test_el_cheesecake_extra_dulce_es_mas_dificil_de_cocinar_que_el_cheesecake(self):
    self.assertEqual(mas_dificil_de_cocinar(cheesecake, cheesecake_extra_dulce), cheesecake_extra_dulce, "mas_dificil_de_cocinar(cheesecake, cheesecake_extra_dulce) debe devolver cheesecake_extra_dulce (porque tiene un ingrediente más que el cheesecake)")


  def test_el_flan_casero_es_mas_dificil_de_cocinar_que_el_cheesecake_extra_dulce(self):
    self.assertEqual(mas_dificil_de_cocinar(flan_casero, cheesecake_extra_dulce), cheesecake_extra_dulce, "mas_dificil_de_cocinar(flan_casero, cheesecake_extra_dulce) debe devolver flan_casero (porque tiene un ingrediente más que el cheesecake_extra_dulce)")

  def test_si_dos_postres_son_igual_de_dificiles_de_cocinar_devuelve_cualquiera_de_los_dos(self):
    mas_dificil = mas_dificil_de_cocinar(flan_casero, lemon_pie)
    self.assertTrue(mas_dificil == flan_casero or mas_dificil == lemon_pie)