from myhdl import *
import random


randrange = random.randrange

@block
def mux(z, a, b, sel):
    @always_comb
    def comb():
        if sel == 0:
            z.next = a
        else:
            z.next = b

    return comb

@block
def adder(x,in1):
    @always_comb
    def adder_op():
        x.next = out + 4
    
    return adder_op

@block
def pc_counter(out0, out1, in0):
    @always_comb
    def pc_count():
        out0[24] = in0 + 4
        out1 = in0 + 1
