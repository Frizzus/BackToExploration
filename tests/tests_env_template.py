import unittest, lib.EnvTemplate as env, shutil, os

test_template_name:str = "test_template"

class TestEnvTemplate(unittest.TestCase):
    def test_key_checking_int(self):
        try:
            env.template_key_checking(2, int, test_template_name)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_key_checking_float(self):
        try:
            env.template_key_checking(2.5, float, test_template_name)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_key_checking_str(self):
        try:
            env.template_key_checking("2", str, test_template_name)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_key_checking_list(self):
        try:
            env.template_key_checking(["hello", 2, 3.14], list, test_template_name)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_key_checking_dict(self):
        try:
            env.template_key_checking({"hello": "world", "ten": 10, "pi": 3.14}, dict, test_template_name)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_key_checking_undefined(self):
        test_dict = {"key": 42}
        with self.assertRaises(KeyError): env.template_key_checking(test_dict["wrong_key"], dict)

    
    def test_key_checking_wrong_type(self):
        with self.assertRaises(TypeError): env.template_key_checking(2, str, test_template_name)
        with self.assertRaises(TypeError): env.template_key_checking(2, float, test_template_name)
        with self.assertRaises(TypeError): env.template_key_checking(2, list, test_template_name)
        with self.assertRaises(TypeError): env.template_key_checking(2, dict, test_template_name)

        with self.assertRaises(TypeError): env.template_key_checking(2.0, str, test_template_name)
        with self.assertRaises(TypeError): env.template_key_checking(2.0, int, test_template_name)
        with self.assertRaises(TypeError): env.template_key_checking(2.0, list, test_template_name)
        with self.assertRaises(TypeError): env.template_key_checking(2.0, dict, test_template_name)

        with self.assertRaises(TypeError): env.template_key_checking("2", int, test_template_name)
        with self.assertRaises(TypeError): env.template_key_checking("2", float, test_template_name)
        with self.assertRaises(TypeError): env.template_key_checking("2", list, test_template_name)
        with self.assertRaises(TypeError): env.template_key_checking("2", dict, test_template_name)

        with self.assertRaises(TypeError): env.template_key_checking(["hello", 2, 3.14], int, test_template_name)
        with self.assertRaises(TypeError): env.template_key_checking(["hello", 2, 3.14], float, test_template_name)
        with self.assertRaises(TypeError): env.template_key_checking(["hello", 2, 3.14], str, test_template_name)
        with self.assertRaises(TypeError): env.template_key_checking(["hello", 2, 3.14], dict, test_template_name)

        with self.assertRaises(TypeError): env.template_key_checking({"hello": "world", "ten": 10, "pi": 3.14}, int, test_template_name)
        with self.assertRaises(TypeError): env.template_key_checking({"hello": "world", "ten": 10, "pi": 3.14}, float, test_template_name)
        with self.assertRaises(TypeError): env.template_key_checking({"hello": "world", "ten": 10, "pi": 3.14}, str, test_template_name)
        with self.assertRaises(TypeError): env.template_key_checking({"hello": "world", "ten": 10, "pi": 3.14}, list, test_template_name)

    def test_create_2_biome(self):
        shutil.rmtree("tests/biome")
        os.mkdir("tests/biome")
        try:
            template = env.EnvTemplate()
            template.set_current_template("assets/env_template/fall_env.json")
            template.create_biome("tests/biome/")
            template.set_current_template("assets/env_template/taiga_env.json")
            template.create_biome("tests/biome/")
        except FileExistsError:
            self.assertTrue(False)

        try:
            file1 = open("tests/biome/biome_1.json", "r")
            file1.close()
            file2 = open("tests/biome/biome_2.json", "r")
            file2.close()
        except OSError:
            self.assertTrue(False)
        
        self.assertTrue(True)

    def test_create_biome(self):
        shutil.rmtree("tests/biome")
        os.mkdir("tests/biome")
        template = env.EnvTemplate()
        template.set_current_template("assets/env_template/fall_env.json")
        template.create_biome("tests/biome/")
        try:
            file = open("tests/biome/biome_1.json", "r")
            file.close()
        except OSError:
            self.assertTrue(False)
        
        self.assertTrue(True)