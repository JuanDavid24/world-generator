from fastapi import APIRouter

from schemas.terrain import Perlin_params, Diamond_square_params
from services.terrain import process_perlin_terrain, process_diamond_square_terrain
  
router = APIRouter(
    prefix="/terrain"
)

@router.post("/perlin")
async def perlin_map_route(args: Perlin_params):
  terrain_args = args.model_dump()  # model to dict
  res_data = process_perlin_terrain(**terrain_args, debug=True)
  
  return res_data

@router.post("/diamond-square")
async def diamond_square_map_route(req_body: Diamond_square_params):
  terrain_params = req_body.model_dump()  # model to dict
  res_data = process_diamond_square_terrain(**terrain_params, debug=True)

  return res_data