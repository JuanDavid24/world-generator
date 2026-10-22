import numpy as np 
import pytest

import engine.world.tests.prototyper_data as pd
import engine.vegetation.data.lsys_examples as data
import engine.vegetation.l_systems as lsys
from engine.world.vegetation_prototyper import VegetationPrototyper

# --- fixtures ---
@pytest.fixture
def prototyper():
    return VegetationPrototyper(pd.GENES_DATA_OK)

@pytest.fixture
def lsys_output_expected():
    lsys_data = data.get_lsys_by_id(pd.GENES_FULL.lsys_id)
    lsys_output_expected, _ = lsys.sentence_generator(lsys_data["axiom"], lsys_data["ruleset"], n=pd.GENES_FULL.iterations, seed=pd.GENES_FULL.seed)
    return lsys_output_expected

@pytest.fixture
def pool(prototyper):
    prototyper.generate_pool()
    return prototyper.pool

# --- tests ---
def test_generate_lsys(prototyper, lsys_output_expected):
    lsys_output = prototyper.generate_lsys_for_genes(pd.GENES_FULL)
    
    assert lsys_output == lsys_output_expected
    
def test_generate_prototype(prototyper, lsys_output_expected):
    prototype = prototyper.generate_prototype(pd.GENES_FULL)
    assert prototype.genes == pd.GENES_FULL
    
    # assert prototype lsys output
    assert prototype.lsys_output == lsys_output_expected
    
    # assert prototype id
    expected_prototype_id_seed = "" if pd.GENES_FULL.seed is None else ("_" + str(pd.GENES_FULL.seed))
    expected_prototype_id = pd.GENES_FULL.lsys_id + "_" + str(pd.GENES_FULL.iterations) + expected_prototype_id_seed
    assert prototype.id == expected_prototype_id
    
    # assert variant probs sum be equal to 1
    probs_sum = sum(prototype.variant_probs)
    assert np.isclose(probs_sum, 1)
    
    # check variant probs calculation
    variants = prototype.genes.variants
    weights = np.array([v.weight for v in variants])
    check_probs_with_weights(prototype.variant_probs, weights)
    
    # check variant ids
    for i in range(len(pd.GENES_FULL.variants)):
        expected_var_id = expected_prototype_id + "_" + str(i)
        variany_id = prototype.genes.variants[i].id
        assert variany_id == expected_var_id
   
# aux function to check list of probabilities against weights
def check_probs_with_weights(probs, weights):
    weight_sum = sum(weights)
    for i, prob in enumerate(probs):
        expected_prob = weights[i] / weight_sum
        assert np.isclose(prob, expected_prob)
        
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
    
    # assert prototype probs sum be equal to 1
    probs_sum = sum(pool.prototype_probs)
    assert np.isclose(probs_sum, 1)
    
    # check variant probs calculation
    prototypes = pool.prototypes
    weights = np.array([prot.genes.weight for prot in prototypes])
    check_probs_with_weights(pool.prototype_probs, weights)
     
def test_pool(pool):
    # check random index picking
    RANDS = [0, 2, 3, 5]
    # expected index results = [0, 1, 2, 3]
    # variant weights = [1, 1, 1, 2]
        
    # check get random plant
    output_plant = pool.get_random_plant()
    assert output_plant.prototype.genes in pd.GENES_DATA_OK
    
    # check variant index in range
    variant_index_range = range(len(output_plant.prototype.genes.variants))
    assert output_plant.variant_index in variant_index_range
    