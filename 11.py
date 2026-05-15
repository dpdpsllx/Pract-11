def is_valid_sudoku(board):
    
    #Проверяем строки
    for row in board:
        nums = []
        
        for cell in row:
            #Пропускаем пустые клетки
            if cell != ".":
                
                #Если число уже было, то Sudoku неверный
                if cell in nums:
                    return False
                
                nums.append(cell)

    #Проверяем столбцы
    for col in range(9):
        nums = []
        
        for row in range(9):
            cell = board[row][col]
            
            if cell != ".":
                if cell in nums:
                    return False
                
                nums.append(cell)

    #Провеяем блоки 3 на 3
    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            
            nums = []

            #Проходим внутри блока
            for row in range(block_row, block_row + 3):
                for col in range(block_col, block_col + 3):
                    
                    cell = board[row][col]

                    if cell != ".":
                        if cell in nums:
                            return False
                        
                        nums.append(cell)
    return True


# Поле Sudoku
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

# Вывод результата
print(is_valid_sudoku(board))
