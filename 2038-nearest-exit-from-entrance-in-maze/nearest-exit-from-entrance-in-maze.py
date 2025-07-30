from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        l=len(maze)
        n=len(maze[0])
        q=deque()
        q.append((entrance[0],entrance[1],0))
        visit=set()
        visit.add((entrance[0],entrance[1]))

        dir=[(-1,0),(0,1),(0,-1),(1,0)]

        while(q):
            x,y,steps=q.popleft()
            for dx,dy in dir:
                nx =x+dx 
                ny =y+dy

                if 0<=nx<l and 0<=ny<n and maze[nx][ny]=='.' and (nx,ny) not in visit:
                    if nx==0 or nx==(l-1) or ny==0 or ny==(n-1):
                        return steps+1
                    q.append((nx,ny,steps+1))
                    visit.add((nx,ny))
        return  -1
