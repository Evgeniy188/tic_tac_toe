# game.py

from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def save_result(res_str):
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(res_str + '\n')


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:

        print(f'Ход делают {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                col = int(input('Введите номер столбца: '))
                if col < 0 or col >= game.field_size:
                    raise FieldIndexError
                if game.board[row][col] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}'
                )
                print(
                    'Пожалуйста, введите значения для строки и столбца заново.'
                )
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print(
                    'Пожалуйста, введите значения для строки и столбца заново.'
                    )
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, col, current_player)
        game.display()
        if game.check_win(current_player):
            res_str = f'Победили {current_player}!'
            print(res_str)
            save_result(res_str)
            running = False

        elif game.is_board_full():
            res_str = 'Ничья!'
            print(res_str)
            save_result(res_str)
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
