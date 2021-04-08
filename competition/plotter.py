import json
from typing import List, Tuple, Dict, Any
# import matplotlib
import matplotlib.pyplot as plt
# from matplotlib import colors
# from matplotlib.ticker import PercentFormatter

def convert_label(label: str):
    return " ".join(l.capitalize() for l in label.split("_"))

class Plotter:
    def __init__(self, file_path):
        self.data = None

        with open(file_path, "r") as file:
            self.data = json.load(file)

        self.metrics = self.generate_metrics()

    def generate_metrics(self):
        metrics = {}
        score_dicts = [item for _, item in self.data.items()]
        metrics["asteroids_hit"] = [[scenario_score["asteroids_hit"] for key, scenario_score in score.items()] for score in score_dicts]
        metrics["deaths"] = [[scenario_score["deaths"] for key, scenario_score in score.items()] for score in
                               score_dicts]

        metrics["accuracy"] = [
            [scenario_score["asteroids_hit"] / scenario_score["bullets_fired"] if scenario_score["bullets_fired"] != 0 else 0
             for key, scenario_score in score.items()] for score in score_dicts]
        metrics["distance_travelled"] = [[scenario_score["distance_travelled"] for key, scenario_score in score.items()]
                                         for score in score_dicts]
        metrics["mean_evaluation_time"] = [[scenario_score["mean_eval_time"] for key, scenario_score in score.items()]
                                           for score in score_dicts]
        metrics["shots_fired"] = [[scenario_score["bullets_fired"] for key, scenario_score in score.items()]
                                  for score in score_dicts]
        return metrics

    @property
    def evaluation_times(self):
        return [[scenario_score["evaluation_times"] for _, scenario_score in score.items()] for score in self.score_dicts]

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

        asteroid_scores = [sum(score for score in controller) for controller in self.metrics["asteroids_hit"]]
        death_scores = [sum(score for score in controller) for controller in self.metrics["deaths"]]
        accuracy_scores = [sum(score for score in controller) for controller in self.metrics["accuracy"]]

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
            print(scenario, end=" ")

            for team_idx, team in enumerate(self.teams):
                print(self.metrics["asteroids_hit"][team_idx][idx], end=" ")
            print()
        print("Total " + " ".join(str(score) for score in asteroid_scores))

    def plot(self):
        # rearranging eval times to be per scenario for all teams
        eval_times = [[row[i] for row in self.evaluation_times] for i in range(len(self.scenarios))]
        # histogram plots for evaluation times
        n_bins = 20
        fig, axs = plt.subplots(1, len(self.scenarios), sharey='all')
        for ind, val in enumerate(eval_times):
            for ii in range(len(self.teams)):
                axs[ind].hist(val[ii], bins=n_bins, density=True, edgecolor="black", linewidth=1, label=self.teams[ii], alpha=0.5)
            axs[ind].set_title(self.scenarios[ind])
            axs[ind].set_xticklabels(axs[ind].get_xticklabels(), rotation=30)
            axs[ind].grid(True)
            axs[ind].legend()
            # plt.xlabel(self.scenarios[ind])
            # plt.ylabel("Density")
            # plt.legend()

        # normal metrics plots, per scenario and for each team
        for ind, (key, value) in enumerate(self.metrics.items()):
            plt.figure(ind+2)
            for ii in range(len(self.teams)):
                plt.plot(list(range(len(self.scenarios))), value[ii], label=self.teams[ii])
            plt.xticks(list(range(len(self.scenarios))), self.scenarios, size=8, rotation=30)
            plt.grid(True)
            plt.xlabel("Scenario")
            plt.ylabel(convert_label(key))
            plt.title(convert_label(key) + " vs. Scenario")
            plt.legend()
        plt.show()





    def save(self):
        pass


if __name__ == "__main__":
    pass
