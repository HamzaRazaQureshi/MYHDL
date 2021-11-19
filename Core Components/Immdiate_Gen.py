from myhdl import *

@block
def ImmGen(inst,pc,s,sb,uj,u,i):
    @always_comb
    def generate():
        # i type
        i.next = concat(intbv(inst[31])[20:],inst[32:20])
        # s type
        s.next = concat(intbv(inst[31])[20:], inst[32:25], inst[12:7])
        #u type
        u.next = concat(inst[32:12], intbv(0)[11:])
        # sb type
        sb.next = concat(intbv(inst[31])[19:], inst[31], inst[7], inst[31:25], inst[12:8], intbv(0)[1:]) + pc
        # uj type
        uj.next = concat(intbv(inst[31])[12:], inst[20:12], inst[20], inst[31:21], intbv(0)[1:]) + pc
    return generate

DW = 2**31

@block
def simulate():
    inst,pc = [Signal(intbv(0, 0, DW)[32:]) for i in range(2)]
    s , sb , uj , u, i = [Signal(intbv(0)[32:]) for i in range(5)]
    imm = ImmGen(inst,pc,s , sb , uj , u, i)

#    test
    instructionsList = [0x010201e7]

    @instance
    def run():
        for x in instructionsList:
            inst.next = x
            pc.next = 0x00000000
            yield delay(10)
            print("inst : ",inst)
            print("pc",pc)
            print("i_imm : ",i)
            print("s_imm : ",s)
            print("sb_imm : ",sb)
            print("uj_imm : ",uj)
            print("u_imm : ",u)
    return run, imm

ab = simulate()
ab.run_sim()