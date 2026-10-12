lsys_a = {
    "stochastic": False,
    "ruleset": {
        "F": [("F[+F]F[-F]F", 1)]
    },
    "axiom": "F"
}

lsys_a2 = {
    "stochastic": False,
    "ruleset": {
        "F": [("F[+FL]F[-FL]F", 1)]
    },
    "axiom": "F"
}

lsys_b = {
    "stochastic": False,
    "ruleset": {
        "F": [("F[+F]F[-F][F]", 1)]
    },
    "axiom": "F"
}

lsys_b2 = {
    "stochastic": False,
    "ruleset": {
        "F": [("F[+FL]F[-FL][FL]", 1)]
    },
    "axiom": "F"
}

lsys_c = {
    "stochastic": False,
    "ruleset": {
        "F": [("FF-[-F+F+F]+[+F-F-F]", 1)]
    },
    "axiom": "F"
}

lsys_c2 = {
    "stochastic": False,
    "ruleset": {
        "F": [("FF-[-F+F+FL]+[+F-F-FL]", 1)]
    },
    "axiom": "F"
}

lsys_d = {
    "stochastic": False,
    "ruleset": {
        "X": [("F[+X]F[-X]+X", 1)],
        "F": [("FF", 1)]
    },
    "axiom": "X"
}

lsys_d2 = {
    "stochastic": False,
    "ruleset": {
        "X": [("F[+XL]F[-XL]+X", 1)],
        "F": [("FF", 1)]
    },
    "axiom": "X"
}

lsys_e = {
    "Stochastic": False,
    "ruleset": {
        "X": [("F[+X][-X]FX", 1)],
        "F": [("FF", 1)]
    },
    "axiom": "X"
}

lsys_e2 = {
    "Stochastic": False,
    "ruleset": {
        "X": [("F[+XL][-XL]FXL", 1)],
        "F": [("FF", 1)]
    },
    "axiom": "X"
}

lsys_f = {
    "Stochastic": False,
    "ruleset": {
        "X": [("F-[[X]+X]+F[+FX]-X", 1)],
        "F": [("FF", 1)]
    },
    "axiom": "X"
}

lsys_f2 = {
    "Stochastic": False,
    "ruleset": {
        "X": [("F-[[X]+XL]+F[+FXL]-X", 1)],
        "F": [("FF", 1)]
    },
    "axiom": "X"
}

lsys_g = {
    "Stochastic": False,
    "ruleset": {
        "X": [("X[-FFF][+FFF]FX", 1)],
        "Y": [("YFX[+Y][-Y]", 1)]
    },
    "axiom": "YYY"
}

lsys_sto_a1 = {
    "Stochastic": True,
    "ruleset": {
        "F": [
            ("F[+F]F[-F]F", 0.33),
            ("F[+F]F", 0.33),
            ("F[-F]F", 0.34)]
    },
    "axiom": "F"
}

lsys_sto_a2 = {
    "Stochastic": True,
    "ruleset": {
        "F": [
            ("F[+FL]F[-FL]F", 0.33),
            ("F[+FL]F", 0.33),
            ("F[-FL]F", 0.34)]
    },
    "axiom": "FL"
}

symetrical_tree_3d = {
    "Stochastic": False,
    "ruleset": {
        "F": [("F[^X]//////[^XL]//////[^XL]", 1)],        
        "X": [("FF", 1)]
    },
    "axiom": "X",
    "default_angle": 22.5
}

dense_bush_3d = {
    "stochastic": False,
    "ruleset": {
        "F": [("F[+FL][-FL][^FL][&FL]", 1)]
    },
    "axiom": "F",
    "default_angle": 25
}

dense_bush_sto_3d = {
    "stochastic": True,
    "ruleset": {
        "F": [
                ("F[+F//L]X", 0.25),
                ("F[-F//L]X", 0.25),
                ("F[+F//L][-F//L]X", 0.5)],
        "X": [
                ("[^F//L][&F//L]", 0.4),
                ("[^F/L]", 0.2),
                ("[&F/L]", 0.2),
                ("", 0.2)]
    },
    "axiom": "F",
    "default_angle": 25
}

fine_herb_3d = {
    "stochastic": False,
    "ruleset": {
        "F": [("FF", 1)],
        "X": [("F[^XL]F[&XL]/XL", 1)]    
    },
    "axiom": "X",
    "default_angle": 20
}

lsys_dataset = {
    "symetrical_tree": symetrical_tree_3d,
    "dense_bush": dense_bush_3d,
    "dense_bush_sto": dense_bush_sto_3d,
    "fine_herb": fine_herb_3d
}

def get_lsys_by_id(id):
    try:
        lsys = lsys_dataset[id]
    except KeyError:
        raise KeyError("Error: no existe L-system con ID especificado")
    return lsys