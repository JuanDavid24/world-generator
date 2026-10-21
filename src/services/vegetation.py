from engine.vegetation.data.lsys_examples import lsys_dataset
from engine.vegetation.l_systems import sentence_generator
from utils.logger import format_plant_data, log_plant_to_json

def process_plant_from_id(id, iterations, seed, debug=False):
    if not id in lsys_dataset:
        return None
    
    lsys = lsys_dataset[id]
    generated_plant, seed = sentence_generator(lsys["axiom"], lsys["ruleset"], iterations, seed)
    plant_data = format_plant_data(lsys, iterations, seed, generated_plant, id)
    
    if debug:
        log_plant_to_json(lsys, iterations, seed, generated_plant)
    return plant_data
