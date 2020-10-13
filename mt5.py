import platform
system = platform.system()

if system == 'Windows':
    from linux import *
else:
    pass