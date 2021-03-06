#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument

import sys, gc, weakref, os, argparse

available_errors = ["assertion", "io", "import", "index", "key",
			"name", "os", "type", "value", "attribute", 
			"overflow", "unbound", "reference", "zerodivision"]
parser = argparse.ArgumentParser()
parser.add_argument("error_type", choices = available_errors)
args = parser.parse_args()
error_type = args.error_type

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
elif error_type == "overflow":
	print 5.0**50000000000000
elif error_type == "unbound":

	local_val = local_val + 1
	print local_val

elif error_type == "reference":
	class ExpensiveObject(object):
		def __init__(self, name):
			self.name = name
		def __del__(self):
			print '(Deleting %s)' % self
	
	obj = ExpensiveObject('thing')
	p = weakref.proxy(obj)

	print 'BEFORE:', p.name
	obj = None
	print 'AFTER:', p.name

else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()
