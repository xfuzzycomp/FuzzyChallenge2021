import json
from typing import List, Tuple, Dict, Any
# import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


class Plotter:
    def __init__(self, file_path):
        self.data = None

        with open(file_path, "r") as file:
            self.data = json.load(file)

        self.metrics = self.generate_metrics()

    def generate_metrics(self):
        metrics = {}
        # score_dicts = [item for _, item in self.data.items()]
        metrics["Asteroids Hit"] = [[scenario_score["asteroids_hit"] for key, scenario_score in score.items()] for score in self.score_dicts]
        metrics["Deaths"] = [[scenario_score["deaths"] for key, scenario_score in score.items()] for score in
                               self.score_dicts]

        metrics["Accuracy"] = [
            [scenario_score["asteroids_hit"] / scenario_score["bullets_fired"] if scenario_score["bullets_fired"] != 0 else 0
             for key, scenario_score in score.items()] for score in self.score_dicts]
        metrics["Distance Travelled"] = [[scenario_score["distance_travelled"] for key, scenario_score in score.items()] for score in
                          self.score_dicts]
        metrics["Mean Evaluation Time"] = [[scenario_score["mean_eval_time"] for key, scenario_score in score.items()] for score in
                               self.score_dicts]
        metrics["Shots Fired"] = [[scenario_score["bullets_fired"] for key, scenario_score in score.items()] for score in
                               self.score_dicts]
        return metrics

    @property
    def evaluation_times(self):
        return [[scenario_score["evaluation_times"] for _, scenario_score in score.items()] for score in self.score_dicts]
        # return [[val["evaluation_times"] for _, item in self.data.items()] for val in self.data[next(iter(self.data))].values()]
        # return [[val["evaluation_times"] for _, item in self.data.items()] for val in item[next(iter(item))].values()]
        # return [[scenario["evaluation_times"] for _, team in self.score_dicts] for scenario in self.data[next(iter(self.data))]]


    @property
    def score_dicts(self):
        return [item for _, item in self.data.items()]

    @property
    def teams(self):
        return [key for key in self.data.keys()]

    @property
    def scenarios(self):
        return [key for key in self.data[next(iter(self.data))].keys()]

    def winner(self):

        asteroid_scores = [sum(score for score in controller) for controller in self.metrics["Asteroids Hit"]]
        death_scores = [sum(score for score in controller) for controller in self.metrics["Deaths"]]
        accuracy_scores = [sum(score for score in controller) for controller in self.metrics["Accuracy"]]

        max_score = max(asteroid_scores)

        if asteroid_scores.count(max_score) > 1:
            tied_idxs = [idx for idx in range(len(asteroid_scores)) if asteroid_scores[idx] == max_score]
            print(f"There is a {len(tied_idxs)}-way tie between {' and '.join(self.teams[idx] for idx in tied_idxs)}")
        else:
            winner_idx = asteroid_scores.index(max_score)
            print(f"{self.teams[winner_idx]} is the winner with {max_score} asteroids destroyed")

        print()
        print("all scores")
        print(" ".join(self.teams))
        for idx, scenario in enumerate(self.scenarios):
            print("Total " + " ".join(str(score) for score in asteroid_scores))

    def plot(self):
        # rearranging eval times to be per scenario for all teams
        eval_times = [[row[i] for row in self.evaluation_times] for i in range(len(self.scenarios))]
        #histogram plots for evaluation times
        n_bins = 20
        for ind, val in enumerate(eval_times):
            # print(ind, val)
            plt.figure(ind)
            for ii in range(len(self.teams)):
                plt.hist(val[ii], bins=n_bins, density=True, edgecolor="black", linewidth=1, label=self.teams[ii], alpha=0.5)
            plt.grid(True)
            plt.xticks(rotation=30)
            plt.xlabel("Evaluation Time")
            plt.ylabel("Density")
            plt.title(self.scenarios[ind] + " Evaluation Times")
            plt.legend()

        # normal metrics plots, per scenario and for each team
        for ind2, (key, value) in enumerate(self.metrics.items()):
            plt.figure(ind2+ind+1)
            for ii in range(len(self.teams)):
                plt.plot(list(range(len(self.scenarios))), value[ii], label=self.teams[ii])
            plt.xticks(list(range(len(self.scenarios))), self.scenarios, size=8, rotation=30)
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
