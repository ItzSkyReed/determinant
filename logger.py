import time
def logger(type,error,obj):
    print(f'[{time.strftime("%X", time.localtime())}][{type.upper()}] {error} // {obj}')