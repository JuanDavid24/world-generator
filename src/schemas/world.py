from pydantic import BaseModel
from .terrain import PerlinParams, DiamondSquareParams
from engine.world.vegetation_prototyper import PlantGenes

class TerrainParams(BaseModel):
    algorithm: str
    params: PerlinParams | DiamondSquareParams
    
class VegetationParams(BaseModel):
    genes: list[PlantGenes]
    
class WorldParams(BaseModel):
    terrain: TerrainParams
    vegetation: VegetationParams