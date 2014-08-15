from helper import unittest, PillowTestCase, lena

from PIL import Image


class TestImage(PillowTestCase):

    def test_lena_sanity(self):
        # Make sure lena() returns the same thing

        # Arrange
        im_original = Image.open("Tests/images/lena.ppm")
        im1 = lena()
        im2 = lena()

        # Assert
        self.assert_image_equal(im1, im2)
        self.assert_image_equal(im1, im_original)

    def test_lena_changed(self):
        # Make sure lena() always returns the same thing,
        # no matter if you change the returned one

        # Arrange
        im_original = Image.open("Tests/images/lena.ppm")
        im0 = lena()
        im1 = lena()

        # Act
        # Resize one image
        im1 = im1.resize((10, 10))
        self.assertEqual(im1.size, (10, 10))
        im2 = lena()

        # Assert
        self.assert_image_equal(im0, im2)
        self.assert_image_equal(im0, im_original)

    def test_lena_change_pixel(self):
        # Make sure lena() always returns the same thing,
        # no matter if you change the returned one

        # Arrange
        im_original = Image.open("Tests/images/lena.ppm")
        im0 = lena()

        # Act
        # Change a pixel in im0
        im0.load()
        im0.putpixel((20, 20), im0.getpixel((0, 0)))
        # Get a fresh lena()
        im1 = lena()

        # Assert
        self.assert_image_equal(im1, im_original)

    # def test_lena_lots(self):
        # # Test getting lots, for timing
        # for i in range(100000):
            # im = lena()

if __name__ == '__main__':
    unittest.main()

# End of file
