import pytest
from jar import Jar

# Unit tests for __init__()
def test_init_default_capacity():
    # Test that the default capacity is 12 and the initial size is 0
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_init_specified_capacity():
    # Test that a specified capacity is set correctly and the initial size is 0
    jar = Jar(capacity=10)
    assert jar.capacity == 10
    assert jar.size == 0

def test_init_negative_capacity():
    # Test that a negative capacity raises a ValueError
    with pytest.raises(ValueError) as exc_info:
        Jar(capacity=-5)
    assert str(exc_info.value) == "Capacity must be a non-negative integer."

def test_init_non_integer_capacity():
    # Test that a non-integer capacity raises a ValueError
    with pytest.raises(ValueError) as exc_info:
        Jar(capacity="ten")
    assert str(exc_info.value) == "Capacity must be a non-negative integer."


# Unit Test for __str__()
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


# Unit tests for deposit()
def test_deposit_valid():
    # Test that depositing a valid number of cookies updates the size correctly
    jar = Jar(capacity=10)
    jar.deposit(5)
    assert jar.size == 5

def test_deposit_exceed_capacity():
    # Test that attempting to deposit more cookies than the remaining capacity raises a ValueError
    jar = Jar(capacity=10)
    jar.deposit(8)
    with pytest.raises(ValueError) as exc_info:
        jar.deposit(5)
    assert str(exc_info.value) == "Capacity exceeded."

def test_deposit_negative_value():
    # Test that attempting to deposit a negative number of cookies raises a ValueError
    jar = Jar(capacity=10)
    with pytest.raises(ValueError) as exc_info:
        jar.deposit(-3)
    assert str(exc_info.value) == "Cannot deposit negative cookies."

def test_deposit_zero():
    # Test that depositing zero cookies does not change the size
    jar = Jar(capacity=10)
    jar.deposit(0)
    assert jar.size == 0

def test_deposit_multiple_times():
    # Test that depositing cookies in multiple calls updates the size correctly
    jar = Jar(capacity=10)
    jar.deposit(3)
    jar.deposit(2)
    jar.deposit(4)
    assert jar.size == 9

def test_deposit_at_capacity():
    # Test that attempting to deposit cookies when the jar is already at its capacity limit raises a ValueError
    jar = Jar(capacity=10)
    jar.deposit(10)
    with pytest.raises(ValueError) as exc_info:
        jar.deposit(1)
    assert str(exc_info.value) == "Capacity exceeded."


# Unit tests for withdraw()
def test_withdraw_valid():
    # Test that withdrawing a valid number of cookies updates the size correctly
    jar = Jar(capacity=10)
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5

def test_withdraw_exceed_size():
    # Test that attempting to withdraw more cookies than are currently in the jar raises a ValueError
    jar = Jar(capacity=10)
    jar.deposit(5)
    with pytest.raises(ValueError) as exc_info:
        jar.withdraw(6)
    assert str(exc_info.value) == "Insufficient cookies."

def test_withdraw_negative_value():
    # Test that attempting to withdraw a negative number of cookies raises a ValueError
    jar = Jar(capacity=10)
    jar.deposit(5)
    with pytest.raises(ValueError) as exc_info:
        jar.withdraw(-3)
    assert str(exc_info.value) == "Cannot withdraw negative cookies."

def test_withdraw_zero():
    # Test that withdrawing zero cookies does not change the size
    jar = Jar(capacity=10)
    jar.deposit(5)
    jar.withdraw(0)
    assert jar.size == 5

def test_withdraw_multiple_times():
    # Test that withdrawing cookies in multiple calls updates the size correctly
    jar = Jar(capacity=10)
    jar.deposit(8)
    jar.withdraw(2)
    jar.withdraw(3)
    assert jar.size == 3
