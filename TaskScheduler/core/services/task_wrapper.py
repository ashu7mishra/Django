class TaskWrapper:
    def __init__(self, task):
        self.task = task
        self.name = task.name
        self.priority = task.priority
        
    def execute(self):
        print(f"Executing task: {self.name}")
        self.task.executed = True
        self.task.save()
        
    def __lt__(self, other):
        return self.priority > other.priority
    