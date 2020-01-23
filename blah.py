
from pyopenscad.executor import Parameters, Executor

p = Parameters()
e = Executor()

p.output = "test.png"
p.preview = True
p.render = False
p.variables = dict()
p.variables["length"] = -1

p.input_file = "/Users/SEIDLM/Downloads/candleStand.scad"

e.execute(p)
