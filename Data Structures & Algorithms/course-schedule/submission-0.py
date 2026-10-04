class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        ingree = [0] * numCourses
        q = collections.deque()
        completed = 0
        for [course, pre] in prerequisites:
            graph[pre].append(course)
            ingree[course] += 1
        for course in range(numCourses):
            if ingree[course] == 0:
                q.append(course)
        while q:
            course = q.popleft()
            completed += 1
            for next_course in graph[course]:
                ingree[next_course] -= 1
                if ingree[next_course] == 0:
                    q.append(next_course)
        return completed == numCourses