from fastapi import APIRouter

from schemas.vegetation import Vegetation_from_id_params
# from services.terrain import process_perlin_terrain, process_diamond_square_terrain
  
router = APIRouter(
    prefix="/vegetation"
)

@router.post("/{id}")
async def vegetation_from_id_route(req_body: Vegetation_from_id_params):
    veg_params = req_body.model_dump()