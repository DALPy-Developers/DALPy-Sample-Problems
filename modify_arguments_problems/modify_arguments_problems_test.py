import unittest

from dalpy.factory_utils import make_array
from dalpy.test_utils import build_and_run_watched_suite, generic_test

from modify_arguments_problems import duplicate_array, duplicate_array_incorrect

class ModifyArgumentsTest(unittest.TestCase):

    def test_proper_modify_arguments(self):
        arr = make_array([1,2,3,None,None,None])
        expected = make_array([1,2,3,1,2,3])
        # Since we have set "in_place = True" the test case will compare its parameter arr against expected.
        generic_test(arr, expected, duplicate_array, in_place=True)

    def test_accidental_modify_arguments(self):
        arr = make_array([1,2,3,None,None,None])
        expected = make_array([1,2,3,1,2,3])
        # Since we have set "in_place = True" the test case will compare its parameter arr against expected.
        # Awarning will be generated and this test will fail because duplicate_array_incorrect returns a new Array isntead of modifying its argument.
        generic_test(arr, expected, duplicate_array_incorrect, in_place=True)


if __name__ == '__main__':
    build_and_run_watched_suite(
        [ModifyArgumentsTest])
