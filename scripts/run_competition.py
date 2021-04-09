"""
This file is used to run graphics for the competition
"""

from competition.portfolio import portfolio
from competition.runner import CompetitionRunner

from competition.competitors import controllers


def run_competition(portfolio, controllers):
    # Run the competition with graphics
    runner = CompetitionRunner(portfolio=portfolio, controllers=controllers)
    runner.run_all(opt_settings={"time_limit": 60})



if __name__ == "__main__":
    # Run the competition on the portfolio with graphics for the competition for all
    # run_competition(portfolio=portfolio, controllers=controllers)

    # Run SamKing
    run_competition(portfolio=portfolio, controllers={"SamKing": controllers["SamKing"]})

    # # Run HeiTerry
    # run_competition(portfolio=portfolio, controllers={"HeiTerry": controllers["HeiTerry"]})
    #
    # # Run Team Asimov
    # run_competition(portfolio=portfolio, controllers={"TeamAsimov": controllers["TeamAsimov"]})
