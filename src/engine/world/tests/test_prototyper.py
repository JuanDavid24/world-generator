import numpy as np 
import pytest

from engine.world.vegetation_prototyper import Vegetation_prototyper, Plant_genes, Plant_variant, Plant_prototype
import engine.vegetation.l_systems as lsys
import engine.vegetation.data.lsys_examples as data

# --- dataset ---
VARIANTS = [
    Plant_variant(default_angle=24, angle_variation=3),
    Plant_variant(angle_variation=3),
    Plant_variant(default_angle=24)
]

GENES_FULL = Plant_genes(lsys_id="dense_bush", iterations=3, seed=123, weight=2, variants=VARIANTS)
GENES_NO_SEED = Plant_genes(lsys_id="dense_bush", iterations=3, weight=2, variants=VARIANTS)

# list of mock genes with valid data
GENES_DATA_OK = [GENES_FULL, GENES_NO_SEED]

# --- fixtures ---
@pytest.fixture
def prototyper():
    return Vegetation_prototyper(GENES_DATA_OK)

@pytest.fixture
def lsys_output_expected():
    lsys_data = data.get_lsys_by_id(GENES_FULL.lsys_id)
    lsys_output_expected, _ = lsys.sentence_generator(lsys_data["axiom"], lsys_data["ruleset"], n=GENES_FULL.iterations, seed=GENES_FULL.seed)
    return lsys_output_expected

# --- tests ---
def test_generate_lsys(prototyper, lsys_output_expected):
    lsys_output = prototyper.generate_lsys_for_genes(GENES_FULL)
    
    assert lsys_output == lsys_output_expected
    
def test_generate_prototype(prototyper, lsys_output_expected):
    prototype = prototyper.generate_prototype(GENES_FULL)
    assert prototype.genes == GENES_FULL
    
    # assert prototype lsys output
    assert prototype.lsys_output == lsys_output_expected
    
    # assert prototype id
    expected_prototype_id = GENES_FULL.lsys_id + str(GENES_FULL.iterations)
    assert prototype.id == expected_prototype_id
    
    # assert variant ids
    for i in range(len(GENES_FULL.variants)):
        expected_var_id = expected_prototype_id + str(i)
        variany_id = prototype.genes.variants[i].id
        assert variany_id == expected_var_id