from fuzzy_asteroids.fuzzy_asteroids import AsteroidGame, FuzzyAsteroidGame
from fuzzy_asteroids.util import Scenario, Score

import os
import json
from typing import List, Tuple, Dict, Any


class CompetitionScore(Score):
    def __init__(self):
        super().__init__()

    def header(self) -> List:
        return list(key for key in self.__dict__.keys())

    def row(self) -> List:
        return [self.__dict__[key] for key in self.header()]


class CompetitionRunner:
    def __init__(self, portfolio, controllers: Dict[str, Any] = None):
        self.portfolio = portfolio

        # What directory to save the runner information in
        self.directory = os.path.abspath(os.path.curdir)

        # Settings for running the environments in different scenarios
        self.hidden_settings = {"real_time_multiplier": 0, "graphics_on": False, "prints": False}
        self.visible_settings = {"real_time_multiplier": 1, "graphics_on": True, "prints": True}

        if controllers:
            self.builder_fcns = controllers
            self.scores = {key: None for key in controllers.keys()}
            self.data = {key: None for key in controllers.keys()}

    def simpler_scores(self, data: Dict[str, Dict]):
        pass

    def save_file(self, file_name: str, data: Dict[str, Any]):
        with open(os.path.join(self.directory, file_name), "w") as file:
            json.dump(data, file, indent=2)

    def load_file(self, file_name: str) -> Dict[str, Any]:
        with open(os.path.join(self.directory, file_name), "w") as file:
            data = json.load(file)
        return data

    def run_human(self, name: str) -> Dict[str, Dict]:
        settings = {"real_time_multiplier": 1, "graphics_on": True, "prints": False}
        game = self.create_environment(settings, human_test=True)
        scores = self._run(name, None, self.portfolio, game)
        return {name: scores}

    def run_all(self, portfolio: List[Scenario] = None, graphics_on=True) -> Dict[str, Dict]:
        all_data = {}

        # Run each controller over the whole portfolio
        for key, controller in self.builder_fcns.items():
            data = self.run(name=key,
                            controller=controller() if callable(controller) else controller,
                            portfolio=portfolio,
                            graphics_on=graphics_on)

            all_data.update(**data)
        return all_data

    def run(self, name: str, controller, portfolio: List[Scenario] = None, graphics_on: bool = True) -> Dict[str, Any]:
        game = self.create_environment(self.visible_settings if graphics_on else self.hidden_settings)
        scores = self._run(name, controller, portfolio, game)
        return {name: scores}

    def _run(self, name: str, controller, portfolio: List[Scenario], game: AsteroidGame) -> Any:
        data = {}

        # Use the given portfolio if it is not, otherwise use the stored portfolio
        _portfolio = portfolio if portfolio else self.portfolio

        if not game.graphics_on:
            print(f"{name} ", end="")

        for scenario in _portfolio:
            scenario_name = str(scenario.name)

            score = self._run_game(game, controller=controller, scenario=scenario)

            if not game.graphics_on:
                print(".", end="")

            data[scenario_name] = score.__dict__

        if not game.graphics_on:
            print()

        return data

    @staticmethod
    def create_environment(override_settings, human_test=False) -> AsteroidGame:
        settings = {"frequency": 60, "time_limit": 1000}
        settings.update(**override_settings)

        if human_test:
            return AsteroidGame(settings=settings)
        else:
            return FuzzyAsteroidGame(settings=settings, track_compute_cost=True)

    @staticmethod
    def _run_game(game, controller, scenario) -> CompetitionScore:
        """
        Function runs a game with the competition score class
        :param game: Game instance
        :param controller: Controller instance
        :param scenario: Scenario to run
        :return: CompetitionScore
        """
        return game.run(controller=controller, scenario=scenario, score=CompetitionScore())
