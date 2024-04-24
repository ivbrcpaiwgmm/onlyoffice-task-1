import os
import pytest
from tree import draw_tree

TEST_DATA = [('temp_tst/tst_1/сhristmas_tree.txt', 1),
             ('temp_tst/tst_2/сhristmas_tree.txt', 5),
             ('temp_tst/сhristmas_tree.txt', 12),
             ('сhristmas_tree.txt', 100),
             ('сhristmas_tree.txt', 20)
             ]


@pytest.fixture(params=TEST_DATA)
def christmas_tree(request):
    path, levels = request.param
    draw_tree(path, levels)
    yield path, levels
    if os.path.exists(path):
        os.remove(path)


@pytest.mark.usefixtures("christmas_tree")
class TestChristmasTree:

    def test_file_creation(self, christmas_tree):
        path = christmas_tree[0]
        assert os.path.exists(path), f"The file {path} doesn't exist."

    def test_file_extension(self, christmas_tree):
        path = christmas_tree[0]
        file_extension = os.path.splitext(path)[1]
        assert file_extension == ".txt", f"the file has extension {file_extension}, not .txt"

    def test_tree_height(self, christmas_tree):
        path, levels = christmas_tree
        try:
            with open(path, 'r') as file:
                content = file.readlines()
                # Одна строка используется для звезды и две для ствола, поэтому использую levels + 3 для проверки.
                assert len(content) == levels + 3, "The height of the tree is incorrect."
        except FileNotFoundError:
            pytest.fail(f"File {path} not found.")

    def test_star_on_top(self, christmas_tree):
        path = christmas_tree[0]
        try:
            with open(path, 'r') as file:
                line_1 = file.readline()
                assert 'W' in line_1, "The Christmas Tree has no star on the top."
        except FileNotFoundError:
            pytest.fail(f"File {path} not found.")

    def test_correct_branches(self, christmas_tree):
        path, levels = christmas_tree
        try:
            with open(path, 'r') as file:
                content = file.readlines()
                branches = [content[line_number].count('*') == (1 + (line_number - 1) * 4) for line_number in
                            range(1, levels + 1)]
                assert all(branches), "There are branches of incorrect size."
        except FileNotFoundError:
            pytest.fail(f"File {path} not found.")

    def test_branches_have_toys(self, christmas_tree):
        path, levels = christmas_tree
        try:
            with open(path, 'r') as file:
                content = file.readlines()
                # На первой строке должна быть звезда, на второй не должно быть игрушки, поэтому использую '2' в range.
                branches_with_toys = ['@' in content[line_number] for line_number in
                                      range(2, levels + 1)]
                assert all(branches_with_toys), "There are branches without toys."
        except FileNotFoundError:
            pytest.fail(f"File {path} not found.")

    def test_correct_trunk(self, christmas_tree):
        path, levels = christmas_tree
        try:
            with open(path, 'r') as file:
                content = file.readlines()
                correct_trunk = content[-1].count('T') == levels and content[-2].count('T') == levels
                assert correct_trunk, "The trunk is incorrect."
        except FileNotFoundError:
            pytest.fail(f"File {path} not found.")
