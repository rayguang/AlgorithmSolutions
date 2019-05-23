```
Write a function to compute and return the number of ways  in which to climb a flight of n steps, taking 1, 2 or 3 steps at a time.

https://stackoverflow.com/questions/22562023/n-steps-with-1-2-or-3-steps-taken-how-many-ways-to-get-to-the-top/40920969#40920969
```

# Recursive O(n), memorization
import functools
@functools.lru_cache(maxsize=None)
def recursive(n):
    if n < 4:
        initials = [1,2,4]
        return initials[n-1]
    else:
        return initials(n-1) + initials(n-2) + initials(n-3)
