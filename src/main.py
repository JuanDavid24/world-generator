from fastapi import FastAPI
from routers import terrain
  
app = FastAPI()

app.include_router(terrain.router)

@app.get("/")
def read_root():
  return {"message": "Servidor de generación procedural de mundos"}