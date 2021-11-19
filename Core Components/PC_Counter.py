from myhdl import *
import random

randrange = random.randrange

DW = 32

@block
def PC(clock, input, pc, pc4):

    reg = Signal(modbv(0,0,2**DW))
    @always_comb
    def read():
        pc.next = reg
        pc4.next = reg + 4
    
    @always(clock.posedge)
    def write():
        reg.next = input

    return read, write

@block
def PC_Test():
    input, pc, pc4 = [Signal(intbv(0)) for i in range(3)]
    PC_Check = PC(clock, input, pc, pc4)

    @instance
    def clk():
        clk.next = not clock

    @instance
    def run():
        for i in range(5):
            input.next, pc.next, pc4.next = randrange(2), randrange(2), randrange(2)
            #yield delay(10)
            print(f"inp:{input} pc:{pc} pc4:{pc4}")

    return clk, run

Sim = PC_Test()
Sim.run_sim()