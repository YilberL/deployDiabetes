from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routerPredictions

app = FastAPI()
app.include_router(routerPredictions.router)

app.add_middleware(
    CORSMiddleware, # type: ignore
    allow_origins=["*"],  # Puedes cambiar "*" por ["http://127.0.0.1:5500&quot;] si quieres más seguridad
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

if __name__=="__name__":
    app.run()