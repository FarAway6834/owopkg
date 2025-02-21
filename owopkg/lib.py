import builtins as __builtins__
from subpr.lib import _subpr
from sys import argv as _a
__builtins__.maingen = lambda globalsv, __name__, cmd : globalsv.setitem('main', (main() if __name__ == "__main__" else main)(lambda a=_a: _subpr(f'python -m owopkg {cmd} {' '.join(a[1:])}')()))