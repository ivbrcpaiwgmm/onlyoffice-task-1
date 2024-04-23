# Варианты улучшения кода:
# 1) Вынесение в константы символов "звезды", "хвои", "ствола".
# 2) Вынесение повторяющегося функционала записи строки символов в отдельную функцию "draw_row"
# 3) Создание валидации входных данных и обработка соответствующих исключений.


def draw_tree(path: str = 'сhristmas_tree.txt', levels: int = 5) -> None:
    with open(path, 'w') as file:
        width = levels * 4
        file.write('W'.center(width) + '\n')
        for level in range(levels):
            row = ('*' * (1 + level * 4)).center(width)
            if level % 2 == 1:
                asterisk_index = row.find('*')
                row = row[:asterisk_index - 1] + '@' + row[asterisk_index:]
            else:
                asterisk_index = row.rfind('*')
                row = row[:asterisk_index + 1] + ('@' * (level > 0)) + row[asterisk_index + 2:]

            file.write(row + '\n')
        file.write(('T' * levels).center(width) + '\n')
        file.write(('T' * levels).center(width) + '\n')


if __name__ == '__main__':
    my_path = 'сhristmas_tree.txt'
    my_levels = 5
    draw_tree(my_path, my_levels)
