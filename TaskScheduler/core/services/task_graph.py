from collections import defaultdict, deque
from models import Task, Dependency
from task_wrapper import TaskWrapper
import heapq

class TaskGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.indegree = defaultdict(int)
        self.task_map = {}
        
    def load_from_db(self):
        tasks = Task.objects.filter(executed=False)
        dependencies = Dependency.objects.all()
        
        for task in tasks:
            self.task_map[task.name] = TaskWrapper(task)
            self.indegree[task.name] = 0
            
        for dep in dependencies:
            if dep.before.name in self.task_map and dep.after.name in self.task_map:
                self.graph[dep.before.name].append(dep.after.name)
                self.indegree[dep.after.name] += 1
                
    def topological_sort(self):
        queue = deque([name for name in self.task_map if self.indegree[name]==0])
        order = []
        while queue:
            current = queue.popleft()
            order.append(current)
            for neighbor in self.graph[current]:
                self.indegree[neighbor] -= 1
                if self.indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(order) != len(self.task_map):
            raise Exception("Cycle detected in task dependencies")
        
        
def execute_scheduler():
    tg = TaskGraph()
    tg.load_from_db()
    execution_order = tg.topological_sort()
    
    heap = []
    for name in execution_order:
        heapq.heappush(heap, tg.task_map[name])
        
    executed = []
    while heap:
        task_wrapper = heapq.heappop(heap)
        task_wrapper.execute()
        executed.append(task_wrapper.name)
        
    return executed