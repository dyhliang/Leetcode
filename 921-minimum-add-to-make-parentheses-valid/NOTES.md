**Solution:**

Very similar to the generate parentheses problem, here we don't need a dictionary as there are only two possible values, "(" and ")".

We start off by initializing a stack along with a counter that keeps track of the amount of ")".

Use a for loop to iterate through the string passed in the argument:

-Check if the current char is a "(", if so, append onto the stack

-Otherwise, it's a ")", so there's two things to check for:

  1) Is the stack nonempty (to prevent the index error thereafter)? And is the top of the stack a "("?
     If so, pop the stack since we've found a pairing.
  2) Increment the counter for ")" by 1 as we'll need an add to eventually pair away this.
  3) Once we iterate through, we add up the length of the stack, which should now hold any "(" that were 
     not paired away, along with the number of extra ")".
