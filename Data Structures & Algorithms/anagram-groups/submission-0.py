class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = list(map(lambda x : "".join(sorted(x)), strs))
        hash_map = {}
        ans = []
        for index, item in enumerate(sorted_strs):
            if item in hash_map.keys():
                hash_map[item].append(index)
            else:
                hash_map[item] = [index]
        for indexs in hash_map.values():
            anagram = []
            for index in indexs:
                anagram.append(strs[index])
            ans.append(anagram)
        return ans

        
            