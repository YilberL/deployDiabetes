from fastapi import FastAPI

import routerPredictions

app = FastAPI()
app.include_router(routerPredictions.router)

if __name__=="__name__":
    app.run()