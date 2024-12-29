import numpy as np
import csv


elasticity_constant=1
accel=9.8

def generate_large_bungee_dataset(csv_file_path, num_samples=1000):
    """
    Generates a synthetic bungee dataset with the given number of samples.

    Columns:
    1) drop_height (m)
    2) drop_mass (kg)
    3) optimal_drop_length (m) - a synthetic value based on a rough formula
    """
    np.random.seed(42)  # for reproducibility

    # Ranges
    min_mass, max_mass = 0.05, 0.30  # kg
    min_height, max_height = 1.0, 5.0  # m

    with open(csv_file_path, mode='w', newline='') as f:
        writer = csv.writer(f)
        # Write header
        writer.writerow(["drop_height", "drop_mass", "optimal_drop_length"])

        for _ in range(num_samples):
            # Randomly pick mass and height in the specified ranges
            mass = np.random.uniform(min_mass, max_mass)
            height = np.random.uniform(min_height, max_height)

            # Synthetic formula: optimal_drop_length = 0.3*height + 0.8*mass + small_noise
            noise = np.random.normal(loc=0.0, scale=0.05)  # mean=0, std=0.05
            optimal_length = (height+((height*accel*mass-(height*(np.sqrt(accel**2*mass**2+2*accel*mass*elasticity_constant))))/elasticity_constant))+ noise

            # Ensure it's not negative (in case noise makes it tiny for small values)
            optimal_length = max(0.0, optimal_length)

            writer.writerow([
                round(height, 3),
                round(mass, 3),
                round(optimal_length, 3)
            ])


if __name__ == "__main__":
    generate_large_bungee_dataset("bungee_drops.csv", num_samples=200)
    print("Large dataset generated: bungee_drops.csv")
