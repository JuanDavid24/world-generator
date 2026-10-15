import numpy as np 
import pytest

from engine.world.vegetation_prototyper import Vegetation_prototyper, Plant_genes, Plant_variant, Plant_prototype, Plant_pool, Plant_result 
import engine.vegetation.l_systems as lsys
import engine.vegetation.data.lsys_examples as data

# --- dataset ---
VARIANT_ANGLES = Plant_variant(default_angle=24, angle_variation=3)
VARIANT_NO_DEF_ANGLE = Plant_variant(default_angle=24)
VARIANT_NO_VAR_ANGLE = Plant_variant(angle_variation=3)
VARIANT_WEIGHT_2 = Plant_variant(default_angle=24, angle_variation=3, weight=2)

VARIANTS = [VARIANT_ANGLES, VARIANT_NO_DEF_ANGLE, VARIANT_NO_VAR_ANGLE, VARIANT_WEIGHT_2]

GENES_FULL = Plant_genes(lsys_id="dense_bush", iterations=3, seed=123, weight=2, variants=VARIANTS)
GENES_NO_SEED = Plant_genes(lsys_id="dense_bush", iterations=3, weight=2, variants=VARIANTS)
GENES_SINGLE_VARIANT = Plant_genes(lsys_id="dense_bush", iterations=2, weight=1, variants=[VARIANTS[0]])
GENES_STOCHASTIC_SEED= Plant_genes(lsys_id="dense_bush_sto", iterations=3, seed=123, weight=2, variants=VARIANTS)

# list of mock genes with valid data
GENES_DATA_OK = [GENES_FULL, GENES_NO_SEED, GENES_SINGLE_VARIANT, GENES_STOCHASTIC_SEED]

# --- fixtures ---
@pytest.fixture
def prototyper():
    return Vegetation_prototyper(GENES_DATA_OK)

@pytest.fixture
def lsys_output_expected():
    lsys_data = data.get_lsys_by_id(GENES_FULL.lsys_id)
    lsys_output_expected, _ = lsys.sentence_generator(lsys_data["axiom"], lsys_data["ruleset"], n=GENES_FULL.iterations, seed=GENES_FULL.seed)
    return lsys_output_expected

@pytest.fixture
def pool(prototyper):
    prototyper.generate_pool()
    return prototyper.pool

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
    expected_prototype_id_seed = "" if GENES_FULL.seed is None else ("_" + str(GENES_FULL.seed))
    expected_prototype_id = GENES_FULL.lsys_id + "_" + str(GENES_FULL.iterations) + expected_prototype_id_seed
    assert prototype.id == expected_prototype_id
    
    # assert variant ids
    for i in range(len(GENES_FULL.variants)):
        expected_var_id = expected_prototype_id + "_" + str(i)
        variany_id = prototype.genes.variants[i].id
        assert variany_id == expected_var_id
        
def test_generate_pool(prototyper, pool):
    for i in range(len(pool.prototypes)):
        prototype = pool.prototypes[i]
        assert prototyper.species[i] == prototype.genes
        
def test_pool_initialization(pool):
    # check pool weight sum
    expected_sum = 0
    for p in pool.prototypes:
        expected_sum += p.genes.weight
    assert pool.weight_sum == expected_sum
    
    # check rng
    assert isinstance(pool.rng, np.random._generator.Generator) 
    
def test_pool(pool):
    # check random index picking
    RANDS = [0, 2, 3, 5]
    # expected index results = [0, 1, 2, 3]
    # variant weights = [1, 1, 1, 2]
    for i in range(len(RANDS)):
        found_index = pool.pick_item_index_weighted(RANDS[i], VARIANTS)
        expected_index = i # expected index results = [0, 1, 2, 3]
        assert found_index == expected_index
        
    # check get random plant
    output_plant = pool.get_random_plant()
    assert output_plant.prototype.genes in GENES_DATA_OK
    
    # check variant index in range
    variant_index_range = range(len(output_plant.prototype.genes.variants))
    assert output_plant.variant_index in variant_index_range
    