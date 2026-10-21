from dataclasses import dataclass, field, asdict
import numpy as np

from .spawner import Spawner
from .vegetation_prototyper import Plant_pool

@dataclass
class Vegetation_assembler:
    spawner: Spawner
    pool: Plant_pool
    prototypes_payload: dict = field(default_factory=dict)
    instances_payload: dict = field(default_factory=dict)
    
    def __post_init__(self):
        self.initialize_dictionaries()
        self.populate_instances()
        
    def initialize_dictionaries(self):
        for proto in self.pool.prototypes:
            # prototypes payload initialization
            variants = proto.genes.variants_to_dict()
            
            self.prototypes_payload[proto.id] = {
                "metadata": {
                    "algorithm": "l_system",
                    "type": "determinist",                    
                    "size": len(proto.lsys_output)
                },
                "genes": proto.genes.to_dict(),
                "variants": variants,
                "sentence": proto.lsys_output
            }
            
            # instances payload initialization
            for v in variants:
                variant_id = v["id"]
                self.instances_payload[variant_id] = {
                        "count": 0,
                        "positions": [],
                        "normals": [],
                        "yaws": [],
                        "scales": []
                    }
    
    def populate_instances(self):
        xs = self.spawner.spawn_positions_x
        ys = self.spawner.spawn_positions_y
        zs = self.spawner.spawn_positions_h

        for (x, y, z) in zip(xs, ys, zs):
            # get random plant
            plant = self.pool.get_random_plant()
            
            # get variant id
            variant_id = plant.prototype.genes.variants[plant.variant_index].id
            
            # calculate normal            
            normal = [0.0, 1.0, 0.0]    # placeholder
            
            # calculate random yaw and scale    
            rng = self.pool.rng     # use pool rng
            yaw = rng.uniform(0, 2 * np.pi)         
            scale = rng.uniform(0.85, 1.15)
            
            # save results in instances payload
            self.instances_payload[variant_id]["count"] += 1
            self.instances_payload[variant_id]["positions"].extend([x, y, z])
            self.instances_payload[variant_id]["normals"].extend(normal)
            self.instances_payload[variant_id]["yaws"].append(yaw)
            self.instances_payload[variant_id]["scales"].append(scale)