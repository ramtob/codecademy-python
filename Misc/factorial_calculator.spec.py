import factorial_calculator as fc

def test_factorial():   
    assert fc.factorial(0) == 1
    assert fc.factorial(1) == 1
    assert fc.factorial(2) == 2
    assert fc.factorial(3) == 6

test_factorial()
print("All tests pass")
# Output: All tests pass