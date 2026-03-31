import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
def process(img_path):
    img = image.load_img(img_path, target_size=(224,224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array
def isLeaf(Arrimage,modelname):
    result=[]
    
    model=tf.keras.models.load_model(f"Dl/{modelname}.h5")
    for i in Arrimage:
        img_array = process(i)
        img_array = image.img_to_array(img) / 255.0
        pred = model.predict(img_array)[0][0]
        if pred > 0.5:
            result.append(True)
        else:
            result.append(False)
    return result
def isSupportedPlant(imge_path,modelname):
    img=process(imge_path)
    model=tf.keras.models.load_model(f"Dl/{modelname}.h5")
    pred1 = model.predict(img)
    plant_id = pred1.argmax()
    plant_conf = pred1.max()
    if plant_conf <0.7:
        return False
    else:
        return True
def plantDisease(imge_path,modelname):
    img=process(imge_path)

    model=tf.keras.models.load_model(f"Dl/{modelname}.h5")
    disease_classes = model.class_names if hasattr(model, "class_names") else None
    pred = model.predict(img)
    class_id = pred.argmax()
    disease_conf = pred.max()
    if disease_classes:
        result = disease_classes[class_id]
        return result
    else:
        return "not found"