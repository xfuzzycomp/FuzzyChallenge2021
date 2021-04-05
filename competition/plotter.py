import json
from typing import List, Tuple, Dict, Any


class Plotter:
    def __init__(self, file_path):
        self.data = None

        with open(file_path, "r") as file:
            self.data = json.load(file)

    def winner(self, data: Dict[str, Dict]):
        teams = [key for key in data.keys()]
        scenarios = [key for key in data[next(iter(data))].keys()]
        print(scenarios)

        score_dicts = [item for _, item in data.items()]
        asteroids_per_scenario = [[scenario_score["asteroids_hit"] for key, scenario_score in score.items()] for score in score_dicts]
        deaths_per_scenario = [[scenario_score["deaths"] for key, scenario_score in score.items()] for score in score_dicts]
        accuracy_per_scenario = [[scenario_score["asteroids_hit"]/scenario_score["bullets_fired"] for key, scenario_score in score.items()] for score in score_dicts]

        asteroid_scores = [sum(score for score in controller) for controller in asteroids_per_scenario]
        death_scores = [sum(score for score in controller) for controller in deaths_per_scenario]
        accuracy_scores = [sum(score for score in controller) for controller in accuracy_per_scenario]

        max_score = max(asteroid_scores)

        if asteroid_scores.count(max_score) > 1:
            tied_idxs = [idx for idx in range(len(asteroid_scores)) if asteroid_scores[idx] == max_score]
            print(f"There is a {len(tied_idxs)}-way tie between {' and '.join(teams[idx] for idx in tied_idxs)}")
        else:
            winner_idx = asteroid_scores.index(max_score)
            print(f"{teams[winner_idx]} is the winner with {max_score} asteroids destroyed")

        print()
        print("all scores")
        print(" ".join(teams))
        for idx, scenario in enumerate(scenarios):
            print(scenario, asteroids_per_scenario[idx])
        print(" ".join(str(score) for score in asteroid_scores))

    def plot(self):
        pass

    def save(self):
        pass


if __name__ == "__main__":
    pass
