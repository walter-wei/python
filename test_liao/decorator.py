import functools

'''
def now():
	print('2016-8-13')
f = now
f()
'''

def logc(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			func(*args, **kw)
			print('end call():')
		return wrapper
	if hasattr(text, '__call__'):
		func=text
		text='call'
		return decorator(func)
	else:
		return decorator


def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@logc('execute')
def now():
	print('20160813')

now()
