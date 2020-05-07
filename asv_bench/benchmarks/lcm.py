from skmine.itemsets import LCM
from skmine.datasets import make_transactions

class LCMBench:
    params = ([.1, .3], [20], [.3, .6])
    param_names = ['min_supp', 'n_transactions', 'density']
    #timeout = 20  # timeout for a single run, in seconds
    repeat = (1, 3, 20.0)
    processes = 1
    def setup(self, min_supp, n_transactions, density):
        self.transactions = make_transactions(
            n_transactions=n_transactions,
            density=density,
            random_state=7,
        )
        self.lcm = LCM(min_supp=min_supp, n_jobs=1)  # set n_jobs to 1 for now

    def time_fit_only(self, *args):
        self.lcm.fit(self.transactions)

    def time_fit_transform(self, *args):
        self.lcm.fit_transform(self.transactions)

    def mem_fit_ony(self, *args):
        self.lcm.fit(self.transactions)

    def mem_fit_transform(self, *args):
        self.lcm.fit_transform(self.transactions)