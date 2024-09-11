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

        alive_neighbors = 0 # adjacent alive cell neighbors
        cell_rows = self.state_matrix.shape[0]
        cell_cols = self.state_matrix.shape[0]


        # apply game fules to every cell in the matrix
        for row_idx in range(cell_rows):
            for col_idx in range(cell_cols):
                # value
                cell = self.state_matrix[row_idx][col_idx]

                # count neighbors