
from pytest import raises, fixture
from binsearch import binary_search
import numpy as np

@fixture
def input_data():
    return list(range(10))

def test_binsearch_true(input_data):
    assert binary_search(input_data, 5) == 5

def test_binsearch_false(input_data):
    assert binary_search(input_data, 4.5) == -1

def test_binsearch_outofrange(input_data):
    assert binary_search(input_data, 10) == -1

def test_binsearch_oneelement_true():
    assert binary_search([5],5) == 0

def test_binsearch_oneelement_false():
    assert binary_search([5],4) == -1

def test_binsearch_inf():
    assert binary_search([1,2,np.inf], 2) == 1

def test_binsearch_inf2():
    assert binary_search([1,2,np.inf], np.inf) == 2

def test_binsearch_needlesleft(input_data):
    assert binary_search(input_data, 5, 1, 3) == -1

def test_binsearch_needlecorrect(input_data):
    assert binary_search(input_data, 2, 1, 3) == 2

def test_binsearch_needlebwd(input_data):
    assert binary_search(input_data, 2, 3, 1) == -1

def test_binsearch_needlestacktrue(input_data):
    assert binary_search(input_data, 2, 2, 2) == 2

def test_binsearch_needlestackfalse(input_data):
    assert binary_search(input_data, 5, 2, 2) == -1

def test_binsearch_needlesoutofrange1(input_data):
    assert binary_search(input_data, 5, 2, 12) == -1

def test_binsearch_needlesoutofrange2(input_data):
    assert binary_search(input_data, 5, -1, 5) == -1

def test_binsearch_needlesextreme(input_data):
    assert binary_search(input_data, 5, 0, len(input_data)-1) == 5

def test_binsearch_oneelementneedles(input_data):
    assert binary_search([5], 5, 0, 0) == 0

def test_binsearch_chars():
    assert binary_search(['a','b','c','d'], 'b') == 1

def test_no_value():
    with raises(TypeError):
        binary_search([])

def test_empty_array():
    assert binary_search([],2) == -1

def test_many_vals():
    assert binary_search([1,2,2,2,2,2],2) in [i for i in range(1,6)]

def test_char_():
    with raises(TypeError):
        binary_search(['a', 3], 3)
