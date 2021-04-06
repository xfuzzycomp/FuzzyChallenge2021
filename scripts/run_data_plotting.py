"""
This file is used to show data from the competition
"""
from competition.plotter import Plotter

if __name__ == "__main__":
    plotter = Plotter(file_path="competition_data.json")
    plotter.winner(plotter.data)
