#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument

import sys


def print_usage():
    """Print usage and exit"""
    sys.stderr.write("usage: python throw_err.py <error type>\n")
    sys.stderr.write("available errors: \n")
    sys.stderr.write("\tassertion, io, import, index\n")
    sys.stderr.write("\tkey, name, os, type, value,\n")
    sys.stderr.write("\tattribute, eof, unbound, generatorexit,\n")
    sys.stderr.write("\tzerodivision\n")
    sys.exit()

# Check args
if len(sys.argv) != 2:
    print_usage()

error_type = sys.argv[1]

if error_type == "assertion":
    assert False, 'The assertion failed'
elif error_type == "io":
    f = open('/does/not/exist', 'r')
elif error_type == "import":
    import module_does_not_exist
elif error_type == "index":
    my_seq = [ 0, 1, 2 ]
    print my_seq[3]
elif error_type == "key":
    d = { 'a':1, 'b':2 }
    print d['c']
elif error_type == "name":
    def func():
	print unkown_name
	
    func()
elif error_type == "os":
    import os
    for i in range(10):
	print i, os.ttyname(i)
elif error_type == "type":
    result = ('tuple',) + 'string'
elif error_type == "value":
    print chr(1024)
elif error_type == "zerodivision":
    1 / 0 
elif error_type == "attribute":
	class NoAttributes(object):
		pass

	o = NoAttributes()
	print o.attribute
elif error_type == "eof":
	while True:
		data = input('prompt:')
		print 'READ:', data
elif error_type == "unbound":
	def throws_global_name_error():
		print unknown_global_name

	def throws_unbound_local():
		local_val = local_val + 1
		print local_val

	try:
		throws_global_name_error()
	except NameError, err:
		print 'Global name error:', err

	try:
		throws_unbound_local()
	except UnboundLocalError, err:
		print 'Local name error:', err
elif error_type == "generatorexit":
	def my_generator():
   		try:
   	    		for i in range(5):
  	         		print 'Yielding', i
				yield i
  	 	except GeneratorExit:
  	     		print 'Exiting early'

	g = my_generator()
	print g.next()
	g.close()
else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()
