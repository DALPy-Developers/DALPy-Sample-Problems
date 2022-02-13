import unittest
from cormen_lib.arrays import Array2D
from cormen_lib.factory_utils import make_array
from array_problems import count_prizes
from cormen_lib.test_utils import build_and_run_watched_suite, assert_array_equals, cormen_equals, \
    run_generic_test, to_cormen_string


class CountPrizesTest(unittest.TestCase):

    def test_unique_items(self):
        prizes = make_array(['d', 'b'])
        items = make_array(['a', 'b', 'c', 'd'])
        run_generic_test([prizes, items], 2, count_prizes, params_to_string=self.count_prizes_to_string)

    def test_duplicate_items(self):
        prizes = make_array(['d', 'b'])
        items = make_array(['a', 'b', 'c', 'd', 'd', 'c', 'b', 'a'])
        run_generic_test([prizes, items], 4, count_prizes, params_to_string=self.count_prizes_to_string)

    def test_case_mix_prizes(self):
        prizes = make_array(['d', 'B'])
        items = make_array(['a', 'b', 'c', 'd'])
        run_generic_test([prizes, items], 1, count_prizes, params_to_string=self.count_prizes_to_string)

    def test_case_mix_items(self):
        prizes = make_array(['a', 'C', 'b', 'A'])
        items = make_array(['c', 'b', 'A', 'a', 'B', 'a', 'c'])
        run_generic_test([prizes, items], 4, count_prizes, params_to_string=self.count_prizes_to_string)

    def test_no_prizes(self):
        prizes = make_array([])
        items = make_array(['a', 'b', 'c', 'd', 'd', 'c', 'b', 'a'])
        run_generic_test([prizes, items], 0, count_prizes, params_to_string=self.count_prizes_to_string)
        prizes = make_array(['D', 'B'])
        items = make_array(['a', 'b', 'c', 'd', 'd', 'c', 'b', 'a'])
        run_generic_test([prizes, items], 0, count_prizes, params_to_string=self.count_prizes_to_string)

    def test_no_items(self):
        prizes = make_array(['D', 'B'])
        items = make_array([])
        run_generic_test([prizes, items], 0, count_prizes, params_to_string=self.count_prizes_to_string)

    def count_prizes_to_string(self, params):
        return f'{to_cormen_string(params[0])}, {to_cormen_string(params[1])}'


if __name__ == '__main__':
    build_and_run_watched_suite([CountPrizesTest], 4)
