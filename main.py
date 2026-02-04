
import sys
from src.exception import CustomException


def test_exception():
    try:
        a = 1 / 0
    except Exception as e:
        raise CustomException(e, sys) from e


if __name__ == "__main__":
    test_exception()
