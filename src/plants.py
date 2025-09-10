import l_systems as lsys

l_sys_a = {
    "ruleset": {
        "F": "F[+F]F[-F]F"
    },
    "axiom": "F"
}

l_sys_a2 = {
    "ruleset": {
        "F": "F[+FL]F[-FL]F"
    },
    "axiom": "F"
}

l_sys_b = {
    "ruleset": {
        "F": "F[+F]F[-F][F]"
    },
    "axiom": "F"
}

l_sys_b2 = {
    "ruleset": {
        "F": "F[+FL]F[-FL][FL]"
    },
    "axiom": "F"
}

l_sys_c = {
    "ruleset": {
        "F": "FF-[-F+F+F]+[+F-F-F]"
    },
    "axiom": "F"
}

l_sys_c2 = {
    "ruleset": {
        "F": "FF-[-F+F+FL]+[+F-F-FL]"
    },
    "axiom": "F"
}

color_fucsia = "#FF0080"
color_corn = "#FBEC5D"
color_olive = "#808000"
color_darkcyan = "#18848e"

# sentence_a = lsys.sentence_generator(l_sys_a["axiom"], l_sys_a["ruleset"], 3)
# lsys.plant_plotter(sentence_a, step=30, angle=30)

# sentence_a2 = lsys.sentence_generator(l_sys_a2["axiom"], l_sys_a2["ruleset"], 3)
# lsys.plant_plotter(sentence_a2, step=30, angle=30, leaf_length=2)

# sentence_b = lsys.sentence_generator(l_sys_b["axiom"], l_sys_b["ruleset"], 4)
# lsys.plant_plotter(sentence_b, step=15, angle=20, speed="fastest")

# sentence_b2 = lsys.sentence_generator(l_sys_b2["axiom"], l_sys_b2["ruleset"], 5)
# lsys.plant_plotter(sentence_b2, step=12, angle=20, leaf_length=1, leaf_width=0.8, leaf_color=color_fucsia, branch_color=color_darkcyan, animation=False)

# sentence_c = lsys.sentence_generator(l_sys_c["axiom"], l_sys_c["ruleset"], 4)
# lsys.plant_plotter(sentence_c, step=15, angle=22.5, leaf_length=1, leaf_width=0.8, leaf_color=color_corn, animation=False)

# sentence_c2 = lsys.sentence_generator(l_sys_c2["axiom"], l_sys_c2["ruleset"], 4)
# lsys.plant_plotter(sentence_c2, step=15, angle=22.5, leaf_length=2, leaf_width=0.6, leaf_color=color_corn, branch_color=color_olive, animation=False)

