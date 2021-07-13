# NOTE this also sort of turned into the game/game logic

# dependencies
import os, sys, pygame

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from lib.board import Board

# init pygame
pygame.init()

class Window:
    def __init__(self):
        # define all const colors
        self.colors = {
            "WHITE" : (255, 255, 255),
            "BLACK" : (0, 0, 0),
            "RED" : (255, 0, 0),
            "CYAN" : (11, 247, 255)
        }

        # is the board being solved?
        self.solving = False

        # selector position
        self.selector_x = 0
        self.selector_y = 0

        # load all images
        bg_filepath = os.path.join(".data", os.path.join("images","blank_board.png"))
        self.BG_IMG = pygame.image.load(bg_filepath)

        # white-list events
        self.remove_all_events()
        self.add_allowed_events()

        # define all fonts
        self.NUM_FONT = pygame.font.SysFont("comicsans", 90) # NOTE here '50' is the font size

        # create sudoku board
        self.sb = Board(callback=self.draw_window)

        # TODO make a create sudoku method on board later, 
        # then delete this block
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
        self.sb.update_board(hard)
    
    def remove_all_events(self):
        pygame.event.set_blocked(None)

    def add_allowed_events(self):
        pygame.event.set_allowed(pygame.QUIT)
        pygame.event.set_allowed(pygame.KEYDOWN)


    # create window
    def create_window(self):
        # window values
        self.WIN_WIDTH = 900
        self.WIN_HEIGHT = 650

        # create and name window
        self.WIN = pygame.display.set_mode( (self.WIN_WIDTH, self.WIN_HEIGHT) )
        pygame.display.set_caption("Sudoku Solver")

    def destroy_window(self):
        pygame.quit()

    # draw the selection rectangle (if needed)
    def draw_selector(self):
        # only draw it if we are not solving
        if not self.solving:
            # determine rectangle position
            width = 90
            height = 65

            initial_x = 13
            initial_y = 13

            x_interval = 97
            y_interval = 70

            x = initial_x + (x_interval * self.selector_x)
            y = initial_y + (y_interval * self.selector_y)

            # define the rectangle
            selector = pygame.Rect(x, y, width, height) # x, y, width, height

            # draw the rectangle
            pygame.draw.rect(self.WIN, self.colors["CYAN"], selector)

    # display boards numbers
    def display_numbers(self, make_zeros_red=False, furthest_i=False):
        # vars to help with text placement on WIN
        initial_x = 40
        initial_y = 20

        x_interval = 97
        y_interval = 70

        for i in range(len(self.sb.grid)):
            # get and create text
            cell_value = str(self.sb.grid[i])
            if not make_zeros_red and not furthest_i:
                cell_text = self.NUM_FONT.render(cell_value, 1, self.colors["BLACK"])
            else:
                cell_text = self.NUM_FONT.render(cell_value, 1, self.colors["BLACK"]) if int(cell_value) != 0 or i > furthest_i else self.NUM_FONT.render(cell_value, 1, self.colors["RED"])

            # define the width and height
            width = initial_x + (x_interval * (i % self.sb.width) )
            height = initial_y + (y_interval * (i // self.sb.width) )

            # blit text to screen
            self.WIN.blit(cell_text, (width, height) )

    # draw window
    def draw_window(self, make_zeros_red=False, furthest_i=False):
        # set bg to white
        self.WIN.blit(self.BG_IMG, (0, 0) )

        # draw the selector
        self.draw_selector()

        # draw the boards numbers to the grid
        self.display_numbers(make_zeros_red=make_zeros_red, furthest_i=furthest_i)

        # update window
        pygame.display.update()

    # main loop
    def main_loop(self):
        self.running = True
        while self.running:
            # event loop
            for event in pygame.event.get():
                # QUIT event
                if event.type == pygame.QUIT:
                    self.running = False

                # KEYDOWN event
                if event.type == pygame.KEYDOWN:
                    # define a keys list (for bulk key press checking)
                    keys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
                    if event.key in keys:
                        # what number was pressed?
                        number_pressed = keys.index(event.key)
                        
                        # find cells index
                        horizontal_value = self.selector_x
                        vertical_value = self.selector_y * self.sb.width

                        i = horizontal_value + vertical_value

                        # update cell
                        self.sb.update_cell(i, number_pressed) 

                    # space bar means quick solve
                    elif event.key == pygame.K_SPACE:
                        # set solving to true
                        self.solving = True

                        # set the callback to false and solve
                        self.sb.callback = False

                        # remove events to stop 'not responding message'
                        self.remove_all_events()

                        self.sb.solve_board()

                        # add events back when done
                        self.add_allowed_events()

                    elif event.key == pygame.K_v:
                        # set solving to true
                        self.solving = True

                        # remove events to stop 'not responding message'
                        self.remove_all_events()

                        # solve (long)
                        self.sb.solve_board()

                        # add events back when done
                        self.add_allowed_events()

                    elif event.key == pygame.K_DOWN:
                        self.selector_y = self.selector_y + 1 if self.selector_y +1 <= self.sb.width -1 else self.sb.width -1 
                    
                    elif event.key == pygame.K_UP:
                        self.selector_y = self.selector_y - 1 if self.selector_y -1 >= 0 else 0 
                        
                    elif event.key == pygame.K_RIGHT:
                        self.selector_x = self.selector_x +1 if self.selector_x +1 <= self.sb.width -1 else self.sb.width -1
                    
                    elif event.key == pygame.K_LEFT:
                        self.selector_x = self.selector_x -1 if self.selector_x -1 >= 0 else 0
                
            # draw/update the window
            self.draw_window()

    def main(self):
        self.create_window()

        self.main_loop()

if __name__ == "__main__":
    w = Window()
    w.main()
