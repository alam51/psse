# File:"C:\Program Files (x86)\PTI\PSSE33\EXAMPLE\my_automation.py", generated on SUN, AUG 15 2021  13:46, release 33.04.00
import psse33
import psspy
psspy.psseinit()
psspy.read(0,r"""C:\Users\hE\Downloads\IEEE 14 bus.raw""")
psspy.fnsl([0,0,0,1,1,1,99,0])
