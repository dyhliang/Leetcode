class BrowserHistory:

    def __init__(self, homepage: str):
        self.visited = [homepage]
        self.forwarded = False
        self.curr = 0

    def visit(self, url: str) -> None:
        prev = self.curr
        
        j = len(self.visited) - 1
        if self.visited and j > self.curr:
            self.visited = self.visited[0:self.curr+1]
        
        self.visited.append(url)
        self.curr = len(self.visited) - 1
        
    def back(self, steps: int) -> str:
        dest = self.curr - steps
        if dest < 0:
            dest = 0
        self.curr = dest
        return self.visited[self.curr]

    def forward(self, steps: int) -> str:
        dest = self.curr + steps
            
        if dest > len(self.visited) - 1:
            dest = len(self.visited) - 1
            
        self.curr = dest
        return self.visited[dest]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)