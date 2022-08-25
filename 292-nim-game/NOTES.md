The game just comes down to whether n is a multiple of 4 (or mod 3 == 1), if so, I can never win, as 4's only combinations are: 1,2,1 or 1,3 or 2,2 or 3,1
Every multiple of 4 thereafter is just a variation of those 3 combos
Ex: n = 8, combos = (1,1,1,1,1,1,1,1,1), I don't have last say 
                  = (1,3,1,3), variation of (1,3)
                  = (1,3,2,2), variation of (1,3) and (2,2)
                  = (1,3,3,1), variation of (1,3) and (3,1)
                  = (2,2,2,2), variation of (2,2)
                  = ...
                  = (3,1,3,1), variation of (3,1)
                  = ...
                  
No need to write out the other combinations omitted by ... because every pair of moves after the first two is always a variation of 1,3 or 2,2 or 3,1.

Otherwise:
(for n % 3 == 0)
if n = 3, this is trivial.
If n is a multiple of 3 (n >= 6), I can always get last say by forcing a move combination amount that is a multiple of 3 by starting with 2.
           combos = (2,1,3)
                  = (2,2,2)
                  = (2,3,1)
                  ...everything else after is a variation of those 2,1 or 2,2 or 2,3
                  
                  
