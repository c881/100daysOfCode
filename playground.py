# def add(*args):
#     total = 0
#     for item in args:
#         total += item
#     return total
#
#
# print(add(1, 2, 3, 4, 2.4, 5, 7, 9, 6, -1.2))
#
# def compute(n, **kwargs):
#     if kwargs["multi"] != None:
#         n *= kwargs["multi"]
#     if kwargs["add"] != None:
#         n += kwargs["add"]
#     return n
#
# print(compute(4, multi=5, add=3, sub=2))
# old_len = len
# # len = lambda x: 0
# len = lambda x: old_len(x) * 2
# print(len("Hello"))

def create_logger(logger_name):
    def log(message):
        print(f"[{logger_name}] {message}")
    return log

log_error = create_logger("Errors")
log_system = create_logger("System")
log_error("CRITICAL FAILURE: Can't find Nemo.")
log_system("Chop Suey")


# def calc1(num1, num2):
#     def mul():
#         return num1 * num2
#     def div():
#         return num1 / num2
#     def add():
#         return num1 + num2
#     def sub():
#         return num1 - num2
#     return {'mul': mul(), 'div': div(),'add': add(), 'sub': sub()}

# print(calc1(5, 6))
        
def debug(f, *args, **kwargs):
    def wrap_func(*args, **kwargs):
        print("Start")
        return_vals = f(*args, **kwargs)
        print("end")
        return return_vals
    return wrap_func

