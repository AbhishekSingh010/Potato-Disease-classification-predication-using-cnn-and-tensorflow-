from fastapi import FastAPI, File, UploadFile, Request
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Load the pre-trained model
Model = tf.keras.models.load_model("./saved_models/1")
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

frontend_folder = "./frontend"
templates = Jinja2Templates(directory=os.path.join(frontend_folder, "templates"))

# Function to read uploaded image as an ndarray
def read_files_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "prediction": None})

@app.post("/predict")
async def predict(request: Request, file: UploadFile = File(...)):
    image = read_files_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    prediction = Model.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = 100 * float(np.max(prediction[0]))

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "prediction": {"class": predicted_class, "confidence": confidence}},
    )

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8001)
