from src.main import add
import pytest

# 正常 print(add(1,2))) print(add(100,300)) print(add(-1,-3)) print(add(1.5,3.2)) print(add(0,0))

# 異常 print(add("a","b")) print(add(true,false)) print(add(a,b)) print(add(@,@)) print(add(1/21,1/22))
def test_add():
  assert add(1,2)) == 3
  assert add(100,300) == 400
  # assert add(5, "2", 3) == "error"
  # assert add("2", "8.2") == "error"
  # assert add("8", "1", 3.6) == 84
  # assert add("1", "2") == 12
  # assert add("3", "4", "5") == 39
  # assert add(2.6, "4", None) == "error"
  # assert add(2.5, 3, "5.1") == "error"
  # assert add(5.4, 9.8) == 15
  # assert add("1.4", "2", 3) == "error"
  # assert add(2.5, 3, "x") == "error"
  # assert add(2.1, 9.3, 3.7) == 14
  # assert add(1, 6, 3) == 10
  # assert add(1.6, 2.1) == 3
  # assert add(3.1, 2) == 5
  # assert add(1.9, 4.3, "2.6") == "error"
  # assert add("1", "2", 9) == 21
  # assert add("4", "2.4", 1) == "error"
  # assert add(None, 3, "5.1") == "error"
  # assert add("b", 4, 5) == "error"
