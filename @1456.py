class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowels = "aeiou"

        left = 0
        right = k

        # First window
        current_count = 0

        for i in range(k):
            if s[i] in vowels:
                current_count += 1

        max_count = current_count

        # Slide the window
        while right < len(s):

            # Remove left character
            if s[left] in vowels:
                current_count -= 1

            # Add right character
            if s[right] in vowels:
                current_count += 1

            left += 1
            right += 1

            if current_count > max_count:
                max_count = current_count

        return max_count
