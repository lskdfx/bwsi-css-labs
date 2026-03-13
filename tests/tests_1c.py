import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_original():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
def test_singles():
    assert max_subarray_sum([5]) == 5
    assert max_subarray_sum([-5]) == -5
    assert max_subarray_sum([0]) == 0
def test_all_negative():
    assert max_subarray_sum([-3,-1,-2]) == -1
def test_all_positive():
    assert max_subarray_sum([1,2,3,4,5]) == 15
def test_all_zero():
    assert max_subarray_sum([0,0,0]) == 0
def test_zero_ans():
    assert max_subarray_sum([-3,0,-2]) == 0
def test_best_start():
    assert max_subarray_sum([5,4,-100,1]) == 9
def test_best_end():
    assert max_subarray_sum([1,-100,4,5]) == 9
def test_single_middle():
    assert max_subarray_sum([-10,100,-10]) == 100
def test_alternating():
    assert max_subarray_sum([1,-1,1,-1,1]) == 1
def test_zero_array():
    with pytest.raises(ValueError, match="Array is Empty"):
        max_subarray_sum([])
if __name__ == "__main__":
    pytest.main()
