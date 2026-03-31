from model import modelv1
from extraction import dataLoader
from validator import isvalidImage,isLeaf,isSupportedPlant,plantDisease
def preprocess(img_path):
    
    if isvalidImage(img_path):
        if isLeaf([img_path],"modelv1"):
            if isSupportedPlant(img_path,modelname="VerifyLeaf"):
                return plantDisease(img_path,modelname="disease_model")
            else:
                return "not supported plant"
        else:
            return "not leaf"
    else:
        return "not valid"
            

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