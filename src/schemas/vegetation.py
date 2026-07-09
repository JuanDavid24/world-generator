from pydantic import BaseModel

class Vegetation_from_id_params(BaseModel): 
  iteraitons: int
  seed: bool | None = None