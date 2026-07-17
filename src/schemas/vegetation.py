from pydantic import BaseModel

class Vegetation_from_id_params(BaseModel): 
  iterations: int
  seed: bool | None = None