#waf that takes one input perameter(n)and evaluates an expressiona=n*10,for all values between 0 to n?
import time
ns=[12312312,23423423,24234234,234534]
n=10000
def evaluate_expression(n):
    for i in range(n+1):
        a = i * 10
        #extimate excution time of this function for n
        def wrapper(func,*args,**kwargs):
            def wrapped(*args,**kwargs):
                start_time = time.time()*1000000
                func(*args,**kwargs)
                end_time = time.time()*1000000
                print(f"for n={n}\nExecution time is{end_time - start_time}micro seconds")
                wrapped(*args,**kwargs)
                n=1000000
                wrapped_fn =wrapper(evaluate_expression,n)
                wrapped_fn(n)