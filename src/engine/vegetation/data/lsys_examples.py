lsys_a = {
    "ruleset": {
        "F": [("F[+F]F[-F]F", 1)]
    },
    "axiom": "F"
}

lsys_a2 = {
    "ruleset": {
        "F": [("F[+FL]F[-FL]F", 1)]
    },
    "axiom": "F"
}

lsys_b = {
    "ruleset": {
        "F": [("F[+F]F[-F][F]", 1)]
    },
    "axiom": "F"
}

lsys_b2 = {
    "ruleset": {
        "F": [("F[+FL]F[-FL][FL]", 1)]
    },
    "axiom": "F"
}

lsys_c = {
    "ruleset": {
        "F": [("FF-[-F+F+F]+[+F-F-F]", 1)]
    },
    "axiom": "F"
}

lsys_c2 = {
    "ruleset": {
        "F": [("FF-[-F+F+FL]+[+F-F-FL]", 1)]
    },
    "axiom": "F"
}

lsys_d = {
    "ruleset": {
        "X": [("F[+X]F[-X]+X", 1)],
        "F": [("FF", 1)]
    },
    "axiom": "X"
}

lsys_d2 = {
    "ruleset": {
        "X": [("F[+XL]F[-XL]+X", 1)],
        "F": [("FF", 1)]
    },
    "axiom": "X"
}

lsys_e = {
    "ruleset": {
        "X": [("F[+X][-X]FX", 1)],
        "F": [("FF", 1)]
    },
    "axiom": "X"
}

lsys_e2 = {
    "ruleset": {
        "X": [("F[+XL][-XL]FXL", 1)],
        "F": [("FF", 1)]
    },
    "axiom": "X"
}

lsys_f = {
    "ruleset": {
        "X": [("F-[[X]+X]+F[+FX]-X", 1)],
        "F": [("FF", 1)]
    },
    "axiom": "X"
}

lsys_f2 = {
    "ruleset": {
        "X": [("F-[[X]+XL]+F[+FXL]-X", 1)],
        "F": [("FF", 1)]
    },
    "axiom": "X"
}

lsys_g = {
    "ruleset": {
        "X": [("X[-FFF][+FFF]FX", 1)],
        "Y": [("YFX[+Y][-Y]", 1)]
    },
    "axiom": "YYY"
}

lsys_sto_a1 = {
    "ruleset": {
        "F": [
            ("F[+F]F[-F]F", 0.33),
            ("F[+F]F", 0.33),
            ("F[-F]F", 0.34)]
    },
    "axiom": "F"
}

lsys_sto_a2 = {
    "ruleset": {
        "F": [
            ("F[+FL]F[-FL]F", 0.33),
            ("F[+FL]F", 0.33),
            ("F[-FL]F", 0.34)]
    },
    "axiom": "FL"
}