# MUX Design Verification

![image](https://user-images.githubusercontent.com/46755232/182206490-a1e66337-a235-4c15-b7c1-cc17f1c68166.png)

## Verification Environment

The test drives inputs to the Design Under Test (adder module here) which takes in 31 2-bit inputs  and gives 2-bit output.

The values are assigned to the input port using:

 for i in range (0,31):
        dut.sel.value = i  
        InputVal = random.randint(0,3)
        str1 =  "inp" + str(i)
        if i != 30:
            dut._id(str1,extended = False).value = InputVal
            
The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:            

AssertionError: Mux result is incorrect: Sel Value 12 |  Input value = 11 | OuptValue = 00 |  Expected Value 11

## Test Scenario

31 random 2-bit inputs: InputVal = random.randint(0,3)
Sel Value 12 |  Input value = 11 | 
OuptValue = 00 | 
Expected Value 11

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

      5'b01101: out = inp12; ====>BUG
      5'b01101: out = inp13;
      5'b01110: out = inp14;
      
The logic should be   5'b01100: out = inp12;

## Design Fix

![image](https://user-images.githubusercontent.com/46755232/182208595-26f3b041-1786-445e-9ff7-fc4ef859f22d.png)

The updated design is checked in as mux_fix.v

## Verification Strategy
The design is tested for random values of inputs at 31 inputs. All 31 cases were tested and it failed at the 12th and 13th input and did not match the input value given at 12th data input.

## Is the verification complete ?
yes
