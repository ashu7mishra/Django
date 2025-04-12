class TaskCommand:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        
    def execute(self):
        print(f"Executing task {self.name}")
        