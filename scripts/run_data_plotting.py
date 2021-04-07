"""
This file is used to show data from the competition
"""
from competition.plotter import Plotter

if __name__ == "__main__":

    test1 = Plotter("C:\\dev\\UCFuzzyChallenge2021\\test\\test_file.json")
    test1.winner()
    test1.plot()
