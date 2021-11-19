from myhdl import block, Signal, now, always, delay, instance, intbv, bin, always_comb
import random

randrange = random.randrange

@block
def XNOR(out:intbv, a:intbv, b:intbv):
    @always_comb
    def comb():
        out.next = not (a ^ b)
    return comb

@block
def test_xnor():
    out, a, b = [Signal(intbv(0)) for i in range(3)]
    XnorGate = XNOR(out, a, b)

    @instance
    def run():
        for i in range(5):
            a.next, b.next = randrange(2), randrange(2)
            yield delay(10)
            print(f"in1:{bin(a)} in2:{bin(b)} out:{bin(out)} ")

    return XnorGate, run

Sim = test_xnor()
Sim.run_sim()