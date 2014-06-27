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

        self.window = Tk()


    def test_dir(self):
        dir(ImageTk)

    def test_bitmap_image_from_pil_image(self):
        # Arrange
        im = lena("1")
        w, h = im.size

        # Act
        bitmap_image = ImageTk.BitmapImage(image=im)

        # Assert
        self.assertEqual(h, bitmap_image.height())
        self.assertEqual(w, bitmap_image.width())

    def test_photo_image_from_pil_image(self):
        # Arrange
        im = lena()
        w, h = im.size

        # Act
        photo_image = ImageTk.PhotoImage(image=im)

        # Assert
        self.assertEqual(h, photo_image.height())
        self.assertEqual(w, photo_image.width())


if __name__ == '__main__':
    unittest.main()

# End of file
