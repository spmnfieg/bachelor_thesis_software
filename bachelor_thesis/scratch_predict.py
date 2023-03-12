from executor import *
import time
from datetime import datetime

if __name__ == '__main__':


    st = datetime.utcnow()
    generate_project_results()
    et = datetime.utcnow()
    elapsed_time = et-st
    print('Execution time:', elapsed_time)

    #Runtime File
    with open('runtime.txt', 'a') as f:
        f.write(str(elapsed_time))
        f.write("\n")
