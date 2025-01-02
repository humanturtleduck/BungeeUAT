import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

boolVerbose=open("verbose.txt","r").read()

print(boolVerbose)

if str(boolVerbose)=="False":
    boolVerbose=0
else:
    boolVerbose=1

print(boolVerbose)

epochCount=int(open("epochs.txt","r").read())

def load(dir):
    data = pd.read_csv(dir)
    X = data[['drop_height', 'drop_mass']].values
    y = data['optimal_drop_length'].values
    
    return X, y


def comp(hidden_layer_sizes):
    model = Sequential()

    model.add(Dense(hidden_layer_sizes[0], activation='relu', input_shape=(2,)))

    for size in hidden_layer_sizes[1:]:
        model.add(Dense(size, activation='relu'))

    model.add(Dense(1))

    model.compile(
        optimizer='adam',
        loss='mean_squared_error',
        metrics=['mean_absolute_error']
    )

    return model


def main(dir):
    X, y = load(dir)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    cin=open("hidden_layers.txt","r").readlines()
    model = comp(cin)
    history = model.fit(
        X_train, y_train,
        validation_data=(X_test, y_test),
        epochs=epochCount,
        batch_size=32,
        verbose=boolVerbose
    )

    test_loss, test_mae = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test MSE Loss: {test_loss:.4f}")
    print(f"Test MAE: {test_mae:.4f}")


    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.plot(history.history['loss'], label='Train Loss(MSE)')
    plt.plot(history.history['val_loss'], label='Validation Loss(MSE)')
    plt.xlabel('Epoch')
    plt.ylabel('MSE Loss')
    plt.title('Training vs. Validation Loss')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(history.history['mean_absolute_error'], label='Train MAE')
    plt.plot(history.history['val_mean_absolute_error'], label='Validation MAE')
    plt.xlabel('Epoch')
    plt.ylabel('MAE')
    plt.title('Training vs. Validation MAE')
    plt.legend()

    plt.tight_layout()
    plt.show()

    #prediction time!!!

    '''
    index=0
    for y in range(50,301):
        print(f"{y} values predicted")
        for x in range(200,501):
            sample_input = np.array([[x/100, y/1000]])  # meters, kg
            prediction = model.predict(sample_input, verbose=False)
            predictions.write(str(prediction[0][0]))
            predictions.write(",")
            #index+=1
            #print(f"{index}/75000 values predicted")
            pass
        predictions.write("\n")
    predictions.close()
    '''

    #predictions=open("bungee_predictions.csv","w")

    sample_input = np.array([[2.0, 0.05]])  # meters, kg
    prediction = model.predict(sample_input)
    print(f"Predicted optimal drop length for height=2.0 m and mass=0.05 kg: {prediction[0][0]:.3f} m")
    print(prediction)
    index=0
    heights_1d = np.arange(2.0, 5.01, 0.01)
    masses_1d = np.arange(0.05, 0.301, 0.001)

    heights, masses = np.meshgrid(heights_1d, masses_1d)

    input_data = np.stack([heights.flatten(), masses.flatten()], axis=1)

    predictions_array = model.predict(input_data)
    predictions_grid = predictions_array.reshape(masses.shape)


    rows, cols = predictions_grid.shape

    with open("bungee_predictions.csv", "w") as f:

        header_row = ["KG/M"]
        for j in range(cols):
            header_row.append(f"{heights_1d[j]:.2f} M")
        f.write(",".join(header_row) + "\n")
        for i in range(rows):
            row_values = []
            row_values.append(f"{masses_1d[i]:.3f} KG")
            for j in range(cols):
                val = predictions_grid[i, j]
                row_values.append(f"{val:.6f} M")

            f.write(",".join(row_values) + "\n")

    print("Predicted all the drop lengths, make sure to subscr-")


if __name__ == '__main__':
    csv_file = 'bungee_drops.csv'
    main(csv_file)
