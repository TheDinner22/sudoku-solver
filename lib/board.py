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
        self.immutable_indices = [] # TODO make me useful later

        # generate the grid
        if print_test_grid:
            for i in range(n**4):
                self.grid.append(i)
        else:
            for _i in range(n**4):
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

    def update_cell(self, cell_index, value):
        if not cell_index in self.immutable_indices:
            self.grid[cell_index] = int(value) # TODO is the 'int' really needed here??
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
        
if __name__ == "__main__":
    g = Board(print_test_grid=True)#,n=2)

    #print(g.return_row_of_index(44))

    #print(g.return_col_of_index(52))

    #g.pretty_print_grid()

    #print(g.return_nxn_grid_of_index(9))

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
