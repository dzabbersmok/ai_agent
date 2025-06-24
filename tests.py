import unittest
from functions.get_files_info import get_files_info

class TestFunction(unittest.TestCase):
    def test_None(self):
        result = get_files_info("calculator")
        test_result = "- tests.py: file_size=1330 bytes, is_dir=False\n- pkg: file_size=4096 bytes, is_dir=True\n- main.py: file_size=575 bytes, is_dir=False"
        self.assertEqual(result, test_result)

    def test_dotstring(self):
        result = get_files_info("calculator", ".")
        test_result = "- tests.py: file_size=1330 bytes, is_dir=False\n- pkg: file_size=4096 bytes, is_dir=True\n- main.py: file_size=575 bytes, is_dir=False"
        self.assertEqual(result, test_result)

    def test_empty_string(self):
        result = get_files_info("calculator", "")
        test_result = "- tests.py: file_size=1330 bytes, is_dir=False\n- pkg: file_size=4096 bytes, is_dir=True\n- main.py: file_size=575 bytes, is_dir=False"
        self.assertEqual(result, test_result)

    def test_empty_string_two(self):
        result = get_files_info("calculator", " ")
        test_result = 'Error: " " is not a directory'
        self.assertEqual(result, test_result)

    def test_subdirectory(self):
        result = get_files_info("calculator", "pkg")
        test_result = "- render.py: file_size=766 bytes, is_dir=False\n- calculator.py: file_size=1737 bytes, is_dir=False\n- __pycache__: file_size=4096 bytes, is_dir=True"
        self.assertEqual(result, test_result)

    def test_outside_directory(self):
        result = get_files_info("calculator", "/bin")
        test_result = 'Error: Cannot list "/bin" as it is outside the permitted working directory'
        self.assertEqual(result, test_result)

    def test_outside_directory_two(self):
        result = get_files_info("calculator", "../")
        test_result = 'Error: Cannot list "../" as it is outside the permitted working directory'
        self.assertEqual(result, test_result)

if __name__ == "__main__":
    print(get_files_info("calculator", "."))
    print(get_files_info("calculator", "pkg"))
    print(get_files_info("calculator", "/bin"))
    print(get_files_info("calculator", "../"))
    unittest.main()