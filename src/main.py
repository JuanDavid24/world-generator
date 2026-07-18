from fastapi import FastAPI
from routers import terrain, vegetation
from fastapi.middleware.cors import CORSMiddleware
  
app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(terrain.router)
app.include_router(vegetation.router)

@app.get("/")
def read_root():
  return {"message": "Servidor de generación procedural de mundos"}