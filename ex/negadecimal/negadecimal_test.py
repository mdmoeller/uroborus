from negadecimal_instrumented import *
target_module=negadecimal

class TestNegadecimal(unittest.TestCase):

    def test_to_negadecimal(self):
        self.assertEqual('192', to_negadecimal(12))
        self.assertEqual('0', to_negadecimal(0))
        self.assertEqual('9', to_negadecimal(9))
        self.assertEqual('190', to_negadecimal(10))
        self.assertEqual('19', to_negadecimal(-1))
        self.assertEqual('10', to_negadecimal(-10))

    def test_to_decimal(self):
        for i in range(-110, 110):
            self.assertEqual(i, to_decimal(to_negadecimal(i)))

    def test_add(self):
        self.check_all(add,
            [(5, 100, 105), (5, -100, -95), (-5, 100, 95),
             (-5, -100, -105), (0, 5, 5), (1, -1, 0)])
        
    def test_subtract(self):
        self.check_all(subtract,
            [(5, 100, -95), (5, -100, 105), (-5, 100, -105),
             (-5, -100, 95), (0, 5, -5), (1, 1, 0)])
        
    def test_multiply(self):
        self.check_all(multiply,
            [(5, 50, 250), (5, -50, -250), (-5, 50, -250),
             (-5, -50, 250), (0, 5, 0), (1, 1, 1)])
        
    def test_divide(self):
        self.check_all(divide,
            [(220, 50, 4), (220, -50, -5), (-220, 50, -5),
             (-220, -50, 4), (0, 5, 0), (1, 1, 1)])

    def test_divide_error(self):
        self.assertRaises(ZeroDivisionError, divide, '1', '0')
        
    def test_remainder(self):
        self.check_all(remainder,
            [(220, 50, 20), (220, -50, -30), (-220, 50, 30),
             (-220, -50, -20), (0, 5, 0), (1, 1, 0)])

    def test_remainder_error(self):
        self.assertRaises(ZeroDivisionError, remainder, '1', '0')

    def test_negate(self):
        neg1 = to_negadecimal(20)
        neg2 = to_negadecimal(-20)
        self.assertEqual(neg1, negate(neg2))
        self.assertEqual(neg2, negate(neg1))
        self.assertEqual(neg2, fetch())
        self.assertEqual('0', negate('0'))

    def test_evaluate(self):
        self.assertEqual('104', evaluate('119 + 5'))
        self.assertEqual('119', evaluate('104 - 5'))
        self.assertEqual('35', evaluate('5 * 15'))
        self.assertEqual('5', evaluate('35 / 15'))
        self.assertEqual('2', evaluate('100 % 7'))
        self.assertEqual('1900', evaluate('-100'))
        self.assertEqual('192', evaluate('neg 12'))

    def test_evaluate_always_returns_a_string(self):   
        self.assertEqual('12', evaluate('dec 192'))

    def test_evaluate_handles_blanks_correctly(self):
        self.assertEqual('4', evaluate('2+2'))   
        self.assertEqual('4', evaluate('   2   +   2  '))
        self.assertEqual('4', evaluate('  6   -2  '))

    def test_store_and_fetch(self):
        store('193')
        self.assertEqual('193', fetch())

##    def test_get_ndn(self):
##        self.assertEqual('123', evaluate('123'))
##        self.assertEqual('123', evaluate(' 123  '))
##        self.assertFalse(evaluate('abc').isdigit())

    # ------------------- Helper functions ------------------

    def check_all(self, fun, triples):
        for (arg1, arg2, expected) in triples:
            self.check(fun, arg1, arg2, expected)
                    
    def check(self, fun, arg1, arg2, expected):
        neg_arg1 = to_negadecimal(arg1)
        neg_arg2 = to_negadecimal(arg2)
        neg_expected = to_negadecimal(expected)
        self.assertEqual(neg_expected, fun(neg_arg1, neg_arg2))
        self.assertEqual(neg_expected, fetch())
        
unittest.main()
