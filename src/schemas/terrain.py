from pydantic import BaseModel

class Perlin_params(BaseModel): 
  seed: int | None = None
  size: int
  scale: int | None = 100
  octaves: int | None = 1
  persistence: float | None = 0.5
  lacunarity: float | None = 2
  
class Diamond_square_params(BaseModel): 
  seed: int | None = None
  n: int
  initial_corners: list[float] | None = None
  roughness: float | None = 1.0
  wrap: bool | None = False