import urotest

negadecimal = urotest.uro_import('negadecimal')


def test_to_negadecimal(R):
    R.assertEquals('192', negadecimal.to_negadecimal(12))
    R.assertEquals('0', negadecimal.to_negadecimal(0))
    R.assertEquals('9', negadecimal.to_negadecimal(9))
    R.assertEquals('190', negadecimal.to_negadecimal(10))
    R.assertEquals('19', negadecimal.to_negadecimal(-1))
    R.assertEquals('10', negadecimal.to_negadecimal(-10))

def test_to_decimal(R):
    for i in range(-110, 110):
        R.assertEquals(i, negadecimal.to_decimal(negadecimal.to_negadecimal(i)))

def test_add(R):
    nega_tester.check_all(R, negadecimal.add,
        [(5, 100, 105), (5, -100, -95), (-5, 100, 95),
         (-5, -100, -105), (0, 5, 5), (1, -1, 0)])
    
def test_subtract(R):
    nega_tester.check_all(R, negadecimal.subtract,
        [(5, 100, -95), (5, -100, 105), (-5, 100, -105),
         (-5, -100, 95), (0, 5, -5), (1, 1, 0)])
    
def test_multiply(R):
    nega_tester.check_all(R, negadecimal.multiply,
        [(5, 50, 250), (5, -50, -250), (-5, 50, -250),
         (-5, -50, 250), (0, 5, 0), (1, 1, 1)])

def test_divide(R):
    nega_tester.check_all(R, negadecimal.divide,
        [(220, 50, 4), (220, -50, -5), (-220, 50, -5),
         (-220, -50, 4), (0, 5, 0), (1, 1, 1)])


# No equivalent UROBORUS test (yet)
"""
def test_divide_error(R):
    R.assertRaises(ZeroDivisionError, divide, '1', '0')
    """
    
def test_remainder(R):
    nega_tester.check_all(R, negadecimal.remainder,
        [(220, 50, 20), (220, -50, -30), (-220, 50, 30),
         (-220, -50, -20), (0, 5, 0), (1, 1, 0)])

# No equivalent UROBORUS test (yet)
"""
def test_remainder_error(R):
    R.assertRaises(ZeroDivisionError, remainder, '1', '0')
    """

def test_negate(R):
    neg1 = negadecimal.to_negadecimal(20)
    neg2 = negadecimal.to_negadecimal(-20)
    R.assertEquals(neg1, negadecimal.negate(neg2))
    R.assertEquals(neg2, negadecimal.negate(neg1))
    R.assertEquals(neg2, negadecimal.fetch())
    R.assertEquals('0', negadecimal.negate('0'))

def test_evaluate(R):
    R.assertEquals('104', negadecimal.evaluate('119 + 5'))
    R.assertEquals('119', negadecimal.evaluate('104 - 5'))
    R.assertEquals('35', negadecimal.evaluate('5 * 15'))
    R.assertEquals('5', negadecimal.evaluate('35 / 15'))
    R.assertEquals('2', negadecimal.evaluate('100 % 7'))
    R.assertEquals('1900', negadecimal.evaluate('-100'))
    R.assertEquals('192', negadecimal.evaluate('neg 12'))

def test_evaluate_always_returns_a_string(R):   
    R.assertEquals('12', negadecimal.evaluate('dec 192'))

def test_evaluate_handles_blanks_correctly(R):
    R.assertEquals('4', negadecimal.evaluate('2+2'))   
    R.assertEquals('4', negadecimal.evaluate('   2   +   2  '))
    R.assertEquals('4', negadecimal.evaluate('  6   -2  '))

def test_store_and_fetch(R):
    negadecimal.store('193')
    R.assertEquals('193', negadecimal.fetch())

##    def test_get_ndn(R):
##        R.assertEquals('123', evaluate('123'))
##        R.assertEquals('123', evaluate(' 123  '))
##        R.assertFalse(evaluate('abc').isdigit())

# ------------------- Helper functions ------------------
class nega_tester:

    @staticmethod
    def check_all(R, fun, triples):
        for (arg1, arg2, expected) in triples:
            nega_tester.check(R, fun, arg1, arg2, expected)
                    
    @staticmethod
    def check(R, fun, arg1, arg2, expected):
        neg_arg1 = negadecimal.to_negadecimal(arg1)
        neg_arg2 = negadecimal.to_negadecimal(arg2)
        neg_expected = negadecimal.to_negadecimal(expected)
        R.assertEquals(neg_expected, fun(neg_arg1, neg_arg2))
        R.assertEquals(neg_expected, negadecimal.fetch())
    
# unittest.main()
