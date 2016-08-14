
'a test module'

__author__ = 'wei xuke'

import sys 

def test():
	args = sys.argv
	if len(args) == 1:
		print('Hello World')
	elif len(args) == 2:
		print('Hello World %s!' % args[1])
	else:
		print('Too many parameters')

if __name__ == '__main__':
	test()


