import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Cache models (IMPORTANT for FastAPI performance)
MODEL_CACHE = {}

def load_model(modelname):
    if modelname not in MODEL_CACHE:
        MODEL_CACHE[modelname] = tf.keras.models.load_model(f"{modelname}.h5")
    return MODEL_CACHE[modelname]


def process(img_path=None, imarr=None):
    if img_path:
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        return img_array
    elif imarr is not None:
        img_array = imarr
        return imarr
    else:
        return None

    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


# ✅ 1. Leaf Detection
def isLeaf(modelname, img_path=None, imarr=None):
    img = process(img_path, imarr)
    if img is None:
        return False

    model = load_model(modelname)

    pred = model.predict(img)[0][0]
    return bool(pred < 0.5)


# ✅ 2. Supported Plant Check
def isSupportedPlant(modelname, img_path=None, imarr=None):
    img = process(img_path, imarr)
    if img is None:
        return False

    model = load_model(modelname)

    pred = model.predict(img)
    plant_conf = float(np.max(pred))
    print("he",plant_conf)

    return plant_conf


# ✅ 3. Disease Prediction
def plantDisease(modelname, img_path=None, imarr=None):
    img = process(img_path, imarr)
    if img is None:
        return "not found"
    model = load_model(modelname)

    pred = model.predict(img)
    class_id = int(np.argmax(pred))
    disease_conf = float(np.max(pred))
    print()
    
    # optional class names
    if hasattr(model, "class_names"):
        return {
            "disease": model.class_names[class_id],
            "confidence": disease_conf
        }

    return {
        "class_id": class_id,
        "confidence": disease_conf
    }