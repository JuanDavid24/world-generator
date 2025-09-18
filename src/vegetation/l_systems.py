import numpy as np

def sentence_generator(axiom, ruleset, n, seed=None):
    if not check_lsys_ruleset(ruleset):
        raise Exception("La suma de las probabilidades de las reglas de cada simbolo debe ser 1")
    if seed is None:
        seed = np.random.randint(0, 2**31)
    rng = np.random.default_rng(seed)
    for _ in range(n):
        sentence = ""
        for symbol in axiom:
            if symbol in ruleset:
                symbol_rules = ruleset[symbol]
                sentence += apply_rule(symbol_rules, rng)                    
            else: 
                sentence += symbol
        axiom = sentence
    return sentence, seed

def apply_rule(ruleset, rng):
    rand_value = rng.random()
    prob_acc = 0
    for (successor, prob) in ruleset:
        # unica regla
        if prob == 1: 
            return successor
        prob_acc += prob
        if rand_value <= prob_acc:
            return successor

def check_lsys_ruleset(ruleset):
    for symbol_rules in ruleset.values():
        if not symbol_ruleset_prob_ok(symbol_rules):
            return False
    return True
        
def symbol_ruleset_prob_ok(ruleset):
    prob_sum = 0
    for (_, prob) in ruleset:
        prob_sum += prob
    return prob_sum == 1
