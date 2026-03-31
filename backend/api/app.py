from fastapi import FastAPI, File, UploadFile
from Dl import preprocess
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    contents = await file.read()
    result = preprocess(contents)
    return {"result": result}

    