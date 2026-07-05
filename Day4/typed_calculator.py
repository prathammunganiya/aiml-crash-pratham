from typing import Optional


def add(a: float, b: float) -> float:
    """Returns addition of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Returns subtraction."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Returns multiplication."""
    return a * b


def divide(a: float, b: float) -> Optional[float]:
    """Returns division result."""
    if b == 0:
        return None
    return a / b


def power(base: float, exp: float) -> float:
    """Returns base raised to exponent."""
    return base ** exp


def modulo(a: int, b: int) -> int:
    """Returns remainder."""
    if b == 0:
        return 0
    return a % b