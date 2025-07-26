import random
import time
import itertools
import numpy as np
import argparse
import copy

class ConwayGameOfLife:
    def __init__(self, row_num = 10, col_num = 10, gen_counter = 10):
        self.row_num = int(row_num)
        self.col_num = int(col_num)
        self.gen_counter = int(gen_counter)
        self.grid = []
        self.history = []
        self._create_grid()

    def _create_grid(self):
        for i in range(self.row_num):
            row_list = []
            for j in range(self.col_num):
                cell_val = random.choice([0, 1])
                row_list.append(cell_val)
            self.grid.append(row_list)
        self.history.append(copy.deepcopy(self.grid))

    def print_grid(self):
        for i in range(self.row_num):
            line = ""
            for j in range(self.col_num):
                if self.grid[i][j] == 1:
                    line += '⬛'
                else:
                    line += '⬜'
            print(line)

    @staticmethod
    def _get_3by3_indices(cell_index, total_len):
        if cell_index > 0 and cell_index < total_len - 1:
            return [cell_index - 1, cell_index, cell_index + 1]
        elif cell_index == 0:
            return [cell_index, cell_index + 1]
        elif cell_index == total_len - 1:
            return [cell_index - 1, cell_index]
        else:
            print(f"Invalid request as {cell_index} lies outside {total_len}")
    
    def count_all_alive_cells(self):
        all_cell_values = list(itertools.chain(*self.grid))
        return sum(all_cell_values)

    def count_live_neighbors(self, row, col):
        row_list = self._get_3by3_indices(row, self.row_num)
        col_list = self._get_3by3_indices(col, self.col_num)

        total_live_neighbors = 0

        for i in row_list:
            for j in col_list:
                if not(i == row and j == col):
                    total_live_neighbors += self.grid[i][j]

        return total_live_neighbors

    def compute_next_gen(self):
        new_grid = [[None] * self.col_num for j in range(self.row_num)]
        for i in range(self.row_num):
            for j in range(self.col_num):
                alive_status = self.grid[i][j]
                live_neighbors = self.count_live_neighbors(i, j)
                
                # Rules of the game
                if alive_status == 1:
                    if live_neighbors in [2, 3]:
                        new_status = 1
                    else:
                        new_status = 0
                else:
                    if live_neighbors == 3:
                        new_status = 1
                    else:
                        new_status = 0
                
                new_grid[i][j] = new_status            
    
        return new_grid

    def play_game(self):
        print("\nBeginning the game ...\n")
        all_alive_cells = self.count_all_alive_cells()
        self.print_grid()
        print(f"The total number of alive cells are {self.count_all_alive_cells()}")
        for i in range(self.gen_counter):
            time.sleep(1)
            print(f"\nGeneration: {i+1}")
            last_gen_grid = copy.deepcopy(self.grid)
            self.grid = self.compute_next_gen()
            self.history.append(last_gen_grid)
            self.print_grid()
            all_alive_cells = self.count_all_alive_cells()
            print(f"The total number of alive cells are {all_alive_cells}")
            if all_alive_cells == 0:
                print("Game ends early as no cells are alive ...\n")
                break
            elif self.grid == last_gen_grid:
                print("Achieved steady state! Game ends ..\n")
                break
            elif self.grid in self.history:
                print("Detected cycle! Game ends ..\n")
                break
        print("\nGame over\n")
            
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--row_number')
    parser.add_argument('-c', '--col_number')
    parser.add_argument('-n', '--num_of_generations')
    args = parser.parse_args()

    conway_game = ConwayGameOfLife(args.row_number, args.col_number, args.num_of_generations)
    conway_game.play_game()
