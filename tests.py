import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

class TestFunction(unittest.TestCase):
    def test_get_files_info_None(self):
        result = get_files_info("calculator")
        test_result = "- tests.py: file_size=1330 bytes, is_dir=False\n- pkg: file_size=4096 bytes, is_dir=True\n- main.py: file_size=575 bytes, is_dir=False\n- lorem.txt: file_size=271026 bytes, is_dir=False"
        self.assertEqual(result, test_result)

    def test_get_files_info_dotstring(self):
        result = get_files_info("calculator", ".")
        test_result = "- tests.py: file_size=1330 bytes, is_dir=False\n- pkg: file_size=4096 bytes, is_dir=True\n- main.py: file_size=575 bytes, is_dir=False\n- lorem.txt: file_size=271026 bytes, is_dir=False"
        self.assertEqual(result, test_result)

    def test_get_files_info_empty_string(self):
        result = get_files_info("calculator", "")
        test_result = "- tests.py: file_size=1330 bytes, is_dir=False\n- pkg: file_size=4096 bytes, is_dir=True\n- main.py: file_size=575 bytes, is_dir=False\n- lorem.txt: file_size=271026 bytes, is_dir=False"
        self.assertEqual(result, test_result)

    def test_get_files_info_empty_string_two(self):
        result = get_files_info("calculator", " ")
        test_result = 'Error: " " is not a directory'
        self.assertEqual(result, test_result)

    def test_get_files_info_subdirectory(self):
        result = get_files_info("calculator", "pkg")
        test_result = "- render.py: file_size=766 bytes, is_dir=False\n- calculator.py: file_size=1737 bytes, is_dir=False\n- __pycache__: file_size=4096 bytes, is_dir=True"
        self.assertEqual(result, test_result)

    def test_get_files_info_outside_directory(self):
        result = get_files_info("calculator", "/bin")
        test_result = 'Error: Cannot list "/bin" as it is outside the permitted working directory'
        self.assertEqual(result, test_result)

    def test_get_files_info_outside_directory_two(self):
        result = get_files_info("calculator", "../")
        test_result = 'Error: Cannot list "../" as it is outside the permitted working directory'
        self.assertEqual(result, test_result)

    # def test_get_file_content_file(self):
    #     result = get_file_content(("calculator", "main.py"))

if __name__ == "__main__":
    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
    # print(get_file_content("calculator", "loerem.txt"))
    unittest.main()