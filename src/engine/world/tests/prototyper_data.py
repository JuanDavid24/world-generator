import copy

from engine.world.vegetation_prototyper import PlantGenes, PlantVariant

# dataset for plant prototypes, genes, variants

# ----- variants -----
VARIANT_ANGLES = PlantVariant(default_angle=24, angle_variation=3)
VARIANT_NO_DEF_ANGLE = PlantVariant(default_angle=24)
VARIANT_NO_VAR_ANGLE = PlantVariant(angle_variation=3)
VARIANT_WEIGHT_2 = PlantVariant(default_angle=24, angle_variation=3, weight=2)

VARIANTS = [VARIANT_ANGLES, VARIANT_NO_DEF_ANGLE, VARIANT_NO_VAR_ANGLE, VARIANT_WEIGHT_2]

# ----- genes -----
GENES_FULL = PlantGenes(lsys_id="dense_bush", iterations=3, seed=123, weight=2, variants=copy.deepcopy(VARIANTS))
GENES_NO_SEED = PlantGenes(lsys_id="dense_bush", iterations=3, weight=2, variants=copy.deepcopy(VARIANTS))
GENES_SINGLE_VARIANT = PlantGenes(lsys_id="dense_bush", iterations=2, weight=1, variants=[copy.deepcopy(VARIANTS[0])])
GENES_STOCHASTIC_SEED= PlantGenes(lsys_id="dense_bush_sto", iterations=3, seed=123, weight=2, variants=copy.deepcopy(VARIANTS))

# list of mock genes with valid data
GENES_DATA_OK = [GENES_FULL, GENES_NO_SEED, GENES_SINGLE_VARIANT, GENES_STOCHASTIC_SEED]
