import numpy as np 
import pytest

import engine.world.tests.prototyper_data as pd
from engine.world.vegetation_assembler import Vegetation_assembler
from .test_spawner import dynamic_spawner, multi_terrain, multi_vegetation
from .test_prototyper import pool, prototyper

# --- fixtures ---
@pytest.fixture
def assembler(dynamic_spawner, pool):
    dynamic_spawner.create_spawn_map()
    dynamic_spawner.get_spawn_positions()
    return Vegetation_assembler(dynamic_spawner, pool)

# --- tests ---
def test_initialize_dictionaries(assembler, pool):
    for p in pool.prototypes:
        # check prototype id exists as key in instances dict
        assert p.id in assembler.prototypes_payload
        
        # check variant count
        variant_count = len(assembler.prototypes_payload[p.id]["variants"])
        variant_count_expected = len(p.genes.variants)
        assert variant_count_expected == variant_count
        
        for v in p.genes.variants:
            # check variant id exists as key in instances dict
            assert v.id in assembler.instances_payload
            
def test_populate_instances(assembler):
    # count expected totals
    total_count = total_positions = total_normals = total_yaws = total_scales = 0 
    for key in assembler.instances_payload:
        total_count += assembler.instances_payload[key]["count"]
        total_positions += len(assembler.instances_payload[key]["positions"])
        total_normals += len(assembler.instances_payload[key]["normals"])
        total_yaws += len(assembler.instances_payload[key]["yaws"])
        total_scales += len(assembler.instances_payload[key]["scales"])
        
    # check items count of each flat array
    assert total_count == len(assembler.spawner.spawn_positions_x)
    assert total_positions == len(assembler.spawner.spawn_positions_x) * 3
    assert total_normals == len(assembler.spawner.spawn_positions_x) * 3 
    assert total_yaws == len(assembler.spawner.spawn_positions_x) 
    assert total_scales == len(assembler.spawner.spawn_positions_x) 
    
        
    