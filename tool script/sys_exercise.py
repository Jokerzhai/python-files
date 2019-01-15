import sys
def exitfunc(value):
    print value
    sys.exit(0)
print "Hello"

try:
    sys.exit(1)
except SystemExit,value:
    exitfunc(value)

print "come?"