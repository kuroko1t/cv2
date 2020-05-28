from setuptools import setup, find_packages
from setuptools.dist import Distribution

class BinaryDistribution(Distribution):
    def has_ext_modules(foo):
        return True

setup(
    name='opencv-python',
    version='4.3.0',
    packages=['cv2'],
    include_package_data=True,
    distclass=BinaryDistribution,
)
