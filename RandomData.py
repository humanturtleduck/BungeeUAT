import numpy as np
import csv


elasticity_constant=1
accel=9.8

def generate_large_bungee_dataset(csv_file_path, num_samples=int(open("datalines.txt","r").read())):

    min_mass, max_mass = 0.05, 0.30
    min_height, max_height = 1.0, 5.0

    with open(csv_file_path, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["drop_height", "drop_mass", "optimal_drop_length"])

        for e in range(num_samples):
            mass = np.random.uniform(min_mass, max_mass)
            height = np.random.uniform(min_height, max_height)

            noise = np.random.normal(loc=0.0, scale=0.05)
            optimal_length = (height+((height*accel*mass-(height*(np.sqrt(accel**2*mass**2+2*accel*mass*elasticity_constant))))/elasticity_constant))+ noise

            optimal_length = max(0.0, optimal_length)

            writer.writerow([
                round(height, 3),
                round(mass, 3),
                round(optimal_length, 3)
            ])

samples=int(open("datalines.txt","r").read())

if __name__ == "__main__":
    generate_large_bungee_dataset("bungee_drops.csv", num_samples=samples)
    print("Large dataset generated: bungee_drops.csv")
