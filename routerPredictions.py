import pickle
from fastapi import APIRouter, FastAPI
import numpy as np

from interfacaes import dfdata


router = APIRouter()

with open("RFDiabetesv132.pkl","rb") as file:
    model=pickle.load(file)

labels = ["Paciente Sano","Paciente Diabetico"]
@router.get("/")
def index():
    return {"Mensaje":"API 2 running"}

@router.post("/predict")
def predict(data: dfdata):
    data = data.model_dump()
    print(data)

    Pregnancies	= data["Pregnancies"]
    Glucose= data["Glucose"]
    BloodPressure= data["BloodPressure"]
    SkinThickness= data["SkinThickness"]
    Insulin= data["Insulin"]
    BMI= data["BMI"]
    DiabetesPedigreeFunction= data["DiabetesPedigreeFunction"]
    Age = data["Age"]

    xin = np.array([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]).reshape(1,8)
    prediction = model.predict(xin)
    print(labels[prediction[0]])
    return{labels[prediction[0]]}

if __name__=="__name__":
    router.run()