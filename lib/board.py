# dependencies
import sys

# whole grid
class Board:
    def __init__(self, n=3, print_test_grid=False):
        self.n = int(n)
        self.print_test_grid = print_test_grid # TODO remove me
        self.width = n * n
        self.height = self.width # this is to make things more human readable 
        self.grid = []
        self.mutable_indices = []

        # generate the grid
        if print_test_grid:
            self.mutable_indices.append(0)
            for i in range(n**4):
                self.grid.append(i)
        else:
            for i in range(n**4):
                self.mutable_indices.append(i)
                self.grid.append(0)

    def pretty_print_grid(self): # TODO remove the need for sys in this and all other files
        for i in range(1,len(self.grid)+1):
            cell = self.grid[i-1]
            if i-1 in self.mutable_indices:
                sys.stdout.write(str(cell))
            else:
                print('\033[91m'+str(cell)+'\033[0m', end="")
            self._spacer(cell)
            if (i % self.width) == 0:
                print()

    def _spacer(self, msg):
        """only works when 4>n>0"""
        msg = str(msg)
        msg_len = len(msg)
        if msg_len == 1:
            sys.stdout.write("  ")
        elif msg_len == 2:
            sys.stdout.write(" ")

    def update_board(self, board_list):
        # update the grid
        if len(board_list) == len(self.grid):
            self.grid = board_list

            # update self.immuteable indices # NOTE if an element == 0 it is muteable
            # TODO can this code be made better?
            self.mutable_indices = []
            for i in range(len(self.grid)):
                cell = self.grid[i]
                if not cell:
                    self.mutable_indices.append(i)
            
    def update_cell(self, cell_index, value):
        if cell_index in self.mutable_indices:
            self.grid[cell_index] = value
        else:
            print("cannot update immutable cell: ", cell_index)

    def return_row_of_index(self, cell_index):
        col_index = cell_index%self.width
        return self.grid[cell_index - col_index : cell_index-col_index + self.width]

    def return_col_of_index(self, cell_index):
        col_index = cell_index % self.width
        return self.grid[col_index::self.width]

    def return_nxn_grid_of_index(self, cell_index):
        # defin the starting index (top_left corner of sub_grid)
        x_pos = ((cell_index % self.width) // self.n) * self.n

        row_num = (cell_index // self.width)
        y_pos =  (row_num - (row_num % self.n)) * self.width 

        start_i = x_pos + y_pos 
        # make sub_grid here
        sub_grid = []
        for x in range(self.n):
            sub_grid += self.grid[(start_i + (x * self.width)):(start_i + (x * self.width))+self.n]

        # return the sub_grid
        return sub_grid
        
    def is_index_valid(self, cell_index):
        # TODO make this tell you which cells are causing the problem and return a bool
        # get the row, col, and sub_grid for the index
        row_list = self.return_row_of_index(cell_index)
        col_list = self.return_col_of_index(cell_index)
        subgrid_list = self.return_nxn_grid_of_index(cell_index)

        lists = [row_list, col_list, subgrid_list]

        # loop through all of these checking for repeat elements in the lists
        for i in range(len(lists)):
            l = lists[i]

            # remove all 0's
            l = list(filter((0).__ne__, l))

            set_l = list(set(l))

            # sort both lists # TODO this needs to be changed later
            set_l.sort()
            l.sort()

            if l != set_l:
                return False

        # return true if for loop runs
        return True

    def solve_board(self):
        '''solve da puzzle!'''
        current_mutable_i = 0
        while current_mutable_i < len(self.mutable_indices):
            current_board_i = self.mutable_indices[current_mutable_i]
            cell_value = self.grid[current_board_i]

            # if the cell is valid and not 0, increment
            if self.is_index_valid(current_board_i) and cell_value != 0:
                current_mutable_i += 1

            # other wise, increment/backtrack
            else:
                new_value = cell_value + 1 if cell_value + 1 <= 9 else 0
                self.update_cell(current_board_i, new_value)

                # if the increment was 0 back track as much as needed
                if not new_value:
                    back_tracking = True
                    while back_tracking:
                        # move to the previous mutable cell
                        current_mutable_i -= 1
                        current_board_i = self.mutable_indices[current_mutable_i]
                        
                        # get and update cell value
                        cell_value = self.grid[current_board_i]
                        new_value = cell_value + 1 if cell_value + 1 <= 9 else 0
                        self.update_cell(current_board_i, new_value)

                        # check to see if back tracking is still needed
                        if new_value:
                            # stop back track
                            back_tracking = False


if __name__ == "__main__":
    # simple
    simple = [
        0,0,0,4,0,3,0,6,0,
        0,0,0,2,0,0,0,0,3,
        0,0,5,1,0,6,0,0,0,
        1,7,8,0,0,0,9,0,5,
        0,0,0,0,0,0,0,0,0,
        9,0,3,0,0,0,1,7,6,
        0,0,0,3,0,1,5,0,0,
        7,0,0,0,0,2,0,0,0,
        0,6,0,5,0,8,0,0,0
    ]

    # easy
    easy = [
        0,0,1,6,0,2,0,0,0,
        0,9,0,8,0,0,0,0,0,
        0,0,6,4,0,0,0,7,0,
        0,0,5,0,4,0,2,0,3,
        2,1,9,5,3,6,7,4,8,
        0,0,0,0,8,1,9,0,6,
        0,7,0,0,0,0,6,0,0,
        0,0,0,0,0,4,0,3,0,
        0,0,0,3,0,5,4,0,0
    ]

    # medium
    medium = [
        1,5,7,6,4,0,0,9,8,
        2,0,9,0,0,0,0,0,0,
        0,0,0,9,1,0,0,0,4,
        8,0,0,4,3,0,0,5,0,
        0,0,0,0,0,0,0,0,0,
        0,2,0,0,6,8,0,0,7,
        7,0,0,0,8,6,0,0,0,
        0,0,0,0,0,0,0,0,1,
        0,9,0,0,0,4,8,6,2
    ]

    # hard
    hard = [
        6,0,0,0,0,0,0,0,8,
        0,4,0,9,0,2,0,3,0,
        0,0,3,0,1,0,4,0,0,
        0,2,0,6,0,5,0,8,0,
        0,0,5,0,0,0,7,0,0,
        0,1,0,7,0,9,0,2,0,
        0,0,4,0,9,0,1,0,0,
        0,3,0,5,0,8,0,6,0,
        7,0,0,0,0,0,0,0,0
    ]

    # really hard (this was made to counter back tracking and takes 1-2 hours to solve)
    rh = [
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,3,0,8,5,
        0,0,1,0,2,0,0,0,0,
        0,0,0,5,0,7,0,0,0,
        0,0,4,0,0,0,1,0,0,
        0,9,0,0,0,0,0,0,0,
        5,0,0,0,0,0,0,7,3,
        0,0,2,0,1,0,0,0,0,
        0,0,0,0,4,0,0,0,9
    ]
    g = Board()

    g.update_board(hard)

    g.solve_board()

    g.pretty_print_grid()

'''
ml= [
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 1, 0, 0, 0, 0, 0, 0,
0, 1, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0
]
'''
