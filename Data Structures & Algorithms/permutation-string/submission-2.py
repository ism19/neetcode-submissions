class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1cnt = [0] * 26
        s2cnt = [0] * 26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1cnt[ord(s1[i]) - ord('a')] += 1
            s2cnt[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            matches += (1 if s1cnt[i] == s2cnt[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[r]) - ord('a')
            s2cnt[idx] += 1
            if s1cnt[idx] == s2cnt[idx]:
                matches +=1
            elif s1cnt[idx] + 1 == s2cnt[idx]:
                matches -= 1

            idx = ord(s2[l]) - ord('a')
            s2cnt[idx] -= 1

            if s1cnt[idx] == s2cnt[idx]:
                matches += 1
            elif s1cnt[idx] - 1 == s2cnt[idx]:
                matches -= 1
            l+=1
        return matches == 26