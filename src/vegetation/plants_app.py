import l_systems as lsystem
import plant_plotter as plt
import data.lsys_examples as data
import data.colors as color
from utils.timer import Timer
from utils.logger import log_plant_to_json

def run_lsystem(lsys, iterations, debug=False, seed=None, **plot_kwargs):
    timer = Timer(debug)
    timer.run()
    sentence, seed = lsystem.sentence_generator(lsys["axiom"], lsys["ruleset"], iterations, seed)
    timer.stop()
    log_plant_to_json(lsys, iterations, seed, sentence)
    timer.run()
    plt.plant_plotter(sentence, **plot_kwargs)
    timer.stop()

# determinist systems
# run_lsystem(data.lsys_a, 3, step=30, angle=30)
# run_lsystem(data.lsys_a2, 3, step=30, angle=30, leaf_length=2)
# run_lsystem(data.lsys_b, 4, step=15, angle=20, speed="fastest")
# run_lsystem(data.lsys_b2, 5, step=12, angle=20, leaf_length=1, leaf_width=0.8, leaf_color=color.fucsia, branch_color=color.darkcyan, animation=False)
# run_lsystem(data.lsys_c, 4, step=15, angle=22.5, leaf_length=1, leaf_width=0.8, leaf_color=color.corn, animation=False)
# run_lsystem(data.lsys_c2, 4, step=15, angle=22.5, leaf_length=2, leaf_width=0.6, leaf_color=color.corn, branch_color=color.olive, animation=False)
# run_lsystem(data.lsys_d, 7, step=3, angle=20, branch_color=color.olive, animation=False)
# run_lsystem(data.lsys_d2, 7, step=3, angle=20, leaf_length=0.4, leaf_width=0.2, leaf_color=color.darkcyan, branch_color=color.olive, animation=False)
# run_lsystem(data.lsys_e, 7, step=3, angle=25.7, branch_color=color.corn, animation=False)
# run_lsystem(data.lsys_e2, 7, step=3, angle=20, leaf_length=0.4, leaf_width=0.9, leaf_color=color.lightgray, branch_color=color.corn, animation=False)
# run_lsystem(data.lsys_f, 7, step=3, angle=25.7, branch_color=color.darkcyan, animation=False)
# run_lsystem(data.lsys_f2, 6, debug=True, step=2.5, angle=20, leaf_length=0.6, leaf_width=0.2, leaf_color=color.fucsia, branch_color=color.darkcyan, animation=False)
# run_lsystem(data.lsys_g, 5, step=6, decay=0.9, angle=35, branch_color=color.darkcyan, animation=False)

# # stochastic systems
run_lsystem(data.lsys_sto_a1, 4, step=30, angle=40, leaf_length=2, animation=False, debug=True)
# run_lsystem(data.lsys_sto_a2, 4, step=25, angle=40, leaf_length=2, animation=False)