from myhdl import block, Signal, now, always, delay, instance, intbv, bin, always_comb
import random

randrange = random.randrange

@block
def NOT(out:intbv, a:intbv):
    @always_comb
    def comb():
        out.next = not a
    return comb

@block
def test_Not():
    out, a = [Signal(intbv()) for i in range(2)]
    NotGate = NOT(out, a)

    @instance
    def run():
        for i in range(5):
            a.next = randrange(2)
            yield delay(10)
            print(f"in1:{a} out:{out} ")

    return NotGate, run

Sim = test_Not()
Sim.run_sim()