
  def test_sweeten_menu_add_sugar_to_dessert_if_sugar_not_present(self):
    menu = {"main_dish": "bife de lomo", "salad": ["papa", "zanahoria", "arvejas"], "dessert": { "ingredients": ["cream cheese", "raspberries"], "cook_time": 80 }}
    sweeten_menu(menu)
    
    self.assertEqual(len(menu["dessert"]["ingredients"]), 3)
    self.assertTrue(menu["dessert"]["ingredients"][-1] == "sugar")

  def test_sweeten_menu_add_sugar_to_dessert_if_sugar_present(self):
    menu = {"main_dish": "milanesas", "salad": ["lechuga", "cebolla"], "dessert": { "ingredients": ["dulce de leche", "vanilla", "sugar"], "cook_time": 60 }}
    sweeten_menu(menu)
    
    self.assertEqual(len(menu["dessert"]["ingredients"]), 4)
    self.assertTrue(menu["dessert"]["ingredients"][-1] == "sugar")
