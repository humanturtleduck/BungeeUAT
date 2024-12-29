import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

boolVerbose=open("verbose.txt","r").read()

if boolVerbose=="True":
    boolVerbose=1
else:
    boolVerbose=0

epochCount=int(open("epochs.txt","r").read())

def load(dir):
    data = pd.read_csv(dir)
    X = data[['drop_height', 'drop_mass']].values
    y = data['optimal_drop_length'].values
    
    return X, y

def comp():
    model = Sequential([
        Dense(16, activation='relu', input_shape=(2,)),
        Dense(16, activation='relu'),
        Dense(8, activation='relu'),
        Dense(1)  # single output: predicted optimal length
    ])
    model.compile(
        optimizer='adam',
        loss='mean_squared_error',
        metrics=['mean_absolute_error']
    )
    return model


def main(dir):
    # 1. Load your data
    X, y = load(dir)

    # 2. Split into train/test (80/20 for example)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3. Build and train the model
    model = comp()
    history = model.fit(
        X_train, y_train,
        validation_data=(X_test, y_test),
        epochs=epochCount,
        batch_size=32,
        verbose=boolVerbose  # set to 1 if you want to see training progress
    )

    # 4. Evaluate the model
    test_loss, test_mae = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test MSE Loss: {test_loss:.4f}")
    print(f"Test MAE: {test_mae:.4f}")

    # 5. Visualize training curves (optional)
    plt.figure(figsize=(12, 4))

    # Loss
    plt.subplot(1, 2, 1)
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Val Loss')
    plt.xlabel('Epoch')
    plt.ylabel('MSE Loss')
    plt.title('Training vs. Validation Loss')
    plt.legend()

    # MAE
    plt.subplot(1, 2, 2)
    plt.plot(history.history['mean_absolute_error'], label='Train MAE')
    plt.plot(history.history['val_mean_absolute_error'], label='Val MAE')
    plt.xlabel('Epoch')
    plt.ylabel('MAE')
    plt.title('Training vs. Validation MAE')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # 6. Use the model to make predictions on *new* data
    # Example usage: Suppose we want to predict for drop_height=2.5 m, drop_mass=0.65 kg
    sample_input = np.array([[2.5, 0.65]])  # shape: (1, 2)
    prediction = model.predict(sample_input)
    print(f"Predicted optimal drop length for height=2.5 m and mass=0.65 kg: {prediction[0][0]:.3f} m")


if __name__ == '__main__':
    # Pass the path to your CSV file here
    csv_file = 'bungee_drops.csv'
    main(csv_file)