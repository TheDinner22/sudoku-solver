import sys

# whole grid
class Board:
    def __init__(self, n=3):
        self.n = int(n)
        self.width = n * n
        self.height = self.width # this is to make things more human readable 
        self.grid = []

        # generate the grid
        for i in range(n**4):
            self.grid.append(i)

    def pretty_print_grid(self):
        for i in range(1,len(self.grid)+1):
            cell = self.grid[i-1]
            sys.stdout.write(str(cell))
            self.spacer(cell)
            if (i % self.width) == 0:
                print()

    def spacer(self, msg):
        """only works when 4>n>0"""
        msg = str(msg)
        msg_len = len(msg)
        if msg_len == 1:
            sys.stdout.write("  ")
        elif msg_len == 2:
            sys.stdout.write(" ")

    def return_row_of_index(self, cell_index, print_test_grid=False): # WORKING
        # define container for row
        row_as_list = []

        # get the number at the highest row AND in the same col
        col_index = cell_index
        while col_index >= self.width:
            col_index  = col_index - self.width if col_index - self.width > -1 else col_index
        
        # get how many spaces are to the left and right
        spaces_to_left = col_index
        spaces_to_right = (self.width - spaces_to_left) -1

        # get the left and right cells

        # left of:
        for i in range(0,spaces_to_left):
            i+=1
            row_as_list.append(self.grid[cell_index-i])
        # reverse the list to correct for the fact that I got cells right-to-left
        row_as_list = row_as_list[::-1]

        # add the cell itself
        row_as_list.append(self.grid[cell_index])        

        # right of:
        for i in range(0,spaces_to_right):
            i +=1
            row_as_list.append(self.grid[cell_index+i])


        # do the optional, tesing/printing code here
        if print_test_grid:
            # NOTE this is test code so i dont care about it being 100% the 
            # best it can be
            # also this depends on the grid having uniqe cell values
            green_indices = range(cell_index-spaces_to_left,cell_index+spaces_to_right+1)
            counter = 0
            for cell in self.grid:
                if self.grid.index(cell) in green_indices:
                    pass
                    sys.stdout.write('\033[92m'+str(cell)+'\033[0m')
                    self.spacer(cell)
                elif self.grid.index(cell) == col_index:
                    pass
                    sys.stdout.write('\033[91m'+str(cell)+'\033[0m')
                    self.spacer(cell)
                else:
                    pass
                    sys.stdout.write(str(cell))
                    self.spacer(cell)

                counter += 1

                if counter >= self.width:
                    counter = 0
                    print()


        #return the list
        return row_as_list   

    def return_col_of_index(self, cell_index, print_test_grid=False): # WORKING
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
        if print_test_grid:
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
                        self.spacer(cell)
                    else:
                        sys.stdout.write('\033[92m'+str(cell)+'\033[0m')
                        self.spacer(cell)
                else:
                    sys.stdout.write(str(cell))
                    self.spacer(cell)

                counter += 1

                if counter >= self.width:
                    counter = 0
                    print()


        # return the list
        return col_as_list
        
    def return_nxn_grid_of_index(self, cell_index, print_test_grid=False):
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
            if cell_index in sub_grid and not print_test_grid:
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
                    self.spacer(cell)
                else:
                    sys.stdout.write('\033[92m'+str(cell)+'\033[0m')
                    self.spacer(cell)
            else:
                sys.stdout.write(str(cell))
                self.spacer(cell)

            counter += 1

            if counter >= self.width:
                counter = 0
                print()

        # return again
        return sub_grid


if __name__ == "__main__":
    g = Board()#n=2)

    #g.return_row_of_index(43,print_test_grid=True)

    #print(g.return_col_of_index(52,print_test_grid=True))

    #g.pretty_print_grid()

    print(g.return_nxn_grid_of_index(5,print_test_grid=True))


# (x, y, z)

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
