# BIT MANIPULATION COPROCESSOR 

![image](https://user-images.githubusercontent.com/46755232/182213177-054868af-f987-404d-802d-c006e2059988.png)

The test drives inputs to the Design Under Test which takes in 4 32-bit inputs AND GIVES OUT 32 BIT OUTPUT

The values are assigned to the input port using
    
    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x5
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x4007033

    SRC1_Values = map(''.join, product('0123456789ABCDEF', repeat=8))
    SRC2_Values = map(''.join, product('0123456789ABCDEF', repeat=8))
    SRC3_Values = map(''.join, product('0123456789ABCDEF', repeat=8))
    Instruction = map(''.join, product('0123456789ABCDEF', repeat=2))


The assert statement is used for comparing the adder's outut to the expected value.

The following error is seen:
 error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message
    
## Test Scenario
    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x5
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x4007033
    DUT =0xb
    Actual output: 0x1
    
    
 # Design Bug
Based on the above test input and analysing the design, we see the following

AssertionError: Value mismatch DUT = 0xb does not match MODEL = 0x1

## Design Fix
Updating the design and re-running the test makes the test pass.


## Verification Strategy

## Is the verification complete ?
