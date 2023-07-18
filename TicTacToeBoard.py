#TicTacToe!

board_size = input("Chess, TicTacToe, or Go?")


board_size = board_size.lower()
board_size = board_size.replace(" ", "")
size = 0

if board_size == 'chess':
    #8x8
    size = 8
    line = ''
    line2 = ''
    for i in range(size):
        line = line + ' ---'
        line2 = line2 + '|   '
    line2 = line2 + '|'

    for i in range(size):
        print(line)
        print(line2)
    print(line)

if board_size == 'ttt': 
    #3x3
    size = 3
    line = ''
    line2 = ''
    for i in range(size):
        line = line + ' ---'
        line2 = line2 + '|   '
    line2 = line2 + '|'

    for i in range(size):
        print(line)
        print(line2)
    print(line)
    

if board_size == 'go':
    #19x19
    size = 19
    line = ''
    line2 = ''
    for i in range(size):
        line = line + ' ---'
        line2 = line2 + '|   '
    line2 = line2 + '|'

    for i in range(size):
        print(line)
        print(line2)
    print(line)




