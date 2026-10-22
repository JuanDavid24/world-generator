from fastapi import APIRouter

from schemas.world import WorldParams, TerrainParams, VegetationParams
from services.world import process_world

router = APIRouter(
    prefix="/world"
)

@router.post("/")
async def world_route(terrain: TerrainParams, vegetation: VegetationParams):
    terrain_args = terrain.model_dump()  # model to dict
    vegetation_args = vegetation # model to dict

    res_data = process_world(terrain_args, vegetation_args)
    return res_data