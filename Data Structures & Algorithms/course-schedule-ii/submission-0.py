class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        graph = [[] for _ in range(numCourses)]
        ingree = [0] * numCourses
        q = deque()
        for [course, pre] in prerequisites:
            graph[pre].append(course)
            ingree[course] += 1
        for course in range(numCourses):
            if ingree[course] == 0:
                q.append(course)
        while q:
            course = q.popleft()
            order.append(course)
            for next_course in graph[course]:
                ingree[next_course] -= 1
                if ingree[next_course] == 0:
                    q.append(next_course)
        return order if len(order) == numCourses else []        