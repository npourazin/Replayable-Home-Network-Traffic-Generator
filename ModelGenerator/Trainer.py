import random
import numpy
import matplotlib.pyplot as plt
from scipy import stats


class Trainer:
    data = []

    mean_of_distribution = 0
    variance_of_distribution = 1

    def __init__(self, data, distribution_type=0):
        self.data = data

        # Fit distributions through mean and average
        self.mean_of_distribution = numpy.mean(data)
        self.variance_of_distribution = numpy.var(data)

    def gamma(self, sample_number=0):
        sample_number = len(self.data)

        def gamma_random_sample(mean, variance):
            """Yields a list of random numbers following a gamma distribution defined by mean and variance"""
            g_alpha = mean * mean / variance
            g_beta = mean / variance
            for i in range(sample_number):
                yield random.gammavariate(g_alpha, 1 / g_beta)

        # force integer values to get integer sample
        grs = [int(i) for i in
               gamma_random_sample(self.mean_of_distribution, self.variance_of_distribution)]

        print("Gamma:")
        print("Original data: ", sorted(self.data))
        print("Random sample: ", sorted(grs))

    def pareto(self, sample_number=0):
        sample_number = len(self.data)
        p_a = 2
        p_size = (2, 3)  # ????
        fshape, floc, fscale = stats.pareto.fit(self.data)
        alpha = fshape
        x_m = fscale
        sample_number = len(self.data)

        def pareto_random_sample(p_alpha):
            """Yields a list of random numbers following a pareto distribution defined by alpha"""
            for i in range(sample_number):
                yield (random.paretovariate(alpha=p_alpha) * x_m)

        # force integer values to get integer sample
        prs = [int(i) for i in
               pareto_random_sample(alpha)]

        print("Pareto:")
        print("Original data: ", sorted(self.data))
        print("Random sample: ", sorted(prs))

        # todo:
        #       1- check for shape, loc and scale, maybe on a video
        #       2- check stats.pareto.pdf()


if __name__ == '__main__':
    trainer = Trainer([1, 3, 2, 2, 2, 2, 4])
    trainer.gamma()
    # numpy.seterr('raise')
    trainer.pareto()
