unit_tests = {}

# dependencies
import os, sys, random

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from lib.board import Board

# Board.return_row_of_index() always returns the correct row
def test1(done):
    # create two different boards to test on
    big_board = Board()
    little_board = Board(n=2)
    why = Board(n=4)

    boards = [big_board, little_board, why]

    # its kind of hard to tell if a test is consistant when using random numbers so this test will be run 50 times
    for i in range(50):
        for board in boards:
            # get the boards width and area
            board_width = board.width

            # change the boards elements so they are not all 0's 
            # this way each row can be uniquely identified 
            for i in range(board_width):
                board.grid[i + (board_width*i)] = 1

            # list of all rows
            rows = []
            for i in range(board_width):
                rows.append(board.grid[ board_width*i : (board_width*i) + board_width ])

            # choose a random row and then choose a random index in that row
            row_index = random.randint(0,board_width-1)
            expected_outcome = rows[row_index]

            cell_index = random.randint(row_index*board_width,(row_index*board_width)+board_width-1)
            
            outcome = board.return_row_of_index(cell_index)

            msg = "outcome:\n" + str(outcome) + "\nwas not equal to expected outcome:\n" + str(expected_outcome) + "\nwhen cell_index = " + str(cell_index) + "\nand row_index = " + str(row_index) + "\nthis happened during iteration: " + str(i+1)
            assert outcome == expected_outcome, msg

    # if no asserts failed the test is a pass
    done("Board.return_row_of_index() always returns the correct row")
unit_tests["Board.return_row_of_index() always returns the correct row"] = test1

# Board.return_col_of_index() always returns the correct column
def test2(done):
    # create two different boards to test on
    big_board = Board()
    little_board = Board(n=2)
    why = Board(n=4) 

    boards = [big_board, little_board, why]

    # its kind of hard to tell if a test is consistant when using random numbers so this test will be run 50 times
    for i in range(50):
        for board in boards:
            # get the boards width and area
            board_width = board.width
            num_of_cells = board_width * board_width

            # change the boards elements so they are not all 0's 
            # this way each column can be uniquely identified 
            for i in range(board_width):
                board.grid[i + (board_width*i)] = 1

            # list of all columns
            columns = []
            for i in range(board_width):
                # TODO this method of getting the columns from a grid might be more 
                # efficient than the way I do it in the actual board.py file... so check that later
                columns.append(board.grid[i:num_of_cells:board_width]) 

            # choose a random column and then choose a random index in that column
            column_index = random.randint(0,board_width-1)
            expected_outcome = columns[column_index]

            cell_index = random.randrange(column_index,num_of_cells,board_width)
            
            outcome = board.return_col_of_index(cell_index)

            msg = "outcome:\n" + str(outcome) + "\nwas not equal to expected outcome:\n" + str(expected_outcome) + "\nwhen cell_index = " + str(cell_index) + "\nand column_index = " + str(column_index) + "\nthis happened during iteration: " + str(i+1)
            assert outcome == expected_outcome, msg

    # if no asserts failed the test is a pass
    done("Board.return_col_of_index() always returns the correct column")
unit_tests["Board.return_col_of_index() always returns the correct column"] = test2

