# local scope
# enclosing scope
# global scope
# built in scope
my_global=10
def fn1():
    enclosed_var=5
    print("Inside function: my_global is",my_global)
    def fn2():
        local_v=6
        print("In nested function:")
        print("Enclosed variable: ",enclosed_var)
    fn2()
fn1()
