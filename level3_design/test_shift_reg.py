import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """
    S=[[0,0],[1,0]]
    data=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
    clock = Clock(dut.CLK, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock


#load the data
#     dut.D0.value= 0
#     dut.D1.value= 1
#     dut.D2.value= 1 
#     dut.D3.value= 1
#     dut.S0.value= 1
#     dut.S1.value= 1 
#     await FallingEdge(dut.CLK) 
#     await FallingEdge(dut.CLK)
# #After loading
#     cocotb.log.info("After Loading")
#     cocotb.log.info("Q0")
#     cocotb.log.info(dut.Q0.value)
#     cocotb.log.info(dut.Q1.value)
#     cocotb.log.info("Q2")
#     cocotb.log.info(dut.Q2.value)
#     cocotb.log.info(dut.Q3.value)

#     dut.S0.value= 1
#     dut.S1.value= 0 
    
    
#     cocotb.log.info("Before shift")
#     cocotb.log.info("Q0")
#     cocotb.log.info(dut.Q0.value)
#     cocotb.log.info(dut.Q1.value)
#     cocotb.log.info("Q2")
#     cocotb.log.info(dut.Q2.value)
#     cocotb.log.info(dut.Q3.value)

#     await FallingEdge(dut.CLK) 
#     cocotb.log.info("After shift")
#     cocotb.log.info("Q0")
#     cocotb.log.info(dut.Q0.value)
#     cocotb.log.info(dut.Q1.value)
#     cocotb.log.info("Q2")
#     cocotb.log.info(dut.Q2.value)
#     cocotb.log.info(dut.Q3.value)

    for i in S:
        #load the data
        for d in data:
            dut.D0.value= d[0]
            dut.D1.value= d[1]
            dut.D2.value= d[2]
            dut.D3.value= d[3]
            dut.S0.value= 1
            dut.S1.value= 1 
            
            await FallingEdge(dut.CLK) 
            await FallingEdge(dut.CLK)

            dut.S0.value= i[0]
            dut.S1.value= i[1] 
            print("Before shift")
            print(i[0],i[1],dut.Q3.value,dut.Q2.value,dut.Q1.value,dut.Q0.value)
            await FallingEdge(dut.CLK)
            #print("After shift") 
            print(i[0],i[1],dut.Q3.value,dut.Q2.value,dut.Q1.value,dut.Q0.value)

            if (i==[0,0]):
                assert (dut.Q0.value == dut.D3.value  and dut.Q1.value == dut.D0.value and dut.Q2.value == dut.D1.value and dut.Q3.value == dut.D2.value  ), f"Sequence detector result is incorrect for input"
            elif (i==[1,0]):
                assert (dut.Q0.value == dut.D1.value and dut.Q1.value == dut.D2.value and dut.Q2.value == dut.D3.value and dut.Q3.value == dut.D0.value ), f"Sequence detector result is incorrect for input"