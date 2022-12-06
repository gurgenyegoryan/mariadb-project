import psutil
import time


def get_using_ram():
    j = 0
    ram_list = []
    f = open("text.txt", "a")
    while j < 10:
        ram_usage = psutil.virtual_memory()[3] / 1000000000
        time.sleep(0.1)
        f.write(str(ram_usage) + '\n')
        #ram_list.append(ram_usage)
        j += 1
    #return ram_list



print(get_using_ram())

