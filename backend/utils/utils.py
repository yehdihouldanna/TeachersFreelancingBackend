from termcolor import cprint
import inspect


cprint("+-------------------------------+" , color="blue")
cprint("| This thread uses debug utils  |" , color="blue")
cprint("+-------------------------------+" , color="blue")

def dprint(variable):
    "prints the variable and the function in which it is called"
    cprint("[DEBUG] " , color = "green" , end="")
    cprint(inspect.stack()[1][0].f_code.co_name, color = "cyan", end =" ")
    print(variable)

# TODO add custom prints based on variable type (lists,dicts,...)

def tprint_OK():
    cprint("[Testing] " , color = "yellow" , end="")
    cprint(inspect.stack()[1][0].f_code.co_name, color = "cyan", end =" ")
    print(" ...",end =" ")
    cprint("[OK!]",color="green",attrs=["bold"])
    
def tprint_FAIL():
    "prints the variable that is called"
    cprint("[Testing] " , color = "yellow" , end="")
    cprint(inspect.stack()[1][0].f_code.co_name, color = "cyan", end =" ")
    print(" ...",end =" ")
    cprint("[FAILED!]",color="red",attrs=["bold"])