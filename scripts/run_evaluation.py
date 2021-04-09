"""
This file is used to run graphics for the competition
"""
from competition.competitors import controllers
from competition.portfolio import portfolio
from competition.runner import CompetitionRunner


def run_evaluation(portfolio, controllers):
    # Run the competition without graphics to generate data
    runner = CompetitionRunner(portfolio=portfolio, controllers=controllers)
    data = runner.run_all(graphics_on=False)
    runner.save_file("competition_data2.json", data)


if __name__ == "__main__":
    run_evaluation(portfolio=portfolio, controllers=controllers)
