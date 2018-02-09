from functiontest import makeavg

def test_ints():
    num_list = [1,2,3,4,5]
    obs = makeavg(num_list)
    exp = 3
    assert obs == exp

def test_double():
    num_list = [1,2,3,4]
    obs = makeavg(num_list)
    exp = 2.5
    assert obs == exp

def test_long():
    big = 1000000
    obs = makeavg(range(1,big))
    exp = big/2
    assert obs == exp

def test_complex():
    # testing for complex numbers
    # as arithmatic mean of complecx numbers is meaningless
    num_list = [2+3j,3+4j,-32-2j]
    obs = makeavg(num_list)
    exp = NotImplemented
    assert obs == exp 
if __name__ == "__main__":
    test_ints()
    print('int ok')
    test_double()
    print('double ok')
    test_long()
    print('long ok')
