#sprawdz czy jakiś element np 30 znajduje się w liście . sprawdz która opcja szybciej to obliczy.

import time

def function_performance(func, arg, how_many_times = 1):
    sum = 0
    for i in range(0,how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end - start)

    return sum
#jeśli mamy przeszukać listę to warto wybrać {}
set_container = {i for i in range(1000)} #będzie szybciej
list_container = [i for i in range(1000)]

def is_element_in(what_value):
    if what_value in set_container:
        return True
    else:
        return False

print(function_performance(is_element_in, 450, how_many_times=30000))



