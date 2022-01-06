# File:"C:\Program Files (x86)\PTI\PSSE33\EXAMPLE\my_automation.py", generated on SUN, AUG 15 2021  13:46,
# release 33.04.00
import os
import sys

psse_path = r'C:\Program Files (x86)\PTI\PSSE33\PSSBIN'
sys.path.append(psse_path)
os.environ['PATH'] += ';' + psse_path

"""Importing from PSSE path"""
import psspy, redirect

psspy.throwPsseException = True
_i = psspy.getdefaultint()  # in place of default integer values, the variable _i is used
_f = psspy.getdefaultreal()  # in place of default float values, the variable _f is used.
_s = psspy.getdefaultchar()  # in place of default string values (not filenames) the variable _s is used.

redirect.psse2py()
psspy.psseinit(100)  # starting bus size of 100
sav_path = r'C:\Program Files (x86)\PTI\PSSE33\EXAMPLE\savnw.sav'
psspy.case(sav_path)
psspy.fnsl()
print('Iteration number:%s' % psspy.iterat())
# psspy.read(0, r"""C:\Users\hE\Downloads\IEEE 14 bus.raw""")
# psspy.fnsl([0, 0, 0, 1, 1, 1, 99, 0])
a = 5
bus_no_list = psspy.abusint(string='NUMBER')
bus_area_list = psspy.abusint(string='AREA')
b = 4
ierr, volt_pu_mag_list = psspy.abusreal(-1, string='PU')
ierr, volt_complex_list = psspy.abuscplx(-1, string='VOLTAGE')
c = 5
h = help(psspy)
h1 = str(h)
with open('PSSPY Reference.txt', 'w') as txt_file:
    txt_file.write(h1)

