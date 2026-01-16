import logging

## logginh setting


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S' ,
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)


logger=logging.getLogger("ArithmeticApp")



def add(a,b):
    result=a+b
    logger.debug(f"Adding {a}+{b} ={result}")
    return result

def subtract(a,b):
    result=a-b
    logger.debug(f"Subtracting {a}-{b}={result}")
    return result

def multiply(a,b):
    result=a*b
    logger.debug(f"Multiplying {a}*{b}={result}")

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"Dividing {a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("division by zero error")
        return None 
    

add(10,45)
subtract(7,2)
multiply(7,8)
divide(20,0)