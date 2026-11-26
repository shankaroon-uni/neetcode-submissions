class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visiting = set()
        completed = set()
        ordered = [] # This is the post order traversal of the courses

        courses = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            courses[course].append(prerequisite)
            
        def dfs(course):
            if course in visiting:
                return False
            if course in completed:
                return True
            visiting.add(course)
            for c in courses[course]:
                if not dfs(c):
                    return False
            visiting.remove(course)
            completed.add(course)
            ordered.append(course)
            return True


        for course in courses:
            if not dfs(course):
                return []
        
        return ordered
