from fastapi import FastAPI
from routers import terrain, vegetation
  
app = FastAPI()

app.include_router(terrain.router)
app.include_router(vegetation.router)

@app.get("/")
def read_root():
  return {"message": "Servidor de generación procedural de mundos"}