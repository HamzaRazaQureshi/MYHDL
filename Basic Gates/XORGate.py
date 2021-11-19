from myhdl import block, Signal, now, always, delay, instance, intbv, bin, always_comb
import random

randrange = random.randrange

@block
def XOR(out:intbv, a:intbv, b:intbv):
    @always_comb
    def comb():
        out.next = a ^ b
    return comb

@block
def test_xor():
    out, a, b = [Signal(intbv(0)) for i in range(3)]
    XorGate = XOR(out, a, b)

    @instance
    def run():
        for i in range(5):
            a.next, b.next = randrange(2), randrange(2)
            yield delay(10)
            print(f"in1:{a} in2:{b} out:{out} ")

    return XorGate, run

Sim = test_xor()
Sim.run_sim()