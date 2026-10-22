from pydantic import BaseModel
from .terrain import Perlin_params, Diamond_square_params
from engine.world.vegetation_prototyper import Plant_genes

class Terrain_Params(BaseModel):
    algorithm: str
    params: Perlin_params | Diamond_square_params
    
class Vegetation_Params(BaseModel):
    genes: list[Plant_genes]
    
class World_Params(BaseModel):
    terrain: Terrain_Params
    vegetation: Vegetation_Params