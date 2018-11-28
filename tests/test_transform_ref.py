import unittest
from coeus_unity.transform import TransformRef


class TransformRefTestCase(unittest.TestCase):
    def test_calculate_path(self):
        transform_a = TransformRef("Some/Path")
        transform_b = TransformRef("Other")
        transform_b.add_child_ref(transform_a)

        assert transform_a.get_rendered_transform_path() == "Other/Some/Path"

    def test_calculate_path_relative(self):
        transform_a = TransformRef("Some/Path")
        transform_b = TransformRef("Other")
        transform_b.add_child_ref(transform_a)

        assert transform_a.get_rendered_transform_path_relative(transform_b) == "Some/Path"