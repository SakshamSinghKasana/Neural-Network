import tensorflow as tf
import json

def write_D(data_L,file):
    data = data_L.tolist()
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

# Load the MNIST dataset
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize pixel values to be between 0 and 1
X_train, X_test = X_train / 255.0, X_test / 255.0

print(f"Training data shape: {X_train.shape}")
print(f"Test data shape: {X_test.shape}")

write_D(X_test,"test.json")
write_D(X_train,"train.json")
print("Data download finished")
