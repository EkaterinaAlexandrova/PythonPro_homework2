from drunk_polish_calculator import op_plus, op_minus, op_divide, op_multiply, main
from unittest.mock import patch
import pytest

@pytest.mark.parametrize("x,y,expected_result", [(2,3,5), (-1,5,4), (0,0,0)])
def test_op_plus(x:float, y:float, expected_result:float):
    result = op_plus(x, y)
    assert result == expected_result

@pytest.mark.parametrize("x,y,expected_result", [(2,5,3), (10,10,0), (-3,5,8)])
def test_op_minus(x:float, y:float, expected_result:float):
    result = op_minus(x, y)
    assert result == expected_result

@pytest.mark.parametrize("x,y,expected_result", [(2,3,6), (0,10,0), (-4,5,-20)])
def test_op_multiply(x:float, y:float, expected_result:float):
    result = op_multiply(x, y)
    assert result == expected_result

@pytest.mark.parametrize("x,y,expected_result", [(2,10,5), (2,7,3.5), (5,0,0)])
def test_op_divide(x: float, y: float, expected_result: float):
    result = op_divide(x, y)
    assert result == expected_result
    with pytest.raises(ZeroDivisionError):
        op_divide(1, 0)


@pytest.mark.parametrize(
    "expression, expected_result",
    [
        ("1 1 +", "2.0"),
        ("5 2 -", "3.0"),
        ("5 4 *", "20.0"),
        ("8 2 /", "4.0")
    ]
)

def test_main_output(capsys, expression, expected_result):
    with patch("builtins.input", return_value=expression):
        main()
    assert capsys.readouterr().out.rstrip() == expected_result