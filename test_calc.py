import sys 
import unittest 

from calc import Calculator

NUM_1 = 3.0 
NUM_2 = 2.0 
FAILURE = 'incorrect value'


class CalculatorTest(unittest.TestCase): 
    def setUp(self): 
        self.calc = Calculator() 

    def test_last_answer_init(self): 
        value = self.calc.last_answer
        self.assertEqual(value, 0.0, FAILURE)

    def test_add(self): 
        value = self.calc.add(NUM_1, NUM_2)
        self.assertEqual(value, 5.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)
    
    def test_subtract(self): 
        value = self.calc.subtract(NUM_1, NUM_2)
        self.assertEqual(value, 1.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)
    
    def test_subtract_negative(self): 
        value = self.calc.subtract(NUM_2, NUM_1)
        self.assertEqual(value, -1.0, FAILURE)
        self.assertEqual(value,self.calc.last_answer, FAILURE)
    
    def test_multiply(self): 
        value = self.calc.multiply(NUM_1, NUM_2)
        self.assertEqual(value, 6.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)
    
    def test_divide(self): 
        value = self.calc.divide(NUM_1, NUM_2)
        self.assertEqual(value, 1.5, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_divide_by_zero(self): 
        self.assertRaises(ZeroDivisionError, self.calc.divide, NUM_1, 0)
    
    def test_max_greater(self): 
        value = self.calc.maximum(NUM_1, NUM_2)
        self.assertEqual(value, self.calc.last_answer, FAILURE)
        self.assertEqual(value, NUM_1, FAILURE)
    
    def test_max_lesser(self): 
        value  = self.calc.maximum(NUM_2, NUM_1)
        self.assertEqual(value, NUM_1, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)
    
    def test_min_greater(self): 
        value = self.calc.minimum(NUM_1, NUM_2)
        self.assertEqual(value, NUM_2, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_min_lesser(self):
        value = self.calc.minimum(NUM_2, NUM_1)
        self.assertEqual(value, NUM_2, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)
    
    def test_max_equal(self): 
        value = self.calc.maximum(NUM_1, NUM_1)
        self.assertEqual(value, NUM_1, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_min_equal(self): 
        value = self.calc.minimum(NUM_1, NUM_2)
        self.assertEqual(value, NUM_2, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)
    
    if __name__ == '__main__': 
        unittest.main()
