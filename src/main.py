from fastapi import FastAPI
from pydantic import BaseModel
from terrain.terrain_generator import perlin_map, diamond_square_map
from utils.logger import format_terrain_data

class Perlin_params(BaseModel): 
  seed: int | None = None
  size: int
  scale: int | None = 100
  octaves: int | None = 1
  persistence: float | None = 0.5
  lacunarity: float | None = 2
  
class Diamond_square_params(BaseModel): 
  seed: int | None = None
  n: int
  initial_corners: list[float] | None = None
  roughness: int | None = 1
  wrap: bool | None = False
  
app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "Servidor de generación procedural de mundos"}

@app.post("/terrain/perlin")
async def create_terrain_perlin(args: Perlin_params):
  terrain_args = args.model_dump()  # model to dict
  terrain_args["shape"] = (args.size, args.size)
  terrain_args.pop("size")  # not needed for perlin_map function
  
  map, seed = perlin_map(**terrain_args, debug=True)
  terrain_args.update({"seed": seed}) # update seed if not given in req
  
  res_data = format_terrain_data(algorithm="perlin_noise", map=map, size=args.size, **terrain_args)

  return res_data

@app.post("/terrain/diamond-square")
async def create_terrain_diamond_square(args: Diamond_square_params):
  terrain_args = args.model_dump()  # model to dict
  
  map, seed, corners = diamond_square_map(**terrain_args, debug=True)
  
  # update dict
  terrain_args.update({"seed": seed})  # update seed if not given in req
  terrain_args.update({"initial_corners": corners}) # update initial_corners if not given in req
  terrain_args.update({"size": 2**args.n + 1}) 
  
  res_data = format_terrain_data(algorithm="diamond_square", map=map, **terrain_args)

  return res_data