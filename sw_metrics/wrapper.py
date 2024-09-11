from math_function import infinite

def wrapper(x):
    
    x = str(x).strip()
    if not x.isdigit():
        raise ValueError("Input should be integer without letters or space.")
    
    x = int(x)
    if x < 0:
        raise ValueError("Input should be a non-negative integer.")
    
    print("wrapper without errors")
    return infinite(x)