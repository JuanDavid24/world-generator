import l_systems as lsys
import plant_plotter as plt

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

l_sys_d = {
    "ruleset": {
        "X": "F[+X]F[-X]+X",
        "F": "FF"
    },
    "axiom": "X"
}

l_sys_d2 = {
    "ruleset": {
        "X": "F[+XL]F[-XL]+X",
        "F": "FF"
    },
    "axiom": "X"
}

l_sys_e = {
    "ruleset": {
        "X": "F[+X][-X]FX",
        "F": "FF"
    },
    "axiom": "X"
}

l_sys_e2 = {
    "ruleset": {
        "X": "F[+XL][-XL]FXL",
        "F": "FF"
    },
    "axiom": "X"
}

l_sys_f = {
    "ruleset": {
        "X": "F-[[X]+X]+F[+FX]-X",
        "F": "FF"
    },
    "axiom": "X"
}

l_sys_f2 = {
    "ruleset": {
        "X": "F-[[X]+XL]+F[+FXL]-X",
        "F": "FF"
    },
    "axiom": "X"
}

color_fucsia = "#FF0080"
color_corn = "#FBEC5D"
color_olive = "#808000"
color_darkcyan = "#18848e"
color_lightgray = "#e8e9eb"

sentence_a = lsys.sentence_generator(l_sys_a["axiom"], l_sys_a["ruleset"], 3)
plt.plant_plotter(sentence_a, step=30, angle=30)

# sentence_a2 = lsys.sentence_generator(l_sys_a2["axiom"], l_sys_a2["ruleset"], 3)
# plt.plant_plotter(sentence_a2, step=30, angle=30, leaf_length=2)

# sentence_b = lsys.sentence_generator(l_sys_b["axiom"], l_sys_b["ruleset"], 4)
# plt.plant_plotter(sentence_b, step=15, angle=20, speed="fastest")

# sentence_b2 = lsys.sentence_generator(l_sys_b2["axiom"], l_sys_b2["ruleset"], 5)
# plt.plant_plotter(sentence_b2, step=12, angle=20, leaf_length=1, leaf_width=0.8, leaf_color=color_fucsia, branch_color=color_darkcyan, animation=False)

# sentence_c = lsys.sentence_generator(l_sys_c["axiom"], l_sys_c["ruleset"], 4)
# plt.plant_plotter(sentence_c, step=15, angle=22.5, leaf_length=1, leaf_width=0.8, leaf_color=color_corn, animation=False)

# sentence_c2 = lsys.sentence_generator(l_sys_c2["axiom"], l_sys_c2["ruleset"], 4)
# plt.plant_plotter(sentence_c2, step=15, angle=22.5, leaf_length=2, leaf_width=0.6, leaf_color=color_corn, branch_color=color_olive, animation=False)

# sentence_d = lsys.sentence_generator(l_sys_d["axiom"], l_sys_d["ruleset"], 7)
# plt.plant_plotter(sentence_d, step=3, angle=20, branch_color=color_olive, animation=False)

# sentence_d2 = lsys.sentence_generator(l_sys_d2["axiom"], l_sys_d2["ruleset"], 7)
# plt.plant_plotter(sentence_d2, step=3, angle=20, leaf_length=0.4, leaf_width=0.2, leaf_color=color_darkcyan, branch_color=color_olive, animation=False)

# sentence_e = lsys.sentence_generator(l_sys_e["axiom"], l_sys_e["ruleset"], 7)
# plt.plant_plotter(sentence_e, step=3, angle=25.7, branch_color=color_corn, animation=False)

# sentence_e2 = lsys.sentence_generator(l_sys_e2["axiom"], l_sys_e2["ruleset"], 7)
# plt.plant_plotter(sentence_e2, step=3, angle=20, leaf_length=0.4, leaf_width=0.9, leaf_color=color_lightgray, branch_color=color_corn, animation=False)

# sentence_f = lsys.sentence_generator(l_sys_f["axiom"], l_sys_f["ruleset"], 7)
# plt.plant_plotter(sentence_f, step=3, angle=25.7, branch_color=color_darkcyan, animation=False)

# sentence_f2 = lsys.sentence_generator(l_sys_f2["axiom"], l_sys_f2["ruleset"], 7)
# plt.plant_plotter(sentence_f2, step=2.5, angle=20, leaf_length=0.6, leaf_width=0.2, leaf_color=color_fucsia, branch_color=color_darkcyan, animation=False)
