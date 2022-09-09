import random
import numpy


class Trainer:
    data = []

    mean_of_distribution = 0
    variance_of_distribution = 1

    def __init__(self, data, distribution_type=0):
        self.data = data

        # Fit distributions through mean and average
        self.mean_of_distribution = numpy.mean(data)
        self.variance_of_distribution = numpy.var(data)

    def gamma(self):
        def gamma_random_sample(mean, variance, sample_number):
            """Yields a list of random numbers following a gamma distribution defined by mean and variance"""
            g_alpha = mean * mean / variance
            g_beta = mean / variance
            for i in range(sample_number):
                yield random.gammavariate(g_alpha, 1 / g_beta)

        # force integer values to get integer sample
        grs = [int(i) for i in
               gamma_random_sample(self.mean_of_distribution, self.variance_of_distribution, len(self.data))]

        print("Original data: ", sorted(self.data))
        print("Random sample: ", sorted(grs))


if __name__ == '__main__':
    trainer = Trainer([6176, 11046, 670, 6146, 7945, 6864, 6282, 8619, 7903, 6318, 13294, 6990, 5515, 9157]
                      )
    trainer.gamma()
