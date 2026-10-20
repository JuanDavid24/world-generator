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
        
    def initialize_dictionaries(self):
        for proto in self.pool.prototypes:
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
                
        # for v in proto.genes.variants:
        #     self.prototypes_payload[proto.id]["variants"].append(
        #         asdict(v)
        #     )