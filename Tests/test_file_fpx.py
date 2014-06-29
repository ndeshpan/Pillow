from helper import unittest, PillowTestCase, tearDownModule

from PIL import Image


class TestFileFpx(PillowTestCase):

    def test_fpx_grayscale(self):
        # Arrange
        filename = "Tests/images/input_grayscale.fpx"

        # Act
        im = Image.open(filename)
        im.load()

        # Assert
        self.assertEqual(im.size, (70, 46))
        self.assertEqual(im.mode, "L")

    def test_fpx_jpeg(self):
        # Arrange
        filename = "Tests/images/input_jpeg.fpx"

        # Act
        im = Image.open(filename)
        im.load()

        # Assert
        self.assertEqual(im.size, (70, 46))
        self.assertEqual(im.mode, "RGB")


if __name__ == '__main__':
    unittest.main()

# End of file
