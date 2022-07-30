# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    # dut.current_state.value=4
    # dut.next_state.value=4
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    dut.inp_bit = 1
    await FallingEdge(dut.clk)
    dut.inp_bit = 0
    await FallingEdge(dut.clk) 
    dut.inp_bit = 1
    await FallingEdge(dut.clk) 
    cocotb.log.info(dut.next_state.value)
    cocotb.log.info(dut.current_state.value)
    dut.inp_bit = 0
    await FallingEdge(dut.clk) 
    dut.inp_bit = 1
    await FallingEdge(dut.clk) 
    dut.inp_bit = 1
    await FallingEdge(dut.clk) 
    cocotb.log.info("HERE")
    cocotb.log.info(dut.seq_seen.value)

    # dut.inp_bit = 0
    # await FallingEdge(dut.clk)
    # dut.inp_bit = 1
    # await FallingEdge(dut.clk)
    # dut.inp_bit = 1
    # await FallingEdge(dut.clk)    
    # dut.inp_bit = 0
    # await FallingEdge(dut.clk)
    # dut.inp_bit = 1
    # await FallingEdge(dut.clk)
    # dut.inp_bit = 1
    # await FallingEdge(dut.clk) 

    cocotb.log.info(dut.next_state.value)
    cocotb.log.info(dut.seq_seen.value)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    assert dut.seq_seen.value == 1, f"Sequence detector result is incorrect for input"
