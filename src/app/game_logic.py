import numpy as np

class GameOfLife:
    def __init__(self, state_matrix):
        # game state variables
        self.generations = 0
        self.population = 0
        self.state_matrix = state_matrix

    # calculate generations
    def next_generation(self):
        '''
            Calculates next generation

            - relative position:
              top, bottom, left, right

            - diagonal position: 
              top-left, bottom-left, top-right, bottom-right
        '''

        cell_rows = self.state_matrix.shape[0]
        cell_cols = self.state_matrix.shape[0]
        next_gen = np.zeros((cell_rows, cell_cols))



        # apply game fules to every cell in the matrix
        for row_idx in range(cell_rows):
            for col_idx in range(cell_cols):
                # value
                cell_state = self.state_matrix[row_idx][col_idx]

                # count live neighbors
                live_neighbors = self.count_live_neighbors(self.state_matrix, cell_rows, cell_cols)

                # cell borns if is dead(0) and # of alive neighbors is 3
                if (cell_state == 0 and live_neighbors == 3):
                    next_gen[row_idx][col_idx] = 1 # cell becomes alive

                # # cell dies if is alive(1) and isolated or overpopulated
                elif cell_state == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    next_gen[row_idx][col_idx] = 0 # cell dies

                else:
                    next_gen[row_idx][col_idx] = cell_state # cell stays the same

            # update state matric for next gen
            self.state_matrix = next_gen
            self.generations += 1



    def count_live_neighbors(self, matrix:"np.ndarray", rows:int, cols:int)->int:
        """
        Counts the number of alive neighbors around a given cell.

        Parameters:
        - matrix (np.ndarray): A 2D numpy array representing the game grid.
        - rows (int): The row index of the cell to check neighbors for.
        - cols (int): The column index of the cell to check neighbors for.

        Returns:
        - int: The number of alive neighbors around the specified cell.
        """

        # grid max rows and cols
        max_rows = matrix.shape[0]
        max_cols = matrix.shape[1]

        print(max_rows)
        print(max_cols)

        # count 
        live_neighbor_count = 0

        # iterate over adjacent cells
        for row_idx in range(-1, 2):
            for col_idx in range(-1, 2):
                # calculate neighbor position
                neighbor_row = rows + row_idx
                neighbor_col = cols + col_idx

                # check neighbor withing bounds
                if 0 <= neighbor_row < max_rows and 0 <= neighbor_col < max_cols:
                    # check if it is a live neighbor (and not the cell itself)
                    if (neighbor_row != rows or neighbor_col != cols) and matrix[neighbor_row, neighbor_col] == 1:
                        #  increase neighbor count
                         live_neighbor_count += 1

        return live_neighbor_count
    
