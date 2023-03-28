
  def test_endulzar_menu_le_agrega_azucar_al_postre_si_no_tiene(self):
    menu = {"plato_principal": "bife de lomo", "ensalada": ["papa", "zanahoria", "arvejas"], "postre": { "ingredientes": ["queso crema", "frambuesas"], "tiempo_de_coccion": 80 }}
    endulzar_menu(menu)
    
    self.assertEqual(len(menu["postre"]["ingredientes"]), 3)
    self.assertTrue(menu["postre"]["ingredientes"][-1] == "azúcar" or menu["postre"]["ingredientes"][-1] == "azucar")

  def test_endulzar_menu_le_agrega_azucar_al_postre_aun_si_tiene(self):
    menu = {"plato_principal": "milanesas", "ensalada": ["lechuga", "cebolla"], "postre": { "ingredientes": ["dulce de leche", "vainillas", "azucar"], "tiempo_de_coccion": 60 }}
    endulzar_menu(menu)
    
    self.assertEqual(len(menu["postre"]["ingredientes"]), 4)
    self.assertTrue(menu["postre"]["ingredientes"][-1] == "azúcar" or menu["postre"]["ingredientes"][-1] == "azucar")