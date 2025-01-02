import pandas as pd
import numpy as np


def add_noise_to_column(
        csv_file,
        output_file,
        column_name,
        distribution,
        num_duplicates,
        **distribution_params
):

    df = pd.read_csv(csv_file)
    result = pd.DataFrame()

    for i in range(num_duplicates):
        temp_df = df.copy()

        if distribution == "gamma":
            scale = distribution_params.get("scale", 1.0)
            shape = distribution_params.get("shape", 2.0)
            noise = np.random.gamma(shape, scale, len(df)) - (shape * scale)
        elif distribution == "gauss":
            mu = 0
            sigma = distribution_params.get("sigma", 1.0)
            noise = np.random.normal(mu, sigma, len(df))
        temp_df[column_name] += noise * temp_df[column_name]
        result = pd.concat([result, temp_df], ignore_index=True)

    result.to_csv(output_file, index=False)
    print(f"File saved with noisy data to {output_file}")

    return result


csv_path = "bungee_drops.csv"
output_path = "bungee_drops.csv"

noisy_df = add_noise_to_column(
    csv_file=csv_path,
    output_file=output_path,
    column_name="optimal_drop_length",
    distribution="gamma",
    num_duplicates=30,
    shape=2.0,
    scale=0.1,
    sigma=0.05 
)
