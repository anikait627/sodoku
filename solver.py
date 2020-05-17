#current boardfor testing 
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#solve for the sodoku board
def solve(arr):
    
    #base case for recursion
    find = find_empty(arr)  
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        #check of the empty box hasa valid solution
        if valid(arr, i, (row,col)):
            arr[row][col] = i

            #reusively call on the board
            if solve(arr):
                return True
            
            #reset the value if it is not a vald solution
            arr[row][col] = 0
    
    return False


#take in a board ,number, and position on the board
def valid(arr, num, pos):
    #check row
    for i in range(len(arr[0])):
        if arr[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(arr[0])):
        if arr[i][pos[1]] == num and pos[0] != i:
            return False

    #check whether it is valid within the subbox
    x = pos[1] // 3 #check whcih column 
    y = pos[0] // 3 #check whcih row

    #make sure to iterate through the correct box
    for i in range (y*3, y*3+3): 
        for j in range (x*3, x*3+3):
            #check whether there are duplicates for the secected number
            if arr[i][j] == num and (i, j) != pos:
                return False
    
    return True


def print_board(selected_board):
    for i in range(len(selected_board)):
        #check for the subset box (in terms of rows)
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(selected_board[i])):
            #check for box in terms of columns 
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            #check last character 
            if j == 8:
                print(selected_board[i][j])
            else:
                print(str(selected_board[i][j]) + " ", end="")


def find_empty(arr):
    #serch for empty spots on the board
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                #return a tuple of the empty spot on the board
                return (i,j) 
    return None


print_board(board)
print('--------------------------------------------------------------------')
solve(board)
print_board(board)
