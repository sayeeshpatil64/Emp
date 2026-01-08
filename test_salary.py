import pytest
from salary_slip import calculate_salary

def test_hra():
    hra, da, pf, net = calculate_salary(10000)
    assert hra == 2000   # 20%

def test_da():
    hra, da, pf, net = calculate_salary(10000)
    assert da == 5000    # 50%

def test_pf():
    hra, da, pf, net = calculate_salary(10000)
    assert pf == 1100   # 11%

def test_net_salary():
    hra, da, pf, net = calculate_salary(10000)
    expected = (10000 + 2000 + 5000) - 1100
    assert net == expected
