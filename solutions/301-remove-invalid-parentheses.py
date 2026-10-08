class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(s: str) -> bool:
            balance = 0

            for ch in s:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = [s]
        visited = {s}

        while queue:
            next_level = []
            result = []

            for curr in queue:
                if is_valid(curr):
                    result.append(curr)

            # First level containing valid strings
            # guarantees minimum removals.
            if result:
