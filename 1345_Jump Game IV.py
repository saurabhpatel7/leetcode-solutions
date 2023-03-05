class Solution:
    def minJumps(self, arr: List[int]) -> int:
        g = defaultdict(list)
        for i,a in enumerate(arr):
            # - key optimization
            # - skip continous value, such as '77...77', only keep first and last 7
            if (i > 0) and (i < len(arr) - 1) and (a == arr[i-1] == arr[i+1]):
                continue

            g[a].append(i)

        seen_set = set([0])
        q = [(0,0)]
        step = 0
        while q:
            p, step = q.pop(0)

            # - check if touch the end
            if p == len(arr) - 1:
                return step
            
            for k in [p-1, p+1] + g[arr[p]]:
                if k in seen_set: continue

                if 0 <= k <= len(arr)-1:
                    seen_set.add(k)
                    q.append((k, step+1))
        
        return 0
