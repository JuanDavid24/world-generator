from pydantic import BaseModel
from .terrain import PerlinParams, DiamondSquareParams
from engine.world.vegetation_prototyper import PlantGenes
from engine.world.spawner import SpawnParams

class TerrainParams(BaseModel):
    algorithm: str
    params: PerlinParams | DiamondSquareParams
    
class VegetationParams(BaseModel):
    genes: list[PlantGenes]
    spawn: SpawnParams
    
class WorldParams(BaseModel):
    terrain: TerrainParams
    vegetation: VegetationParams