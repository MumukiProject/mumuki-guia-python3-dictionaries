
  def test_sweeten_menu_add_sugar_to_dessert_if_sugar_not_present(self):
    menu = {"main_dish": "bife de lomo", "salad": ["papa", "zanahoria", "arvejas"], "postre": { "ingredients": ["cream cheese", "raspberries"], "cook_time": 80 }}
    sweeten_menu(menu)
    
    self.assertEqual(len(menu["postre"]["ingredients"]), 3)
    self.assertTrue(menu["postre"]["ingredients"][-1] == "sugar")

  def test_sweeten_menu_add_sugar_to_dessert_if_sugar_present(self):
    menu = {"main_dish": "milanesas", "salad": ["lechuga", "cebolla"], "postre": { "ingredients": ["dulce de leche", "vanilla", "sugar"], "cook_time": 60 }}
    sweeten_menu(menu)
    
    self.assertEqual(len(menu["postre"]["ingredients"]), 4)
    self.assertTrue(menu["postre"]["ingredients"][-1] == "sugar")
