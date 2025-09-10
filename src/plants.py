import l_systems as lsys

l_sys_a = {
    "ruleset": {
        "F": "F[+F]F[-F]F"
    },
    "axiom": "F"
}

n = 2
angle = 30
stroke_len = 15

sentence_a = lsys.sentence_generator(l_sys_a["axiom"], l_sys_a["ruleset"], n)

lsys.plant_plotter(sentence_a, stroke_len, angle)

