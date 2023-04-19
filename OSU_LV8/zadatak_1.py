import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix


# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# train i test podaci
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# prikaz karakteristika train i test podataka
print('Train: X=%s, y=%s' % (x_train.shape, y_train.shape))
print('Test: X=%s, y=%s' % (x_test.shape, y_test.shape))

# TODO: prikazi nekoliko slika iz train skupa
fig, axes = plt.subplots(3, 3, figsize=(10, 10))
axes = axes.ravel()
for i in range(9):      # 9 slika
    axes[i].imshow(x_train[i], cmap='gray')
    axes[i].axis('off')
plt.subplots_adjust(wspace=0.5)
plt.show()


# skaliranje slike na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# slike trebaju biti (28, 28, 1)
x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

print("x_train shape:", x_train_s.shape)
print(x_train_s.shape[0], "train samples")
print(x_test_s.shape[0], "test samples")


# pretvori labele
y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)


# TODO: kreiraj model pomocu keras.Sequential(); prikazi njegovu strukturu
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())  # umjesto 28x28 matrice kao ulaz, stavljamo array od 784 bita
model.add(tf.keras.layers.Dense(100, activation=tf.nn.relu))    # 100 neurona i relu funkcija
model.add(tf.keras.layers.Dense(50, activation=tf.nn.relu))     # 50 neurona i relu funkcija
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))  # 10 neurona zbog 10 mogucih brojeva i softmax


# TODO: definiraj karakteristike procesa ucenja pomocu .compile()
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# TODO: provedi ucenje mreze
model.fit(x_train, y_train, epochs=5)

# TODO: Prikazi test accuracy i matricu zabune
test_loss, test_acc = model.evaluate(x_test_s, y_test_s, verbose=2)
print("Test accuracy:", test_acc)

y_pred = model.predict(x_test_s)
y_pred = np.argmax(y_pred, axis=1)
cm = confusion_matrix(y_test, y_pred)
print("Confusion matrix:\n", cm)

# TODO: spremi model
model.save("net.h5")
