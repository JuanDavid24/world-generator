from fastapi import APIRouter

from schemas.vegetation import Vegetation_from_id_params
from services.vegetation import process_plant_from_id
  
router = APIRouter(
    prefix="/vegetation"
)

@router.post("/{id}")
async def vegetation_from_id_route(id: str, req_body: Vegetation_from_id_params):
    veg_params = req_body.model_dump() # modele to dict
    res_data = process_plant_from_id(id, **veg_params)
    
    return res_data