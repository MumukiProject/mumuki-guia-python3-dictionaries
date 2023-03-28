
  def test_flan_is_most_difficult_to_cook_than_cheesecake(self):
    self.assertEqual(most_difficult_to_cook(flan, cheesecake), flan, "most_difficult_to_cook(flan, cheesecake) should return flan")

  def test_flan_is_most_difficult_to_cook_than_cheesecake_with_flipped_arguments(self):
    self.assertEqual(most_difficult_to_cook(cheesecake, flan), flan, "most_difficult_to_cook(cheesecake, flan) should return flan")

  def test_lemon_pie_is_most_difficult_to_cook_than_cheesecake(self):
    self.assertEqual(most_difficult_to_cook(cheesecake, lemon_pie), lemon_pie, "most_difficult_to_cook(cheesecake, lemon_pie) should return lemon_pie")

  def test_lemon_pie_is_most_difficult_to_cook_than_cheesecake_with_flipped_arguments(self):
    self.assertEqual(most_difficult_to_cook(lemon_pie, cheesecake), lemon_pie, "most_difficult_to_cook(lemon_pie, cheesecake) should return lemon_pie")

  def test_cheesecake_extra_dulce_is_most_difficult_to_cook_than_cheesecake(self):
    self.assertEqual(most_difficult_to_cook(cheesecake, cheesecake_extra_dulce), cheesecake_extra_dulce, "most_difficult_to_cook(cheesecake, cheesecake_extra_dulce) should return cheesecake_extra_dulce (because it has one ingredient more than cheesecake)")

  def test_cheesecake_extra_dulce_is_most_difficult_to_cook_than_cheesecake_with_flipped_arguments(self):
    self.assertEqual(most_difficult_to_cook(cheesecake_extra_dulce, cheesecake), cheesecake_extra_dulce, "most_difficult_to_cook(cheesecake_extra_dulce, cheesecake) should return cheesecake_extra_dulce (because it has one ingredient more than cheesecake)")

  def test_flan_is_most_difficult_to_cook_than_cheesecake_extra_dulce(self):
    self.assertEqual(most_difficult_to_cook(flan, cheesecake_extra_dulce), flan, "most_difficult_to_cook(flan, cheesecake_extra_dulce) should return flan (because it has one ingredient more than cheesecake_extra_dulce)")

  def test_flan_is_most_difficult_to_cook_than_cheesecake_extra_dulce_with_flipped_arguments(self):
    self.assertEqual(most_difficult_to_cook(cheesecake_extra_dulce, flan), flan, "most_difficult_to_cook(cheesecake_extra_dulce, flan) should return flan (because it has one ingredient more than cheesecake_extra_dulce)")

  def test_if_two_desserts_are_equals_in_difficult_to_cook_return_anyone_of_both(self):
    more_difficult = most_difficult_to_cook(flan, lemon_pie)
    self.assertTrue(more_difficult == flan or more_difficult == lemon_pie)