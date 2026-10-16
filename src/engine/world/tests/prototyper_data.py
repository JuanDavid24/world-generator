import copy

from engine.world.vegetation_prototyper import Plant_genes, Plant_variant

# dataset for plant prototypes, genes, variants

# ----- variants -----
VARIANT_ANGLES = Plant_variant(default_angle=24, angle_variation=3)
VARIANT_NO_DEF_ANGLE = Plant_variant(default_angle=24)
VARIANT_NO_VAR_ANGLE = Plant_variant(angle_variation=3)
VARIANT_WEIGHT_2 = Plant_variant(default_angle=24, angle_variation=3, weight=2)

VARIANTS = [VARIANT_ANGLES, VARIANT_NO_DEF_ANGLE, VARIANT_NO_VAR_ANGLE, VARIANT_WEIGHT_2]

# ----- genes -----
GENES_FULL = Plant_genes(lsys_id="dense_bush", iterations=3, seed=123, weight=2, variants=copy.deepcopy(VARIANTS))
GENES_NO_SEED = Plant_genes(lsys_id="dense_bush", iterations=3, weight=2, variants=copy.deepcopy(VARIANTS))
GENES_SINGLE_VARIANT = Plant_genes(lsys_id="dense_bush", iterations=2, weight=1, variants=[copy.deepcopy(VARIANTS[0])])
GENES_STOCHASTIC_SEED= Plant_genes(lsys_id="dense_bush_sto", iterations=3, seed=123, weight=2, variants=copy.deepcopy(VARIANTS))

# list of mock genes with valid data
GENES_DATA_OK = [GENES_FULL, GENES_NO_SEED, GENES_SINGLE_VARIANT, GENES_STOCHASTIC_SEED]
