class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        num = self.numerator * other.denominator + self.denominator * other.numerator
        den = self.denominator * other.denominator
        return f'{num} / {den}'

    def __subrtraction__(self):
        num = self.numerator * other.denominator - self.denominator * other.numerator
        den = self.denominator * other.denominator
        return f'{num} / {den}'