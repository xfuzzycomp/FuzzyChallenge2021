import os
from competition.plotter import Plotter

if __name__ == "__main__":
    plotter = Plotter("competition_data.json")
    plotter.winner()
