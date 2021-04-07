import json
from typing import List, Tuple, Dict, Any
# import matplotlib
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, file_path):
        self.data = None

        with open(file_path, "r") as file:
            self.data = json.load(file)

        self.metrics = self.generate_metrics()

    def generate_metrics(self):
        metrics = {}
        score_dicts = [item for _, item in self.data.items()]
        metrics["Asteroids Hit"] = [[scenario_score["asteroids_hit"] for key, scenario_score in score.items()] for score in score_dicts]
        metrics["Deaths"] = [[scenario_score["deaths"] for key, scenario_score in score.items()] for score in
                               score_dicts]
        metrics["Accuracy"] = [
            [scenario_score["asteroids_hit"] / scenario_score["bullets_fired"] for key, scenario_score in score.items()]
            for score in score_dicts]
        metrics["Distance Travelled"] = [[scenario_score["distance_travelled"] for key, scenario_score in score.items()] for score in
                          score_dicts]
        metrics["Mean Evaluation Time"] = [[scenario_score["mean_eval_time"] for key, scenario_score in score.items()] for score in
                               score_dicts]
        metrics["Shots Fired"] = [[scenario_score["bullets_fired"] for key, scenario_score in score.items()] for score in
                               score_dicts]
        return metrics

    def winner(self):

        teams = [key for key in self.data.keys()]
        scenarios = [key for key in self.data[next(iter(self.data))].keys()]
        print(scenarios)


        asteroid_scores = [sum(score for score in controller) for controller in self.metrics["Asteroids Hit"]]
        death_scores = [sum(score for score in controller) for controller in self.metrics["Deaths"]]
        accuracy_scores = [sum(score for score in controller) for controller in self.metrics["Accuracy"]]

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
            print(scenario, self.metrics["Asteroids Hit"][idx])
        print(" ".join(str(score) for score in asteroid_scores))

    def plot(self):
        teams = [key for key in self.data.keys()]
        scenarios = [key for key in self.data[next(iter(self.data))].keys()]

        for ind, (key, value) in enumerate(self.metrics.items()):
            plt.figure(ind)
            for ii in range(len(teams)):
                plt.plot(list(range(len(scenarios))), value[ii], label=teams[ii])
            plt.xticks(list(range(len(scenarios))), scenarios, size="small")
            plt.grid(True)
            plt.xlabel("Scenario")
            plt.ylabel(key)
            plt.title(key + " vs. Scenario")
            plt.legend()
        plt.show()

    def save(self):
        pass


if __name__ == "__main__":
    pass
