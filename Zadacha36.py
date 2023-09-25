# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation):
    num_rows = int(input('Введите количество рядов: '))
    num_columns = int(input('Введите количество столбцов: '))
    for row in range(1, num_rows+1):
        for column in range(1, num_columns+1):
            number = operation(row, column)
            print(number, end='\t')
        print()


find_number = lambda row, column: row * column


print_operation_table(find_number)
