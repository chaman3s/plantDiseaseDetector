from .model import modelv1
from PIL import Image
import numpy as np
import io
from .extraction import dataLoader
from .validator.validateImage import isvalidImage
from .validator.check_leaf import isLeaf,isSupportedPlant,plantDisease
def preprocess_image(file_bytes):
    image = Image.open(io.BytesIO(file_bytes)).convert("RGB").resize((224,224))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array
def preprocess(content):
    imgarr=preprocess_image(content)
    if isvalidImage(content):
        result=isSupportedPlant(modelname="VerifyLeaf",imarr=imgarr)
        print(result)
        return result

    #     if result:
    #         return plantDisease(modelname="disease_model",imarr=imgarr)
    #     else:
    #         return "not supported plant"
    # else:
    #     return "not valid  image"
            

if __name__ == "__main__": 
    # train_data,val_data,class_names=dataLoader()
    # modelv1("isleafOrNot",train_data,val_data)
#     train_data,val_data,class_names=dataLoader(urlData="Dl/data/leaf")
#     modelv1(
#     modelName="disease_model",
#     train_data=train_data,
#     val_data=val_data,
#     filter_sizes=[64, 128, 256],
#     last_layers=[
#         (128, 'relu'),
#         (len(class_names), 'softmax')   # 🔥 IMPORTANT
#     ],
#     lossfunction="sparse_categorical_crossentropy"
# )   
    preprocess("Dl/blur.jpg")