from fastapi import APIRouter

from schemas.world import World_Params, Terrain_Params, Vegetation_Params
from services.world import process_world

router = APIRouter(
    prefix="/world"
)

@router.post("/")
async def world_route(terrain: Terrain_Params, vegetation: Vegetation_Params):
    terrain_args = terrain.model_dump()  # model to dict
    vegetation_args = vegetation # model to dict

    res_data = process_world(terrain_args, vegetation_args)
    return res_data