"""
This file is used to run graphics for the competition
"""

from competition.competitors import controllers
from competition.portfolio import portfolio, show_portfolio
from competition.runner import CompetitionRunner


def run_competition(portfolio, controllers):
    runner = CompetitionRunner(portfolio=portfolio, controllers=controllers)
    runner.run_all(opt_settings={"time_limit": 60})


if __name__ == "__main__":
    # Run the competition on the portfolio with graphics for the competition for all
    run_competition(portfolio=portfolio, controllers=controllers)

    """
    Run the competition individually for each team
    """
    # Run SamKing
    # run_competition(portfolio=show_portfolio, controllers={"SamKing": controllers["SamKing"]})

    # Run HeiTerry
    # run_competition(portfolio=show_portfolio, controllers={"HeiTerry": controllers["HeiTerry"]})

    # # Run Team Asimov
    # run_competition(portfolio=show_portfolio, controllers={"TeamAsimov": controllers["TeamAsimov"]})
