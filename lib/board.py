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

    def pretty_print_grid(self):
        for i in range(1,len(self.grid)+1):
            cell = self.grid[i-1]
            sys.stdout.write(str(cell))
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


if __name__ == "__main__":
    g = Board(print_test_grid=True)#,n=2)

    my_sb = [
    2,3,5,1,7,8,6,9,9,
    7,5,6,0,0,3,0,8,5,
    0,0,1,0,2,0,0,0,0,
    0,0,0,5,0,7,0,0,0,
    0,0,4,0,0,0,1,0,0,
    0,9,0,0,0,0,0,0,0,
    5,0,0,0,0,0,0,7,3,
    0,0,2,0,1,0,0,0,0,
    0,0,0,0,4,0,0,0,9
]
    #print(g.return_row_of_index(44))

    #print(g.return_col_of_index(52))

    g.update_board(my_sb)

    g.pretty_print_grid()

    print(g.is_index_valid(11))

    #print(g.return_nxn_grid_of_index(11))

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
