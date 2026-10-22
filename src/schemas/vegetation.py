from pydantic import BaseModel

class VegetationFromIDParams(BaseModel): 
  iterations: int
  seed: bool | None = None