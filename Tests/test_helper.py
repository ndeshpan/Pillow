from helper import unittest, PillowTestCase, lena


class TestImage(PillowTestCase):

    def test_lena_sanity(self):
        # Make sure lena() returns the same thing

        # Arrange
        im1 = lena()
        im2 = lena()

        # Assert
        self.assert_image_equal(im1, im2)

    def test_lena_changed(self):
        # Make sure lena() always returns the same thing,
        # no matter if you change the returned one

        # Arrange
        im0 = lena()
        im1 = lena()

        # Act
        # Resize one image
        im1 = im1.resize((10, 10))
        self.assertEqual(im1.size, (10, 10))
        im2 = lena()

        # Assert
        self.assert_image_equal(im0, im2)

if __name__ == '__main__':
    unittest.main()

# End of file
