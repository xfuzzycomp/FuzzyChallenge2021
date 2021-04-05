import math
import time
from typing import Dict, Tuple, Any

from fuzzy_asteroids.util import Scenario
from fuzzy_asteroids.fuzzy_controller import ControllerBase, SpaceShip

from competition.scenarios import portfolio
from competition.runner import CompetitionRunner
from competition.plotter import Plotter


# Competition repositories
repos = [
    "https://github.com/samking7185/UCFuzzyChallenge",
    "https://github.com/WesleyBumpus/TeamAsimov",
    "https://github.com/WiceCwispies/HeiTerryAsteroids"
]


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
    Scenario(name="scenario1", num_asteroids=4, seed=idx) for idx in range(2)
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
    runner = CompetitionRunner(portfolio=portfolio, controllers=controllers)
    data = runner.run_all(graphics_on=True)
    # print(data)

    # data = runner.run_human(name="brandon")
    # print(data)

    # data = CompetitionRunner().run_blind(name="controller1", controller=Controller1(), portfolio=_portfolio)
    # print(data)

    # a = CompetitionRunner(builder_fcns=controllers)
    # data = a.run_all_blind(portfolio=_portfolio)
    # a.save_file("test_file.json", data)

    # plotter = Plotter("test_file.json")
    # plotter.winner(plotter.data)

    # print("\n".join(str(row) for row in data))

    # a = CompetitionRunner(controllers={"controller1": Controller1()})
    # data = a.run_with_graphics(name="controller1", controller=Controller1(), portfolio=_show_portfolio)
    # print(data)
