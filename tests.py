import unittest
from maze import Maze

class Test(unittest.TestCase):
    test_cases = [
        {
            "name": "basic",
            "maze_args": [0, 0, 12, 10, 10, 10],
            "expected_len_cols": 10,
            "expected_len_rows": 12
         },
         {
            "name": "large",
            "maze_args": [0, 0, 20, 14, 10, 10],
            "expected_len_cols": 14,
            "expected_len_rows": 20
         }
    ]

    def test_maze_create_cells(self):
        for case in self.test_cases:
            with self.subTest(case["name"]):
                m1 = Maze(*case["maze_args"])
                self.assertEqual(
                    len(m1._cells),
                    case["expected_len_cols"],
                )
                self.assertEqual(
                    len(m1._cells[0]),
                    case["expected_len_rows"],
                )

    def test_break_entrance_and_exit(self):
        for case in self.test_cases:
            with self.subTest(case["name"]):
                m1 = Maze(*case["maze_args"])
                entrance_cell = m1._cells[0][0]
                exit_cell = m1._cells[-1][-1]
                self.assertEqual(sum(entrance_cell.walls()), 4)
                self.assertEqual(sum(entrance_cell.walls()), 4)

                m1._break_entrance_and_exit()

                self.assertEqual(sum(entrance_cell.walls()), 3)
                self.assertTrue(not (entrance_cell.has_left_wall and
                                     entrance_cell.has_top_wall))
                self.assertEqual(sum(exit_cell.walls()), 3)
                self.assertTrue(not (exit_cell.has_right_wall and
                                     exit_cell.has_bottom_wall))


if __name__ == "__main__":
    unittest.main()