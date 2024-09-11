import numpy as np

class GameOfLife:
    def __init__(self, state_matrix):
        # game state variables
        self.generations = 0
        self.population = 0
        self.state_matrix = state_matrix

    def next_generation(self):
        '''
            Calculates next generation

            - relative position:
            top, bottom, left, right

            - diagonal position: 
            top-left, bottom-left, top-right, bottom-right
        '''
        
        next_gen = np.zeros_like(self.state_matrix)
        cell_rows, cell_cols = self.state_matrix.shape

        for row_idx in range(cell_rows):
            for col_idx in range(cell_cols):
                # Get the current state of the cell
                cell_state = self.state_matrix[row_idx, col_idx]
                
                # Count live neighbors
                live_neighbors = self.count_live_neighbors(row_idx, col_idx)
                
                # Determine the next state based on the rules of the game
                if cell_state == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        next_gen[row_idx, col_idx] = 0  # Cell dies
                    else:
                        next_gen[row_idx, col_idx] = 1  # Cell stays alive
                else:
                    if live_neighbors == 3:
                        next_gen[row_idx, col_idx] = 1  # Cell is born

        # Update the state matrix with the new generation
        self.state_matrix = next_gen
        self.generations += 1

        # Update population after state matrix is updated
        self.update_population()


    def count_live_neighbors(self, row:int, col:int) -> int:
        """
        Counts the number of alive neighbors around a given cell.

        Parameters:
        - row (int): The row index of the cell to check neighbors for.
        - col (int): The column index of the cell to check neighbors for.

        Returns:
        - int: The number of alive neighbors around the specified cell.
        """

        # grid max rows and cols
        max_rows = self.state_matrix.shape[0]
        max_cols = self.state_matrix.shape[1]

        live_neighbor_count = 0

        # iterate over adjacent cells
        for row_idx in range(-1, 2):
            for col_idx in range(-1, 2):
                # calculate neighbor position
                neighbor_row = row + row_idx
                neighbor_col = col + col_idx

                # check neighbor within bounds
                if 0 <= neighbor_row < max_rows and 0 <= neighbor_col < max_cols:
                    # check if it is a live neighbor (and not the cell itself)
                    if (neighbor_row != row or neighbor_col != col) and self.state_matrix[neighbor_row, neighbor_col] == 1:
                        # increase counter
                        live_neighbor_count += 1

        return live_neighbor_count
    
    def update_population(self)-> int:
        """
        Updates the population count based on the current state of the grid.
        """
        self.population = int(np.sum(self.state_matrix))
