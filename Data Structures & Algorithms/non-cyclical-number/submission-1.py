class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        sum_digits = 0

        while sum_digits != 1:
            sum_digits = 0
            while n > 0:
                digit = n % 10
                sum_digits += digit * digit
                n //= 10 

            if sum_digits in visited:
                return False

            visited.add(sum_digits)

            n = sum_digits

        return True
        