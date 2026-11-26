class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i: [] for i in range(numCourses)}
        visiting = set()
        completed = set()
        
        for course, prerequisite in prerequisites:
            courses[course].append(prerequisite)

        def dfs(course):
            
            if course in completed:
                return True
            if course in visiting:
                return False
                
            visiting.add(course)
            for c in courses[course]:
                if not dfs(c):
                    return False
            visiting.remove(course)
            completed.add(course)

            return True

        for course in courses:
            if not dfs(course):
                return False
        return True