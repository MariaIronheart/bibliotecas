import numpy as np
import theano.tensor as T
from theano import function

a = T.dscalar('a')
f = function([a],[a**2, a**3])
f(3)