# Board.return_nxn_grid_of_index always returns the correct sub_grid
def test3(done):
    # create two different boards to test on
    big_board = Board()
    little_board = Board(n=2)
    why = Board(n=4)

    boards = [big_board, little_board, why]

    # its kind of hard to tell if a test is consistant when using random numbers so this test will be run 50 times
    for i in range(50):
        for board in boards:
            # get the boards width and area
            board_width = board.width
            num_of_cells = board_width * board_width

            # change the boards elements so they are not all 0's 
            # this way each sub_grid can be uniquely identified 
            for i in range(num_of_cells):
                board.grid[i] = random.randint(0,2)

            # list of all sub_grids
            # TODO this method of getting the sub_grids from a grid might be more 
            # efficient than the way I do it in the actual board.py file... so check that later
            sub_grids = []
            for i in range(board_width):
                sub_grid = []
                for x in range(board.n):
                    # only ok becuase this is unit test
                    # haha the next line has 188 chars in it 
                    sub_grid += board.grid[ ((board_width*x) + ( (i%board.n) * (board.n) ) ) + ((i//board.n)*(board_width*board.n)) : ((board_width*x) + ( (i%board.n) * (board.n) )) + ((i//board.n)*(board_width*board.n))+board.n]
                sub_grids.append(sub_grid)

            # choose a random sub_grid and then choose a random index in that subgrid
            sub_grid_index = random.randint(0,board_width-1)
            expected_outcome = sub_grids[sub_grid_index]

            up_down_pos = (sub_grid_index//board.n)*(board_width*board.n)
            l_r_pos = (sub_grid_index%board.n)*(board.n)
            cell_index = random.randrange(0,board.n) + (random.randrange(0,board.n) * board_width)
            cell_index += up_down_pos + l_r_pos
            
            outcome = board.return_nxn_grid_of_index(cell_index)

            msg = "outcome:\n" + str(outcome) + "\nwas not equal to expected outcome:\n" + str(expected_outcome) + "\nwhen cell_index = " + str(cell_index) + "\nand sub_grid_index = " + str(sub_grid_index) + "\nthis happened during iteration: " + str(i+1)
            assert outcome == expected_outcome, msg

    # if no asserts failed the test is a pass
    done("Board.return_nxn_grid_of_index always returns the correct sub_grid")
unit_tests["Board.return_nxn_grid_of_index always returns the correct sub_grid"] = test3

# Board.update_cell should update Board.grid
def test4(done):
    why = Board(n=4)
    board = Board(n=3)
    little_board = Board(n=2)
    atom = Board(n=1)

    boards = [why, board, little_board, atom]

    for board in boards:
        num_of_cells = board.width * board.width
        random_index = random.randrange(0,num_of_cells)
        test_value = 314159

        # create the expected output
        expected_output = []
        for _i in range(num_of_cells):
            expected_output.append(0)
        expected_output[random_index] = test_value

        # get output
        board.update_cell(random_index,test_value)
        output = board.grid

        # compare outputs
        msg = f"Output:\n{output}\ndid not match expected_output:\n{expected_output}\nwhen random_index = {random_index}\nand test_value = {test_value}\nboard.n = {board.n}"
        assert output == expected_output, msg

    # if the index was updated the test passes
    done("Board.update_cell should update Board.grid")
unit_tests["Board.update_cell should update Board.grid"] = test4

# Board.update_board should do nothing if passed the wrong list
def test5(done):
    why = Board(n=4)
    board = Board(n=3)
    little_board = Board(n=2)
    atom = Board(n=1)

    boards = [why, board, little_board, atom]

    for b in boards:
        expected_outcome = b.grid
        expected_outcome2 = b.mutable_indices

        bad_input = ['', '', '', '', 'qewccs', '', '', '', '', '', '', '', '3224', 'afafds', 'ad', ]

        b.update_board(bad_input)

        outcome = b.grid
        outcome2 = b.mutable_indices

        msg = f'Outcome:\n{outcome} did not match expected outcome:\n{expected_outcome}'
        assert outcome == expected_outcome, msg

        msg = f'Outcome:\n{outcome2} did not match expected outcome:\n{expected_outcome2}'
        assert outcome2 == expected_outcome2, msg

    # if the foor loop ends with no assert errors the test is a pass
    done("Board.update_board should do nothing if passed the wrong list")
unit_tests["Board.update_board should do nothing if passed the wrong list"] = test5 

# Board.is_index_valid should return the correct bool
def test6(done):
    why = Board(n=4)
    board = Board(n=3)
    little_board = Board(n=2)
    atom = Board(n=1)

    boards = [why, board, little_board, atom]

    for b in boards:
        ### Board.grid is all 0's right now so any index should return true
        expected_outcome = True
        i = random.randrange(0,len(b.grid))

        outcome = b.is_index_valid(i)

        msg = f'Outcome:\n{outcome}\ndid not match expected outcome:\n{expected_outcome}\n when i = {i}\nn = {b.n}'
        assert expected_outcome == outcome, msg

        ### any value inserted at i should also be valid
        expected_outcome = True

        # insert a number (3 for no real reason)
        b.update_cell(i, 3)

        outcome = b.is_index_valid(i)

        msg = f'Outcome:\n{outcome}\ndid not match expected outcome:\n{expected_outcome}\n when i = {i}\nn = {b.n}'
        assert expected_outcome == outcome, msg

        # TODO you might want to add a third assert where expected outcome = False

    # if the for loop raises no assert errors, the test passes
    done("Board.is_index_valid should return the correct bool")
unit_tests["Board.is_index_valid should return the correct bool"] = test6

'''
# example tests
def one_plus_one_is_two(done):
    outcome = 1+1
    desired_outcome = 2
    assert outcome == desired_outcome, "1+1 was not equal to two"
    done("one plus one is equal to two")
unit_tests["one plus one is equal to two"] = one_plus_one_is_two

def one_plus_one_is_three(done):
    outcome = 1+1
    desired_outcome = 3
    assert outcome == desired_outcome, "1+1 was not equal to three"
    done("one plus one is equal to three")
unit_tests["one plus one is equal to three"] = one_plus_one_is_three
'''
