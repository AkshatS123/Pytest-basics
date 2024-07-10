import pytest 

from calc_class import Calculator

#defining some constants for testing 

NUM_1 = 3.0 
NUM_2 = 2.0



#creating a fixture which is fixed set of data that tests can use. 
#fixture is a function names Calculator here that we deifined, when called it will instantiate a new calc objct from calc_class 


#Each test that requires a Calculator instance will call this fixture, and a fresh instance of the Calculator will be created and passed to the test function.
@pytest.fixture
def calculator(): 
    return Calculator()

#helper functions 

def check_answer(expected, answer, last_answer): 
    assert expected == answer
    assert expected == last_answer


#test cases here: 
def test_last_answer_init(calculator): 
    assert calculator.last_answer == 0.0

def test_add(calculator): 
    answer = calculator.add(NUM_1, NUM_2)
    check_answer(5.0, answer, calculator.last_answer)

def test_subtract(calculator): 
    answer = calculator.subtract(NUM_1, NUM_2)
    check_answer(1.0, answer, calculator.last_answer)

def test_subtract_negative(calculator): 
    answer = calculator.subtract(NUM_2, NUM_1)
    check_answer(-1.0, answer, calculator.last_answer)

def test_multiply(calculator): 
    answer = calculator.multiply(NUM_1, NUM_2)
    check_answer(6.0, answer, calculator.last_answer)

def test_divide(calculator): 
    answer = calculator.divide(NUM_1, NUM_2)
    check_answer(1.5, answer, calculator.last_answer)


#test to catch divide by 0 exception
def test_divide_zero(calculator):
    with pytest.raises(ZeroDivisionError) as e:  
        answer = calculator.divide(NUM_1, 0)
    assert "division by zero" in str(e.value)

#test for maximum and min use parameters, for using fixture we use it as the first function argument 
#mark.parametrzie allows us to test multiple diffren't inputs here test_max function is going to check for all of the tuple inputs below, a,b,expected is specifiying how 
@pytest.mark.parametrize("a,b,expected",[
    (NUM_1, NUM_2, NUM_1),
    (NUM_2, NUM_1, NUM_1),
    (NUM_1, NUM_1, NUM_1),
])


def test_max(calculator, a, b, expected): 
    answer = calculator.maximum(a,b)
    check_answer(expected, answer, calculator.last_answer)


@pytest.mark.parametrize("a,b,expected",[
    (NUM_1, NUM_2, NUM_2),
    (NUM_2, NUM_1, NUM_2),
    (NUM_2, NUM_2, NUM_2),
])

def test_minimum(calculator, a,b, expected): 
    answer = calculator.minimum(a,b)
    check_answer(expected, answer, calculator.last_answer)



