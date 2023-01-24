
  def test_mover_archivo_no_retorna_nada(self):
    archivo = {"ruta":"/usr/miarchivo.doc", "creacion":"15/02/2019"}
    self.assertEqual(None, mover_archivo(archivo, "/home/miarchivo.doc"), "No debe retornar nada, dado que es un procedimiento")
    
  def test_mover_archivo_le_cambia_la_ruta_a_un_archivo_al_pasar_una_ruta_nueva(self):
    archivo = {"ruta":"/usr/miarchivo.doc", "creacion":"15/02/2019"}
    mover_archivo(archivo, "/home/miarchivo.doc")
    self.assertEqual(archivo["ruta"], "/home/miarchivo.doc")

  def test_mover_archivo_le_mantiene_la_ruta_a_un_archivo_si_se_pasa_la_misma(self):
    archivo = {"ruta":"/usr/miarchivo.doc", "creacion":"15/02/2019"}
    mover_archivo(archivo, "/usr/miarchivo.doc")
    self.assertEqual(archivo["ruta"], "/usr/miarchivo.doc")

  def test_mover_archivo_no_modifica_la_fecha_de_creacion_del_archivo(self):
    archivo = {"ruta":"/usr/miarchivo.doc", "creacion":"15/02/2019"}
    mover_archivo(archivo, "/home/miarchivo.doc")
    self.assertEqual(archivo["creacion"], "15/02/2019")