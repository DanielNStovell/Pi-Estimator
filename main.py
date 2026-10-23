import random
import matplotlib.pyplot as plt
import numpy as np

GENERATION_NUMBER = 5  # Number of generations
ITERATION_NUMBER = 10000  # Number of points generated per iteration


def generate_point() -> float:
    # Generate a random point from (0,0) to (1,1)
    # Displaces it to be in range (-1, -1) to (1, 1)
    return random.random() * 2 - 1, random.random() * 2 - 1


def validate_point(x: float, y: float) -> bool:
    # Returns whether the point lies within region of circle (x^2 + y^2 < 1)
    return x**2 + y**2 < 1


def main():
    for _ in range(GENERATION_NUMBER):
        N_outside = 0  # Number of points outside the circle region
        N_inside = 0  # Number of points inside the circle region
        estimations = []  # Estimations of pi each itteration

        for _ in range(ITERATION_NUMBER):
            x, y = generate_point()

            if validate_point(x, y):
                N_inside += 1
            else:
                N_outside += 1

            # pi r^2 / 4 = Probability of point lies in circle
            # pi / 4 = probability => probability * 4 = pi
            estimations.append((N_inside / (N_outside + N_inside)) * 4)
        
        plt.plot(np.array(estimations), linestyle='-', label='Pi Estimation')
    plt.axhline(y=np.pi, color='r', linestyle='--', label='True Pi ($\pi$')
    plt.show()

if __name__ == "__main__":
    main()