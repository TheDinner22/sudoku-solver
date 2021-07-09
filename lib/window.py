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
            "WHITE" : (255, 255, 255)
        }

        # create sudoku board
        self.sb = Board()

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
    
    # create window
    def create_window(self):
        # window values
        self.WIN_WIDTH = 900
        self.WIN_HEIGHT = 500

        # create and name window
        self.WIN = pygame.display.set_mode( (self.WIN_WIDTH, self.WIN_HEIGHT) )
        pygame.display.set_caption("Sudoku Solver")

    def destroy_window(self):
        pygame.quit()

    # create rectangles/lines for board

    # draw window
    def draw_window(self):
        # set bg to white
        self.WIN.fill(self.colors["WHITE"])

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
                    self.destroy_window()

            # draw/update the window
            self.draw_window()

    def main(self):
        self.create_window()

        self.main_loop()

if __name__ == "__main__":
    w = Window()
    w.main()
