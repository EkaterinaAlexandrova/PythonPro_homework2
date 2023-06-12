from drunk_polish_calculator import op_plus, op_minus, op_divide, op_multiply, main
from io import StringIO
import sys
import pytest

def test_op_plus():
    assert op_plus(2, 3) == 5
    assert op_plus(-1, 5) == 4
    assert op_plus(0, 0) == 0


def test_op_minus():
    assert op_minus(5, 2) == 3
    assert op_minus(10, 10) == 0
    assert op_minus(3, -5) == -2


def test_op_divide():
    assert op_multiply(2, 3) == 6
    assert op_multiply(0, 10) == 0
    assert op_multiply(-4, 5) == -20
    with pytest.raises(ZeroDivisionError):
        op_divide(1, 0)


def test_op_multiplu():
    assert op_divide(10, 2) == 5
    assert op_divide(7, 2) == 3.5
    assert op_divide(0, 5) == 0

def test_main_op_plus():
    sys.stdin = StringIO('8 3 +')
    sys.stdout = result = StringIO()
    main()
    assert result.getvalue().strip() == 'Expression with space delimiter:11.0'

def test_main_op_minus():
    sys.stdin = StringIO('5 2 -')
    sys.stdout = result = StringIO()
    main()
    assert result.getvalue().strip() == 'Expression with space delimiter:3.0'

def test_main_op_multiply():
    sys.stdin = StringIO('2 5 *')
    sys.stdout = result = StringIO()
    main()
    assert result.getvalue().strip() == 'Expression with space delimiter:10.0'

def test_main_op_divide():
    sys.stdin = StringIO('6 2 /')
    sys.stdout = result = StringIO()
    main()
    assert result.getvalue().strip() == 'Expression with space delimiter:3.0'

def test_main_output(capsys):
    input_string = "2 3 + 4 *"
    expected_output = "20.0\n"
    with pytest.raises(StopIteration):
        main(input_string)
        captured = capsys.readouterr()
        assert captured.out == expected_output