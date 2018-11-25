class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 对小朋友进行排序
        g = sorted(g, reverse=True)
        # 对饼干进行排序
        s = sorted(s, reverse=True)

        g_index = 0
        s_index = 0

        result = 0

        while g_index < len(g) and s_index < len(s):
            if g[g_index] <= s[s_index]:
                g_index += 1
                s_index += 1
                result += 1
                print(g_index,s_index)
            else:
                g_index += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))
