from employee import Employee

def test_give_default_raise():
    """Test default raise of 5000."""
    emp = Employee('john', 'doe', 50000)
    emp.give_raise()
    assert emp.salary == 55000


def test_give_custom_raise():
    """Test custom raise amount."""
    emp = Employee('john', 'doe', 50000)
    emp.give_raise(10000)
    assert emp.salary == 60000