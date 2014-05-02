from tester import *

from PIL import Image
import os
import os.path

IMAGE_DIR = "TESTIMAGES"

if not os.path.exists(IMAGE_DIR):
    skip()


def helper_test_file(file):
    im = Image.open(file)
    assert_no_exception(lambda: im.load())


def test_testimages():
    for dirpath, dirnames, filenames in os.walk(IMAGE_DIR):
        for filename in filenames:
            if filename.endswith(".TXT"):
                continue
            filename = os.path.join(dirpath, filename)
            helper_test_file(filename)

# End of file
