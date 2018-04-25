def luckysevens(g):
    point={(r,c) for r in len(g) for c in len(g[0])}
    neighbors=lambda r,c: sum(g[rr][cc] for rr,cc in [(r-1,c),(r,c+1),(r,c-1),(r+1,c)] if (rr,cc) in point)
    return sum(1 for (r,c) in point if g[r][c]==7 and isCube(neighbors(r,c)))


def isCube(n):
    return int(round(x ** (1. / 3))) ** 3 == x
