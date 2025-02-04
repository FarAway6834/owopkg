from subpr.lib import subpr
from sys import argv as _a

python = lambda x : subpr(f'python {x}')
cmds = dict(
    build = lambda a: python(f'setup.py sdist {a}'),
    deploy = lambda a: python('-m twine upload dist/*')
)

def main(*argv, _a = _a):
    L = len(argv)
    if L - 1:
        a = list(argv)
        f = cmds[a.pop(0)]
        f(' '.join(a))
    elif L: main(None, input('mode : '))
    else: main(*_a)

if __name__ == "__main__" : main()