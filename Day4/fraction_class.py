from math import gcd


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        num = (
            self.numerator * other.denominator +
            other.numerator * self.denominator
        )

        den = self.denominator * other.denominator

        g = gcd(num, den)

        return Fraction(num // g, den // g)

    def __eq__(self, other):
        return (
            self.numerator * other.denominator ==
            other.numerator * self.denominator
        )

    def __lt__(self, other):
        return (
            self.numerator * other.denominator <
            other.numerator * self.denominator
        )


f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print(f1 + f2)
print(f1 == Fraction(2, 4))
print(f1 < Fraction(3, 4))