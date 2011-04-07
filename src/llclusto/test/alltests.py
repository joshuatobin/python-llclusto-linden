
if __name__ == '__main__':

    import os
    import sys


    sys.path.append(os.path.realpath('.'))


import unittest
import llclusto.test


def gettests(tests=None):
    if not tests:
        tests = ('llclusto.test.drivers',)

    suite = unittest.defaultTestLoader.loadTestsFromNames(tests)

    return suite


def runtests(tests=None, db='sqlite:///:memory:', echo=False):

    llclusto.test.testbase.DB=db
    llclusto.test.testbase.ECHO=echo
    suite = gettests(tests)
    print suite
    runner = unittest.TextTestRunner()    
    runner.run(suite)




if __name__ == '__main__':

    import optparse

    parser = optparse.OptionParser()
    parser.add_option('--db', dest='dsn', 
                      help='specifies which db to test against',
                      default='sqlite:///:memory:')
    parser.add_option('--echo', dest='echo', action='store_true', default=False,
                      help="Echo sqlalchemy sql")
    
    (options, args) = parser.parse_args()
    runtests(args, options.dsn, options.echo)
