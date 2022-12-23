class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        avg = (sum(salary[1:-1]))/len(salary[1:-1])
        return avg
      
 """Best Solution :
      class Solution:
    def average(self, salary: List[int]) -> float:
        max_salary = max(salary)
        min_salary = min(salary)
        salary.remove(max_salary)
        salary.remove(min_salary)
        return mean(salary)
        
   Another:
    class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop()
        salary.pop(0)
        return sum(salary)/len(salary) """
   
