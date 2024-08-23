class Solution:
    def fractionAddition(self, expression: str) -> str:
        def parse_fraction(fraction):
            numerator, denominator = map(int, fraction.split('/'))
            return numerator, denominator
        
        # Extract all the fractions, including the signs
        fractions = []
        i = 0
        while i < len(expression):
            # Check if there's a sign (plus or minus)
            if expression[i] in '+-':
                j = i + 1
            else:
                j = i
            while j < len(expression) and expression[j] not in '+-':
                j += 1
            fractions.append(expression[i:j])
            i = j
        
        # Initialize the first fraction as the result
        numerator, denominator = parse_fraction(fractions[0])
        
        for frac in fractions[1:]:
            next_numerator, next_denominator = parse_fraction(frac)
            # Calculate the common denominator
            lcm = denominator * next_denominator // gcd(denominator, next_denominator)
            # Adjust numerators according to the common denominator
            numerator = numerator * (lcm // denominator) + next_numerator * (lcm // next_denominator)
            denominator = lcm
        
        # Simplify the resulting fraction
        common_divisor = gcd(abs(numerator), denominator)
        numerator //= common_divisor
        denominator //= common_divisor
        
        return f"{numerator}/{denominator}"