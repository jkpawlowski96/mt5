import platform
system = platform.system()

if system == 'Linux':
    from linux import *
else:
    pass
