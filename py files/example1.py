Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print "Hello world"
Hello world
>>> principal = 1000
>>> rate = 0.05
>>> numyears = 5
>>> year = 1
>>> while year <= numyears:
	principal = principal * (1 + rate)
	print "%3d %0.2f" % (year,principal)
	year += 1
	
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 
