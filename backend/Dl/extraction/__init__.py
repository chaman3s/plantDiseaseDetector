import tensorflow as tf
import cv2
import os
import shutil
def dataLoader(urlData="Dl/data"):
    train_data = tf.keras.preprocessing.image_dataset_from_directory(
        urlData,
        image_size=(224, 224),
        batch_size=32,
        validation_split=0.2,
        subset="training",
        seed=42
    )
    val_data = tf.keras.preprocessing.image_dataset_from_directory(
        urlData,
        image_size=(224, 224),
        batch_size=32,
        validation_split=0.2,
        subset="validation",
        seed=42
    )
    # ✅ SAVE BEFORE MAP
    class_names = train_data.class_names
    # normalize
    train_data = train_data.map(lambda x, y: (x / 255.0, y))
    val_data = val_data.map(lambda x, y: (x / 255.0, y))
    return train_data,val_data,class_names
def cleandataSet(arrplant=["Apple","Blueberry","Cherry","Corn","Grape","Orange","Peach","Pepper","Potato","Raspberry","Soybean","Squash","Strawberry","Tomato"]):
    src = "Dl/data/leaf"
    dst = "Dl/plant_data"
    os.makedirs(dst, exist_ok=True)
    for folder in os.listdir(src):
        plant_name = folder.split("___")[0]
        plant = plant_name.lower()
        plant_folder = os.path.join(dst, plant)
        os.makedirs(plant_folder, exist_ok=True)
        for img in os.listdir(os.path.join(src, folder)):
            src_path = os.path.join(src, folder, img)
            dst_path = os.path.join(plant_folder, img)
            shutil.copy(src_path, dst_path)


