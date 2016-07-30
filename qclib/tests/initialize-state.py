import qclib
import numpy as np

try:
	nqbits = 6
	initstate = [None]*(2**nqbits)

	p = 0
	stsz = 2**nqbits
	for i in range(stsz):
		c = np.cos(i*2*np.pi/stsz)
		s = np.sin(i*2*np.pi/stsz)
		initstate[i] = complex(c,s)
		p += np.absolute(initstate[i])**2
	initstate = np.transpose(np.matrix(initstate,dtype=complex))/np.sqrt(p)
	q = qclib.qcsim(nqbits,initstate=initstate, qtrace=True)
except qclib.QClibError, ex:
	print ex.args
