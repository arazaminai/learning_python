import time, sys

indent = 0
indent_increasing = True

try:
    while True:  #main program loop
        print(" " * indent, end="")
        print("********")
        time.sleep(0.05)

        if indent_increasing:
            indent += 1
            if indent == 30:
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()