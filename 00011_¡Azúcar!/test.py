
  def test_endulzar_menu_le_agrega_azúcar_al_postre(self):
    menu = {"platoPrincipal": "bife de lomo", "ensalada": ["papa", "zanahoria", "arvejas"], "postre": { "ingredientes": ["queso crema", "frambuesas"], "tiempoDeCoccion": 80 }}
    endulzar_menu(menu)
    
    self.assertEqual(len(menu["postre"]["ingredientes"]), 3)
    self.assertEqual(menu["postre"]["ingredientes"][-1], "azúcar")