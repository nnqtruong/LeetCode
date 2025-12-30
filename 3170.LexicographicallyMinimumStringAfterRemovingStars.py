class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        removed = [False] * n
        
        # 26 stacks: one stack per character 'a' to 'z'
        pos_stacks = [[] for _ in range(26)]
        
        for i, ch in enumerate(s):
            if ch == '*':
                # Find smallest character that has appeared and not yet removed
                for c in range(26):  # 'a' to 'z'
                    if pos_stacks[c]:
                        idx = pos_stacks[c].pop()  # rightmost occurrence of this char
                        removed[idx] = True        # mark that char as removed
                        break
                removed[i] = True  # mark the star itself as removed
            else:
                # Normal character: push its index onto its stack
                pos_stacks[ord(ch) - ord('a')].append(i)
        
        # Build the final string from characters that are not removed and not '*'
        result = []
        for i, ch in enumerate(s):
            if not removed[i] and ch != '*':
                result.append(ch)
        
        return "".join(result)
