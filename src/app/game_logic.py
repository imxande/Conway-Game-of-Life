class GameOfLife:
    def __init__(self, state_matrix):
        # game state variables
        self.generations = 0
        self.population = 0
        self.state_matrix = state_matrix

        self.next_generation(state_matrix)

    # calculate generations
    def next_generation(self, state_matrix):
        print(state_matrix)
