from tensorflow.keras import layers, models

def modelv1(
    modelName,
    train_data,
    val_data,
    filter_sizes=[64, 128],
    last_layers=[(128, 'relu'), (3, 'softmax')],
    lossfunction="sparse_categorical_crossentropy"
):
    model = models.Sequential()
    # First layer
    model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3)))
    model.add(layers.MaxPooling2D())
    # Dynamic conv layers
    for f in filter_sizes:
        model.add(layers.Conv2D(f, (3,3), activation='relu'))
        model.add(layers.MaxPooling2D())
    # Flatten
    model.add(layers.Flatten())
    # Dynamic dense layers
    for neurons, act in last_layers:
        model.add(layers.Dense(neurons, activation=act))
    # Compile
    model.compile(
        optimizer='adam',
        loss=lossfunction,
        metrics=['accuracy']
    )
    # Train
    model.fit(
        train_data,
        validation_data=val_data,
        epochs=5
    )
    # Save
    model.save(f"{modelName}.h5")
