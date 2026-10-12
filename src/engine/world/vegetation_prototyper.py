from dataclasses import dataclass

import engine.vegetation.l_systems as lsys
import engine.vegetation.data.lsys_examples as data
 
@dataclass
class Plant_variant:
    default_angle: int | None = None
    angle_variation: int = 0
    weight: int = 1
    
@dataclass
class Plant_genes:
    lsys_id: str
    iterations: int
    variants: list[Plant_variant]
    seed: int | None = None
    weight: int = 1
    
    
@dataclass
class Plant_prototype:
    genes: Plant_genes
    lsys_output: str
    probability: float | None = None
    id: str | None = None
    
    # creates prototype id and variant ids
    def crete_ids(self):
        self.create_id()
        self.create_variant_ids()
    
    # creates prototype id from genes available data as: {l_system_name}_{number_of_iterations}_{seed}
    def create_id(self):
        id_fixed = self.genes.lsys_id + self.genes.iterations
        id_seed = "" if self.seed is None else str(self.seed)
        self.id = id_fixed + id_seed
    
    # creates ids for plant variants as: {prototype_id}_{variant_index}
    def create_variant_ids(self):
        for i, variant in enumerate(self.genes.variants):
            variant.id = self.id + str(i)

dataclass
class Plant_pool:
    prototypes: list[Plant_prototype] = []
    roll_thresholds: list[float] = []
    
@dataclass
class Vegetation_prototyper:
    species: list[Plant_genes]
    
    # def __post_init__(self):
    #     self.calculate_probability_offset()
        
    def calculate_probability_offset():
        self.prob_max_deviation = 1 / len(genes) * .25
    
    def generate_pool(self):
        self.pool = Plant_pool()
        
        for genes in self.species:
            new_protoype = self.generate_prototype(genes)
            self.pool.append(new_protoype)
    
    def generate_prototype(self, genes):
        lsys_output = self.generate_lsys_for_genes(genes)
        return Plant_prototype(genes, lsys_output)
    
    # def get_lsys_data(self, genes):
    #     # get lsys from dataset
    #     lsys_data = 
    #     return lsys_data
    
        
    def generate_lsys_for_genes(self, genes):
        # get lsys from dataset
        lsys_data = data.get_lsys_by_id(genes.lsys_id)
        
        # generate lsys output sentence
        lsys_output, output_seed = lsys.sentence_generator(lsys_data["axiom"], lsys_data["ruleset"], genes.iterations, genes.seed)
        
        # ensure genes seed is updated
        self.update_seed(genes, lsys_data, output_seed)
        
        # update variants
        self.complete_data_of_variants_if_missing(genes, lsys_data)
        
        # # create genes and variants ids with updated seed
        # genes.crete_ids()
        return lsys_output
    
    def update_seed(self, genes, lsys_data, output_seed):
        genes.seed = output_seed if lsys_data["stochastic"] else None
        
    def complete_data_of_variants_if_missing(self, genes, lsys_data):
        for variant in genes.variants:
            # default_angle assignation
            if variant.default_angle is None:
                variant.default_angle = lsys_data["default_angle"]
        
