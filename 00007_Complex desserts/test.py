
  def test_flan_is_most_difficult_to_cook_than_cheesecake(self):
    self.assertEqual(most_difficult_to_cook(flan, cheesecake), flan, "most_difficult_to_cook(flan, cheesecake) should return flan")

  def test_flan_is_most_difficult_to_cook_than_cheesecake_with_flipped_arguments(self):
    self.assertEqual(most_difficult_to_cook(cheesecake, flan), flan, "most_difficult_to_cook(cheesecake, flan) should return flan")

  def test_lemon_pie_is_most_difficult_to_cook_than_cheesecake(self):
    self.assertEqual(most_difficult_to_cook(cheesecake, lemon_pie), lemon_pie, "most_difficult_to_cook(cheesecake, lemon_pie) should return lemon_pie")

  def test_lemon_pie_is_most_difficult_to_cook_than_cheesecake_with_flipped_arguments(self):
    self.assertEqual(most_difficult_to_cook(lemon_pie, cheesecake), lemon_pie, "most_difficult_to_cook(lemon_pie, cheesecake) should return lemon_pie")

  def extra_sweet_cheesecake_is_most_difficult_to_cook_than_cheesecake(self):
    self.assertEqual(most_difficult_to_cook(cheesecake, extra_sweet_cheesecake), extra_sweet_cheesecake, "most_difficult_to_cook(cheesecake, extra_sweet_cheesecake) should return extra_sweet_cheesecake (because it has one ingredient more than cheesecake)")

  def extra_sweet_cheesecake_is_most_difficult_to_cook_than_cheesecake_with_flipped_arguments(self):
    self.assertEqual(most_difficult_to_cook(extra_sweet_cheesecake, cheesecake), extra_sweet_cheesecake, "most_difficult_to_cook(extra_sweet_cheesecake, cheesecake) should return extra_sweet_cheesecake (because it has one ingredient more than cheesecake)")

  def extra_sweet_cheesecake(self):
    self.assertEqual(most_difficult_to_cook(flan, extra_sweet_cheesecake), flan, "most_difficult_to_cook(flan, extra_sweet_cheesecake) should return flan (because it has one ingredient more than extra_sweet_cheesecake)")

  def extra_sweet_cheesecake_with_flipped_arguments(self):
    self.assertEqual(most_difficult_to_cook(extra_sweet_cheesecake, flan), flan, "most_difficult_to_cook(extra_sweet_cheesecake, flan) should return flan (because it has one ingredient more than extra_sweet_cheesecake)")

  def test_if_two_desserts_are_equals_in_difficult_to_cook_return_anyone_of_both(self):
    more_difficult = most_difficult_to_cook(flan, lemon_pie)
    self.assertTrue(more_difficult == flan or more_difficult == lemon_pie)