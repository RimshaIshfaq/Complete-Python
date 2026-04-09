import logging


# logging settings

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Appname")

def add(a,b):
    result = a + b
    logger.debug(f"Adding {a} and {b} to get {result}")
    return result

def subtract(a,b):
    result = a - b
    logger.debug(f"Subtracting {b} from {a} to get {result}")
    return result

def multiply(a,b):
    result = a * b
    logger.debug(f"Multiplying {a} and {b} to get {result}")
    return result

def divide(a,b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} by {b} to get {result}")
        return result
    except ZeroDivisionError as e:
        logger.error(f"Error dividing {a} by {b}: {e}")
        return None
    
add(10,14)
subtract(10,14)
multiply(10,14)
divide(10,0)



    
