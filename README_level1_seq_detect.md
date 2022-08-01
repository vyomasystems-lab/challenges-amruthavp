# SEQUENCE DETECTOR 

![image](https://user-images.githubusercontent.com/46755232/182209882-5e037448-b025-44c4-9cba-1b34c1ae09b1.png)

## Verification Environment

The test drives inputs to the Design Under Test (adder module here) which takes in 1-bit inputs inp and gives 1 bit output to check if sequence was detected.

The values are assigned to the input port using 

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
    
    
  The assert statement is used for comparing the adder's outut to the expected value.
  
  assert dut.seq_seen.value == 1, f"Sequence detector result is incorrect for input"
     
 ## Test Scenario
 
 input: 101011
 expected ouput seq_seen : 1
 actual ouput : 0
 
 Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE; ======>BUG     -----------> SHOULD HAVE BEEN SEQ1
        else
          next_state = SEQ_10;
      end
      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE;
      end
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE; =====>BUG   -----------> SHOULD HAVE BEEN SEQ10
          
          
          
## Design Fix
Updating the design and re-running the test makes the test pass.
          
![image](https://user-images.githubusercontent.com/46755232/182211696-caab49b9-7cca-4e45-93a2-cc069e7b36d3.png)
          
 
The updated design is checked in as test_seq_fix.v

## Verification Strategy
The sequence input was given and tested. Next the sequence with overlap was tested. This failed due to improper FSM. when the current state was SEQ1, for it to handle overlap case it should stay in the SEQ1 state.
Similarly when inp_bit is 0, the next state for SEQ101 should be SEQ10.

## Is the verification complete ?
   YES
     
    
    
    
    
  
    
