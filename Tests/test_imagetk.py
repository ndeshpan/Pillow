from helper import unittest, PillowTestCase, tearDownModule, lena

try:
    from Tkinter import Tk
    from PIL import ImageTk
    dir(ImageTk)
except (OSError, ImportError) as v:
    # Will be skipped in setUp
    pass


class TestImageTk(PillowTestCase):

    def setUp(self):
        try:
            from Tkinter import Tk
            from PIL import ImageTk
        except (OSError, ImportError) as v:
            self.skipTest(v)

    def test_dir(self):
        dir(ImageTk)

    def test_bitmapimage_from_pil_image(self):
        # Arrange
        im = lena("1")
        window = Tk()
        w, h = im.size

        # Act
        bitmap_image = ImageTk.BitmapImage(image=im)

        # Assert
        self.assertEqual(h, bitmap_image.height())
        self.assertEqual(w, bitmap_image.width())


if __name__ == '__main__':
    unittest.main()

# End of file
