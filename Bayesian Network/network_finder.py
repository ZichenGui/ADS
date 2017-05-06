from pebl import data
from pebl import prior
from pebl.learner import greedy


dataset = data.fromfile("output.txt")
dataset.discretize(numbins = 3)

node_src = [32 for ii in range(32)] + [3 for ii in range(32)] + [30 for ii in range(32)] + [31 for ii in range(32)]
node_dest = range(32) + range(32) + range(32) + range(32)
prior = prior.Prior(33, prohibited_edges = zip(node_src, node_dest))


learner = greedy.GreedyLearner(dataset, prior, max_iterations = 120000)
result = learner.run()
result.tohtml()
