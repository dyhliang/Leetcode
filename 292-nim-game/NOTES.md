This problem is easier to solve by finding an n value where I cannot win at all. 

This happens when n is a multiple of 4 (or mod 3 == 1), if so, I can never win, as 4's only combinations are: 1,2,1 or 1,3 or 2,2 or 3,1


Every multiple of 4 thereafter is just a variation of those 3 combos



Ex: n = 8 

           combos = (1,1,1,1,1,1,1,1,1), I don't have last say 

                  = (1,3,1,3), variation of (1,3)
                  
                  = (1,3,2,2), variation of (1,3) and (2,2)
                  
                  = (1,3,3,1), variation of (1,3) and (3,1)
                  
                  = (2,2,2,2), variation of (2,2)
                  
                  = ...
                  
                  = (3,1,3,1), variation of (3,1)
                  
                  = ...
                  
                  
The other combinations omitted will also have every pair of moves after the first two will be a variation of 1,3 or 2,2 or 3,1.

Otherwise for every number that is not a multiple of 4, there is always an optimal path I can take to guarantee a win.

                  
                  
