
  def test_a_file_created_in_2012_no_is_not_from_past_millennium(self):
    file = {"path":"", "creation":"2012/01/01"}
    self.assertFalse(is_from_past_millennium(file))
  
  def test_a_file_created_in_2000_no_is_not_from_past_millennium(self):
    file = {"path":"", "creation":"2000/01/01"}
    self.assertFalse(is_from_past_millennium(file))
  
  def test_a_file_created_in_1999_is_from_past_millennium(self):
    file = {"path":"", "creation":"1994/09/23"}
    self.assertTrue(is_from_past_millennium(file))
  
  def test_a_file_created_in_1994_is_from_past_millennium(self):
    file = {"path":"", "creation":"1994/09/23"}
    self.assertTrue(is_from_past_millennium(file))