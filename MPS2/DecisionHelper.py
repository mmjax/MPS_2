
import methods


class DecisionHelper:

    def __init__(self, dataset, weights, name, signs=None):
        self.dataset = dataset
        self.weights = weights
        self.name = name
        self.signs = signs if signs else [1]*len(weights)

    def topsis(self):
        return methods.topsis(
            self.dataset,
            self.weights,
            self.name,
            self.signs
        )

    def electre(self):
        return methods.electre(
            self.dataset,
            self.name,
            self.weights
        )

    def saw(self):
        return methods.saw_method(
            self.dataset,
            self.name,
            self.weights
        )
