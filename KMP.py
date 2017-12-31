def makePi(self, pattern):
        """
        pattern[i] = k means when i strings are matched before the point of mismatch, from the k index of pattern should we start the next match.
        """
        pi = [0] * (len(pattern) + 1)
        k = 0
        for i in range(2, len(pattern) + 1):
            while k > 0 and pattern[k] != pattern[i - 1]:
                k = pi[k]
            if pattern[k] == pattern[i - 1]:
                k += 1
            pi[i] = k
        return pi
def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    #corner case
    if needle == "":
        return 0

    pi = self.makePi(needle)
    k = 0
    for i, val in enumerate(haystack):
        while k > 0 and val != needle[k]:
            k = pi[k]
        if val == needle[k]:
            k += 1
        if k == len(needle):
            return i - len(needle) + 1
    return -1
