from pathlib import Path
from fastai.basic_train import load_learner
from fastai.vision import open_image
from io import BytesIO

path = Path('./model')
learner = None

classes = ['Araneus-Diadematus',
 'Araniella-Cucurbitina',
 'Eratigena-Atrica',
 'Pholcidae',
 'Salticus-Scenicus',
 'Steatoda-Nobilis',
 'Tegenaria-Domestica',
 'Zygiella-X-Notata']

def init():
    print("loading learner from model...")
    global learner
    learner = load_learner(path)
    print("loaded learner")

def predict_image(img):
    prediction = learner.predict(img)
    print("\n\n\n######## prediction:")
    print(prediction)
    return prediction

def predict_from_bytes(bytes):
    img = open_image(BytesIO(bytes))
    return predict_image(img)