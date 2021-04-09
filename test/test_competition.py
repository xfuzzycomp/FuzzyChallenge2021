import math
from typing import Dict, Tuple, Any

from fuzzy_asteroids.util import Scenario
from fuzzy_asteroids.fuzzy_controller import ControllerBase, SpaceShip

from competition.portfolio import portfolio, show_portfolio, portfolio_dict, show_portfolio_dict
from competition.runner import CompetitionRunner
from competition.plotter import Plotter



class Controller1(ControllerBase):

    def actions(self, ship: SpaceShip, input_data: Dict[str, Any]) -> None:
        ship.turn_rate = ship.turn_rate_range[0]
        # ship.thrust = max(ship.thrust_range)
        # ship.shoot()


class Controller2(ControllerBase):

    def actions(self, ship: SpaceShip, input_data: Dict[str, Any]) -> None:
        ship.turn_rate = ship.turn_rate_range[0] * math.cos(input_data["frame"] * 10)
        # ship.thrust = max(ship.thrust_range)
        # ship.shoot()


_portfolio = [
    Scenario(name="scenario"+str(idx), num_asteroids=4, seed=idx) for idx in range(4)
]

_show_portfolio = [
    Scenario(name="scenario1", num_asteroids=4, seed=0)
]

if __name__ == "__main__":
    controllers = {
        "controller1": Controller1(),
        "controller2": Controller2(),
    }

    # Run the competition on the portfolio with no graphics and get the results
    # runner = CompetitionRunner(portfolio=_portfolio, controllers=controllers)
    # data = runner.run_all(graphics_on=False)
    # runner.save_file("test_file.json", data)

    # data = CompetitionRunner().run_blind(name="controller1", controller=Controller1(), portfolio=_portfolio)

    # a = CompetitionRunner(builder_fcns=controllers)
    # data = a.run_all_blind(portfolio=_portfolio)
    # a.save_file("test_file.json", data)

    plotter = Plotter("test_file.json")
    plotter.winner()

    # a = CompetitionRunner(controllers={"controller1": Controller1()})
    # data = a.run_with_graphics(name="controller1", controller=Controller1(), portfolio=_show_portfolio)
    # print(data)
