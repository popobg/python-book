#! /usr/bin/env python3

def profit(scient_calcul, graph_calcul):
    return -2 * scient_calcul + 5 * graph_calcul

# range for scient [x0, x1]
# range for graph [y0, y1]
# scient + graph must be >= sum
def search_max(f, x0, y0, x1, y1, sum):
    """search the maximum profit that can be done
    with how many scientific and graphic calculators"""
    pmax = -1 * 10**12
    pscient = -100
    pgraph = -100
    for s in range (x0, x1+1):
        for g in range (y0, y1+1):
            if s + g >= sum:
                p = f(s, g)
                if p >= pmax:
                    pmax = p
                    pscient = s
                    pgraph = g
    return((pscient, pgraph))

# The minimum of scientific calculator to fabric is 100
# its maximum is 200 per day.
# The minimum of graphic calculator to fabric is 80
# its maximum is 170 per day.
# The minimum to ship is 200 (sum to reach or to exceed).
c = search_max(profit, 100, 80, 200, 170, 200)
print(c)