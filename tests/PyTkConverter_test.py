import unittest
from svg2canvas.svg2canvasUtils.PyTkConverter import PyTkConverter

class PyTkConverterTestCase(unittest.TestCase):
    def test_empty_file(self):
        converter = PyTkConverter()
        result = converter.convert("tests/TestSVG/empty.svg")
        expected = open("tests/TestPythonTkinter/TestEmptyPythonTkinter.txt", "r")
        self.assertEqual(result, expected.read())
        expected.close()

    def test_rectangles(self):
        converter = PyTkConverter()
        result = converter.convert("tests/TestSVG/rectangles.svg")
        expected = open("tests/TestPythonTkinter/TestRectangles.txt", "r")
        self.assertEqual(result, expected.read())
        expected.close()

if __name__ == '__main__':
    unittest.main()