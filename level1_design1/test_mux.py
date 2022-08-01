# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random



@cocotb.test()
async def test_mux(dut):
   # sel = 13
    # int12 = 3
    # int13 = 1
    # dut.sel.value= sel
    # dut.inp12.value= int12
    # dut.inp13.value = int13
    # dut.inp0.value= 0
    # dut.inp1.value = 1
    # dut.inp2.value= 2
    # dut.inp3.value = 3
    # dut.inp4.value= 0
    # dut.inp5.value = 1
    # dut.inp6.value= 2
    # dut.inp7.value = 3
    # dut.inp8.value= 0
    # dut.inp9.value = 1
    # dut.inp10.value= 2
    # dut.inp11.value = 3
    # dut.inp12.value= 0
    # dut.inp13.value = 1
    # dut.inp14.value= 2
    # dut.inp15.value = 3
    # dut.inp16.value= 0
    # dut.inp17.value = 1
    # dut.inp18.value= 2
    # dut.inp19.value = 3
    # dut.inp20.value= 0
    # dut.inp21.value = 1
    # dut.inp22.value= 2
    # dut.inp23.value = 3
    # dut.inp24.value= 0
    # dut.inp25.value = 1
    # dut.inp26.value= 2
    # dut.inp27.value = 3
    # dut.inp28.value= 0
    # dut.inp29.value = 1
    # dut.inp30.value= 2
    # x=["inp0","inp1"]
    # for i in range (0,30):
    #     sel = i
    #     dut.sel.value= sel
    #     # x[i]=random.randint(0,3)
    #     # cocotb.log.info(x[i])
    #     cocotb.log.info(dut.inp0.value)
    #     # dut.inp12.value= int12
    #     # dut.inp13.value = int13
    #     await Timer(2, units='ns')
    #     cocotb.log.info(i%4)
    #     assert dut.out.value == i%4, f"Adder result is incorrect for input {i}: {dut.out.value} != {i%4}"




    for i in range (0,31):
        dut.sel.value = i  
        InputVal = random.randint(0,3)
        str1 =  "inp" + str(i)
        if i != 30:
            dut._id(str1,extended = False).value = InputVal
            await Timer(2, units='ns')
            # print(dut.sel.value, InputVal, dut.out.value,dut._id(str1,extended = False).value)
            assert dut.out.value == InputVal , f"Mux result is incorrect: Sel Value {i} |  Input value = {dut._id(str1,extended = False).value} | OuptValue = {dut.out.value} |  Expected Value {dut._id(str1,extended = False).value}"
        else:
            dut._id(str1,extended = False).value =0 
            await Timer(2, units='ns')
            # print(dut.sel.value, InputVal, dut.out.value,dut._id(str1,extended = False).value)
            assert dut.out.value == 0 , f"Mux result is incorrect: Sel Value {i} | Input value = {dut._id(str1,extended = False).value} | OuptValue = {dut.out.value} |  Expected Value {dut._id(str1,extended = False).value}"

