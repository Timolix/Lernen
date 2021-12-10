class Ex(Exception):
    pass

def foo():
    print("foo")
    raise NameError

try:
    foo()
    abc = 5/0
except Ex:
    print("Exception Detected")
except ZeroDivisionError:
    print("durch null geteilt")
except RuntimeError as detail:
    print("RuntimeError", detail)
except NameError:
    print("NameError")
except Exception:
    print("andere")
else:
    print("keine ex")

print("weiter gehts")