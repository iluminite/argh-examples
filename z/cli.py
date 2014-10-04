import argh
from argh.decorators import arg


@arg('-m', '--myarg', help='Test arg.', default=True)
def cmd(**kwargs):
    print 'my arg: ', kwargs['myarg']


@arg('-m', '--myarg', help='Test arg.', default=True)
def load(**kwargs):
    print 'loading: ', kwargs['myarg']


@arg('-m', '--myarg', help='Test arg.', default=True)
def dump(**kwargs):
    print 'dumping: ', kwargs['myarg']
