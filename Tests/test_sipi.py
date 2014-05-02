from tester import *

from PIL import Image
import glob
import os

IMAGE_DIRS = ["aerials", "misc", "sequences", "textures"]

for dir in IMAGE_DIRS:
    if not os.path.exists(dir):
        print(dir + " doesn't exist")
        skip()


def helper_test_file(file):
    im = Image.open(file)
    assert_no_exception(lambda: im.load())


def test_sipi():
    for dir in IMAGE_DIRS:
        files = glob.glob(os.path.join(dir, "*"))
        for file in files:
            helper_test_file(file)

# End of file
