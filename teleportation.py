from pyquil import Program, get_qc
from pyquil.gates import *
from pyquil.api import WavefunctionSimulator
from math import pi

# prepare Objects
p = Program()
wf = WavefunctionSimulator()

# prepare sending qubit
p += RY(pi / 4.0, 0)
print('Sending quantum state.')
print(wf.wavefunction(p))

# prepare Bell state
p += H(1)
p += CNOT(1,2)

# prepare classical register
ro = p.declare('ro', 'BIT', 2)

# measure Alice bits
p += CNOT(0,1)
p += H(0)
p += MEASURE(0, ro[0])
p += MEASURE(1, ro[1])

# apply gates to Bob's bit
p.if_then(ro[1], X(2))
p.if_then(ro[0], Z(2))
print('Received quantum state.')
print(wf.wavefunction(p))
