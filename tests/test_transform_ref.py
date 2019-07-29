import unittest
from coeus_unity.transform import TransformRef


class TransformRefTestCase(unittest.TestCase):
    def test_calculate_path(self):
        menu = TransformRef("Path/To/Menu")

        button = TransformRef("Button", parent=menu)
        assert button.transform_path == "Button"
        assert button.get_relative_transform_path() == "Button"
        assert button.get_absolute_transform_path() == "Path/To/Menu/Button"

        button.set_parent(None)
        assert button.transform_path == "Path/To/Menu/Button"
        assert button.get_relative_transform_path() == "Path/To/Menu/Button"
        assert button.get_absolute_transform_path() == "Path/To/Menu/Button"
