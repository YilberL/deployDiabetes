from pydantic import BaseModel

class dfdata(BaseModel):
    Pregnancies	: int
    Glucose: float
    BloodPressure: float
    SkinThickness: int
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int