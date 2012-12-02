from negadecimal_instrumented import *
import negadecimal_instrumented as negadecimal
target_module = negadecimal

class TestNegadecimal():

    def test_to_negadecimal(R):
        R.assertTrue('192'== negadecimal.to_negadecimal(12))
        R.assertTrue('0'== negadecimal.to_negadecimal(0))
        R.assertTrue('9'== negadecimal.to_negadecimal(9))
        R.assertTrue('190' == negadecimal.to_negadecimal(10))
        R.assertTrue('19' == negadecimal.to_negadecimal(-1))
        R.assertTrue('10' == negadecimal.to_negadecimal(-10))

    def test_to_decimal(R):
        for i in range(-110, 110):
            R.assertTrue(i == negadecimal.to_decimal(negadecimal.to_negadecimal(i)))

    def test_add(R):
        check_all(R, negadecimal.add,
            [(5, 100, 105), (5, -100, -95), (-5, 100, 95),
             (-5, -100, -105), (0, 5, 5), (1, -1, 0)])
        
    def test_subtract(R):
        check_all(R, negadecimal.subtract,
            [(5, 100, -95), (5, -100, 105), (-5, 100, -105),
             (-5, -100, 95), (0, 5, -5), (1, 1, 0)])
        
    def test_multiply(R):
        check_all(R, negadecimal.multiply,
            [(5, 50, 250), (5, -50, -250), (-5, 50, -250),
             (-5, -50, 250), (0, 5, 0), (1, 1, 1)])
        
    def test_divide(R):
        check_all(R, negadecimal.divide,
            [(220, 50, 4), (220, -50, -5), (-220, 50, -5),
             (-220, -50, 4), (0, 5, 0), (1, 1, 1)])

#    def test_divide_error(R):
#        R.assertRaises(ZeroDivisionError, divide, '1', '0')
        
    def test_remainder(R):
        check_all(R, negadecimal.remainder,
            [(220, 50, 20), (220, -50, -30), (-220, 50, 30),
             (-220, -50, -20), (0, 5, 0), (1, 1, 0)])

#    def test_remainder_error(R):
#        R.assertRaises(ZeroDivisionError, remainder, '1', '0')

    def test_negate(R):
        neg1 = negadecimal.to_negadecimal(20)
        neg2 = negadecimal.to_negadecimal(-20)
        R.assertTrue(neg1 == negadecimal.negate(neg2))
        R.assertTrue(neg2 == negadecimal.negate(neg1))
        R.assertTrue(neg2 == negadecimal.fetch())
        R.assertTrue('0' == negadecimal.negate('0'))

    def test_evaluate(R):
        R.assertTrue('104' == negadecimal.evaluate('119 + 5'))
        R.assertTrue('119' == negadecimal.evaluate('104 - 5'))
        R.assertTrue('35' == negadecimal.evaluate('5 * 15'))
        R.assertTrue('5' == negadecimal.evaluate('35 / 15'))
        R.assertTrue('2' == negadecimal.evaluate('100 % 7'))
        R.assertTrue('1900' == negadecimal.evaluate('-100'))
        R.assertTrue('192' == negadecimal.evaluate('neg 12'))

    def test_evaluate_always_returns_a_string(R):   
        R.assertTrue('12' == negadecimal.evaluate('dec 192'))

    def test_evaluate_handles_blanks_correctly(R):
        R.assertTrue('4' == negadecimal.evaluate('2+2'))   
        R.assertTrue('4' == negadecimal.evaluate('   2   +   2  '))
        R.assertTrue('4' == negadecimal.evaluate('  6   -2  '))

    def test_store_and_fetch(R):
        store('193')
        R.assertTrue('193' == negadecimal.fetch())

##    def test_get_ndn(R):
##        R.assertTrue('123' == evaluate('123'))
##        R.assertTrue('123' == evaluate(' 123  '))
##        R.assertFalse(evaluate('abc').isdigit())

    # ------------------- Helper functions ------------------

    def check_all(R, fun, triples):
        for (arg1, arg2, expected) in triples:
            check(R, fun, arg1, arg2, expected)
                    
    def check(R, fun, arg1, arg2, expected):
        neg_arg1 = negadecimal.to_negadecimal(arg1)
        neg_arg2 = negadecimal.to_negadecimal(arg2)
        neg_expected = negadecimal.to_negadecimal(expected)
        R.assertTrue(neg_expected == fun(neg_arg1, neg_arg2))
        R.assertTrue(neg_expected == negadecimal.fetch())
        
