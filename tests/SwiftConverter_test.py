import unittest
from svg2canvas.svg2canvasUtils.SwiftConverter import SwiftConverter

class PyTkConverterTestCase(unittest.TestCase):
    def test_empty_file(self):
        # Test class1's method1
        converter = SwiftConverter()
        result = converter.convert("tests/TestSVG/empty.svg")
        expected = open("tests/TestSwiftUIKit/TestEmptySwift.txt", "r")
        self.assertEqual(result, expected.read())
        expected.close()

if __name__ == '__main__':
    unittest.main()