def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
    if sx == fx and sy == fy and t == 1:
        return False
    dist_x = abs(fx-sx)
    dist_y = abs(fy-sy)
    return t >= min(dist_x, dist_y) + abs(dist_x-dist_y)