Just illustrating how ternry Boolean should behave
**************************************************

In electronics we have 3 states : 

* HV : High Voltage which is True
* LV : Low Voltage wich is Fale
* Z : high impendance or undefined. 

This is useful for protocol like I2C since it enables bi-directional communications on a single wire. 

Is there a use for Z in CS ? 
****************************

Well, knowing that a boolean equation has a solution whatever the input is can be nice. 

At least it is consistent. 

http://en.wikipedia.org/wiki/Three-valued_logic

 TESTING OPERATION NOT
 ----------------
 True    |False
 False   |True
 undef   |undef
 ****************************************
 TESTING OPERATION AND
     True    |False  |undef
 ------------------------------
 True    |True   |False  |undef
 ------------------------------
 False   |False  |False  |False
 ------------------------------
 undef   |undef  |False  |undef
 ****************************************
 TESTING OPERATION XOR
     True    |False  |undef
 ------------------------------
 True    |False  |True   |undef
 ------------------------------
 False   |True   |False  |undef
 ------------------------------
 undef   |undef  |undef  |undef
 ****************************************
 TESTING OPERATION OR
     True    |False  |undef
 ------------------------------
 True    |True   |True   |True
 ------------------------------
 False   |True   |False  |undef
 ------------------------------
 undef   |True   |undef  |undef
 

