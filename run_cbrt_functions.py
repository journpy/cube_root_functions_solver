from cube_root_functions_loop import CubeRootFunctionsLoop
from datetime import datetime


date_and_time = datetime.now()
print(f"\nToday's date and current time is {date_and_time}.\n")

crfl = CubeRootFunctionsLoop(a='', c='', h='', k='')
crfl.main_loop()

