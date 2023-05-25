import unittest
from ..svg2canvas.svg2canvasUtils.PyTkConverter import PyTkConverter

class PyTkConverterTestCase(unittest.TestCase):
    def test_empty_file(self):
        # Test class1's method1
        converter = PyTkConverter()
        result = converter.convert("tests/TestSVG/empty.svg")
        expected = open("tests/TestEmptyPythonTkinter/TestEmptyPythonTkinter.txt", "r")
        self.assertEqual(result, expected.read())

if __name__ == '__main__':
    unittest.main()