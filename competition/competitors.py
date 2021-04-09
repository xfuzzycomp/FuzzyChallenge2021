import sys
import os
from functools import partial

from competition.portfolio import portfolio
from competition.runner import CompetitionRunner
from competition.plotter import Plotter

# Add to system path to load controller modules
sys.path.insert(0, os.path.abspath("../controllers/SamKing"))
sys.path.insert(1, os.path.abspath("../controllers/TeamAsimov/src"))
sys.path.insert(2, os.path.abspath("../controllers/HeiTerry/src"))

# Perform import of partiicpant controllers
import controllers.SamKing.controller
import controllers.TeamAsimov.src.evaluator
import controllers.HeiTerry.src.sample_training_script

# Set up controllers based on given examples
sam_king_gene = [[[-0.016246364446154682, -0.36285930195602933, -0.9702654976469424],
                  [0.4649000608588642, 0.73135334195408, 0.7840761736391507],
                  [0, 3, 1, 0, 2, 2, 1, 0, 0, 2, 1, 2],
                  [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                  [-32, -118, -29, -86, -114, -70, -29],
                  [131, 138, 149, 79, 41, 59, 81]], 41.842592592592595]

heiTerry_chrom = controllers.HeiTerry.src.sample_training_script.Chromosome(controllers.HeiTerry.src.sample_training_script.chrom)

# Store controller definitions in delayed function calls
controllers = {
    "SamKing": partial(controllers.SamKing.controller.FuzzyController, sam_king_gene),
    "HeiTerry": partial(controllers.HeiTerry.src.sample_training_script.FuzzyController, heiTerry_chrom),
    "TeamAsimov": controllers.TeamAsimov.src.evaluator.FuzzyController,
}
