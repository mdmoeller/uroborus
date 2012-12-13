import urotest

euclid = urotest.uro_import('euclid')


def ten(R):
    g0 = euclid.gcd(10, 10)

    R.assertTrue( g0 == 10 ) # Should be a PASS


def hundred(R):
    g1 = euclid.gcd(100, 1000) 

    R.assertTrue( g1 == 100 ) # Should PASS

def primes(R):
    g2 = euclid.gcd(17, 19)

    R.assertTrue( g2 == 1 ) # Should PASS

def bigprimes(R):
    g3 = euclid.gcd(192, 480) 

    R.assertTrue( g3 == 96 ) # Should PASS
