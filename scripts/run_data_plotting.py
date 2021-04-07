"""
This file is used to show data from the competition
"""
from competition.plotter import Plotter

if __name__ == "__main__":

    plotter = Plotter(file_path=r"..\test\test_file.json")
    plotter.winner()
    plotter.plot()

