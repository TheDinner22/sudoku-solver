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

    def return_col_of_index(self, cell_index): # WORKING
        # define container for col
        col_as_list = []

        # get the number at the highest row AND in the same row 
        col_index = cell_index
        while col_index >= self.width:
            col_index  = col_index - self.width if col_index - self.width > -1 else col_index

        # add the col_index to the list
        col_as_list.append(self.grid[col_index])

        # add all of the other colums under col_index to a list
        for x in range(1, self.height):
            next_row_down_index = col_index + (self.width * x)
            col_as_list.append(self.grid[next_row_down_index])

        # do the optional, tesing/printing code here
        if self.print_test_grid:
            # NOTE this is test code so i dont care about it being 100% the 
            # best it can be
            # also this depends on the grid having uniqe cell values
            counter = 0
            green_indices = [col_index]

            # add all of the other column index's under col_index to the list
            for x in range(1, self.height):
                next_row_down_index = col_index + (self.width * x)
                green_indices.append(next_row_down_index)

            for cell in self.grid:
                if self.grid.index(cell) in green_indices:
                    if self.grid.index(cell) == col_index:
                        sys.stdout.write('\033[91m'+str(cell)+'\033[0m')
                        self._spacer(cell)
                    else:
                        sys.stdout.write('\033[92m'+str(cell)+'\033[0m')
                        self._spacer(cell)
                else:
                    sys.stdout.write(str(cell))
                    self._spacer(cell)

                counter += 1

                if counter >= self.width:
                    counter = 0
                    print()

        # return the list
        return col_as_list
        
    def return_nxn_grid_of_index(self, cell_index):
        # NOTE here I just create and then loop through all of the sub_grids until 
        # I find the one the given index is in 
        # if this turns out to be too slow I will refactor later

        # create all of the nxn sub-grids
        start_i = 0
        for i in range(self.width):
            # make sub_grid here
            sub_grid = []
            for i in range(self.width):
                add_num = i % self.n
                i = i // self.n
                sub_grid.append((start_i+add_num) + (self.width * i))

            # update the starting index      ### NOTE pretty proud I got this to work second try 🧠🧠🧠
            start_i = start_i + self.n if (start_i + self.n) % self.width != 0 else (start_i + self.n) + (self.width * (self.n -1))

            # check to see if our index is in the subgrid # we skip this if print_test_grid is True
            if cell_index in sub_grid and not self.print_test_grid:
                # convert indices in sub_grid to cells is self.grid
                for i in range(len(sub_grid)):
                    sub_grid[i] = self.grid[sub_grid[i]]
                return sub_grid
            elif cell_index in sub_grid:
                break

        # print the grid
        
        # NOTE this is test code so i dont care about it being 100% the 
        # best it can be
        # also this depends on the grid having uniqe cell values
        counter = 0
        green_indices = sub_grid

        for cell in self.grid:
            if self.grid.index(cell) in green_indices:
                if self.grid.index(cell) == cell_index:
                    sys.stdout.write('\033[91m'+str(cell)+'\033[0m')
                    self._spacer(cell)
                else:
                    sys.stdout.write('\033[92m'+str(cell)+'\033[0m')
                    self._spacer(cell)
            else:
                sys.stdout.write(str(cell))
                self._spacer(cell)

            counter += 1

            if counter >= self.width:
                counter = 0
                print()

        # return again
        for i in range(len(sub_grid)):
            sub_grid[i] = self.grid[sub_grid[i]]
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
