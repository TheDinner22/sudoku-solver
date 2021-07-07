# solve da puzzle!

# dependencies
import os, sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from lib.board import Board

def solve_board(sb):
    # init the current_i var
    current_i = 0

    while current_i != len(sb.grid):
        if current_i in sb.mutable_indices:
            # get the cell value
            cell_value = sb.grid[current_i]

            # if its valid and not 0, move on 
            if sb.is_index_valid(current_i) and cell_value != 0:
                current_i += 1

            # otherwise increment it or back track if needed
            else:
                # increment the value
                new_value = cell_value + 1 if cell_value + 1 <= 9 else 0
                sb.update_cell(current_i, new_value)

                # re-run to check the new value (if it != 0)
                if new_value:
                    continue

                # otherwise back track and increment the previous value
                else:
                    # define a flag for back tracking
                    back_tracking = True

                    # move current_i back to the previous muteable cell
                    current_i = sb.mutable_indices[sb.mutable_indices.index(current_i) -1]

                    # increment the new current_i by one, unless it is 9 in which case back track twice (or 3, 4, 5, etc times)
                    while back_tracking:
                        cell_value = sb.grid[current_i]
                        if cell_value == 9:
                            # reset this cell to 0
                            sb.update_cell(current_i, 0)

                            # move current_i to the previous muteable index
                            current_i = sb.mutable_indices[sb.mutable_indices.index(current_i) -1]

                        else:
                            # increment the cell value and stop back tracking
                            new_value = cell_value + 1
                            sb.update_cell(current_i, new_value)
                            back_tracking = False
        else:
            current_i += 1

if __name__ == "__main__":
    b = Board()

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

    b.update_board(simple)

    solve_board(b)

    b.pretty_print_grid()