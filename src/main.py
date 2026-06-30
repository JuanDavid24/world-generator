from fastapi import FastAPI
from pydantic import BaseModel
from terrain.terrain_generator import perlin_map

class Perlin_params(BaseModel): 
  seed: int | None = None
  size: int
  scale: int | None = 100
  octaves: int | None = 1
  persistence: float | None = 0.5
  lacunarity: float | None = 2
  
app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "Servidor de generación procedural de mundos"}

@app.post("/terrain/perlin")
async def create_terrain_perlin(args: Perlin_params):
  args_dict = args.model_dump()
  args_dict["shape"] = (args.size, args.size)
  args_dict.pop("size")
  
  map, seed = perlin_map(**args_dict, debug=True)
  args_dict["seed"] = seed
  return {"Perlin params": args}