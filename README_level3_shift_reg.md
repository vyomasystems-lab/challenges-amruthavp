# Bidirectional shift register Design Verification

A bidirectional shift register is a type of register which can have its contents shifted to the left or right.

![image](https://user-images.githubusercontent.com/46755232/182200758-f276857e-95d4-4674-9e67-e5b10fa3d1a5.png)

## Verification Environment
The test drives inputs to the Design Under Test which takes in 4 data inputs *D*, clock input and 2 select inputs *S* and gives 4-bit shifted output 

The values are assigned to the input port using 

    S=[[0,0],[1,0]]
    data=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
    
    
The assert statement is used for comparing the register's outut to the expected value.

The following error is seen:

Before shift
0 0 0 0 0 1
After shift
0 0 0 0 1 0
Before shift
0 0 0 0 1 0
After shift
0 0 0 0 0 0
Expected: 0 0 1 0
Acutal Output: 0 0 0 0
Before shift
0 0 0 1 0 0
After shift
0 0 1 1 0 0
Expected: 0 0 0 1
Acutal Output: 0 0 1 1
Before shift
0 0 1 0 0 0
After shift
0 0 0 0 0 1
Before shift
0 0 1 1 1 0
After shift
0 0 1 1 0 1
Before shift
0 0 1 1 0 1
After shift
0 0 1 1 1 1
Expected: 1 1 0 1
Acutal Output: 1 1 1 1
Before shift
0 0 1 0 1 1
After shift
0 0 0 0 1 1
Expected: 1 1 1 0
Acutal Output: 1 1 0 0
Before shift
0 0 0 1 1 1
After shift
0 0 1 1 1 0
Before shift
1 0 0 0 0 1
After shift
1 0 1 0 0 0
Before shift
1 0 0 0 1 0
After shift
1 0 0 0 0 1
Before shift
1 0 0 1 0 0
After shift
1 0 0 0 1 0
Before shift
1 0 1 0 0 0
After shift
1 0 0 1 0 0
Before shift
1 0 1 1 1 0
After shift
1 0 0 1 1 1
Before shift
1 0 1 1 0 1
After shift
1 0 1 1 1 0
Before shift
1 0 1 0 1 1
After shift
1 0 1 1 0 1
Before shift
1 0 0 1 1 1
After shift
1 0 1 0 1 1
fail_cnt 4
475000.00ns INFO     AssertionError: Number of test cases failed 4

## Test Scenario

Test input: D3 D2 D1 D0: 0 0 1 0

Expected output: Q3 Q2 Q1 Q0: 0 0 1 0

Actual output: Q3 Q2 Q1 Q0: 0 0 0 0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

   multiplexer_4_1 #(1) mux0(X0, Q3, Q1, Q0, D0, S1, S0);   
   d_flip_flop_edge_triggered dff0(Q0, Q0n, CLK, X0);
   multiplexer_4_1 #(1) mux1(X1, Q0, Q2, Q1, D1, S1, S0);   
   d_flip_flop_edge_triggered dff1(Q1, Q1n, CLK, X1);
   multiplexer_4_1 #(1) mux2(X2, Q2, Q3, Q2, D2, S1, S0); =========> BUG   
   d_flip_flop_edge_triggered dff2(Q2, Q2n, CLK, X2);
   multiplexer_4_1 #(1) mux3(X3, Q2, Q0, Q3, D3, S1, S0);   
   d_flip_flop_edge_triggered dff3(Q3, Q3n, CLK, X3);


The multiplexer should have gotten an input through feedback from Q1

## Design Fix
Updating the design and re-running the test makes the test pass.

Before shift
0 0 0 0 0 1
After shift
0 0 0 0 1 0
Before shift
0 0 0 0 1 0
After shift
0 0 0 1 0 0
Before shift
0 0 0 1 0 0
After shift
0 0 1 0 0 0
Before shift
0 0 1 0 0 0
After shift
0 0 0 0 0 1
Before shift
0 0 1 1 1 0
After shift
0 0 1 1 0 1
Before shift
0 0 1 1 0 1
After shift
0 0 1 0 1 1
Before shift
0 0 1 0 1 1
After shift
0 0 0 1 1 1
Before shift
0 0 0 1 1 1
After shift
0 0 1 1 1 0
Before shift
1 0 0 0 0 1
After shift
1 0 1 0 0 0
Before shift
1 0 0 0 1 0
After shift
1 0 0 0 0 1
Before shift
1 0 0 1 0 0
After shift
1 0 0 0 1 0
Before shift
1 0 1 0 0 0
After shift
1 0 0 1 0 0
Before shift
1 0 1 1 1 0
After shift
1 0 0 1 1 1
Before shift
1 0 1 1 0 1
After shift
1 0 1 1 1 0
Before shift
1 0 1 0 1 1
After shift
1 0 1 1 0 1
Before shift
1 0 0 1 1 1
After shift
1 0 1 0 1 1
475000.00ns INFO     test_seq_bug1 passed
475000.00ns INFO     **************************************************************************************
                     ** TEST                          STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
                     **************************************************************************************
                     ** test_shift_reg.test_seq_bug1   PASS      475000.00           0.02   31007990.60  **
                     **************************************************************************************
                     ** TESTS=1 PASS=1 FAIL=0 SKIP=0             475000.00           0.03   16149460.99  **
                     **************************************************************************************
                     
## Verification Strategy
The design is verified for 8 cases of shift left and 8 cases of shift right covering the entire range of test senarios. The test failed for 4 shift left cases, so error must be when s0s1="00". The 4 senarios accured while there was a transfer from D3 to D2, hence the bug must be in the 3rd multiplexer.

## Is the verification complete ?
With the above explanation the verification is complete.
