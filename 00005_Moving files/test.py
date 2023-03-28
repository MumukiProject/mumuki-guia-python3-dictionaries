def test_move_file_returns_nothing(self):
    file = { "path":"/usr/my_file.doc", "creation":"15/02/2019" }
    self.assertEqual(None, move_file(file, "/home/my_file.doc"), "Must return none because it is a procedure")
    
  def test_move_file_change_path_a_un_file_al_pasar_una_path_nueva(self):
    file = { "path":"/usr/my_file.doc", "creation":"15/02/2019" }
    move_file(file, "/home/my_file.doc")
    self.assertEqual(file["path"], "/home/my_file.doc")

  def test_move_file_keep_its_path_if_path_is_the_same(self):
    file = { "path":"/usr/my_file.doc", "creation":"15/02/2019" }
    move_file(file, "/usr/my_file.doc")
    self.assertEqual(file["path"], "/usr/my_file.doc")

  def test_move_file_does_not_update_creation_date(self):
    file = { "path":"/usr/my_file.doc", "creation":"15/02/2019" }
    move_file(file, "/home/my_file.doc")
    self.assertEqual(file["creation"], "15/02/2019")
