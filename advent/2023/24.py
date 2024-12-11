from time import time_ns
from scipy.optimize import minimize
import numpy as np

LO, HI = 200000000000000, 400000000000000


def line_coeff(p, v):
    a = v[1] / v[0]
    return a, p[1] - a * p[0]


def add(p0, p1):
    return tuple(x1 + x0 for x1, x0 in zip(p0, p1))


def sub(p0, p1):
    return tuple(x1 - x0 for x1, x0 in zip(p0, p1))


def prod(p0, p1):
    return sum(x0 * x1 for x0, x1 in zip(p0, p1))


def scale(p, k):
    return tuple(map(k.__mul__, p))


def sqr(p):
    return sum(x ** 2 for x in p)


def norm(p):
    return sqr(p) ** .5


def dist(p0, p1):
    return norm(sub(p0, p1))


def inter_time(m, p):
    return (p[0] - m[0][0]) / m[1][0]


def intersect(m0, m1):
    (a0, b0), (a1, b1) = (line_coeff(*pv) for pv in (m0, m1))
    if a1 == a0:
        return None
    else:
        x = (b1 - b0) / (a0 - a1)
        y = a0 * x + b0
        p = x, y
        return p, inter_time(m0, p), inter_time(m1, p)


def motion_dist(m0, m1):
    dp, dv = (sub(*x) for x in zip(m0, m1))
    t = -prod(dp, dv) / sqr(dv)
    return norm(add(dp, scale(dv, t))), t


def get_point(m, t):
    return tuple(px + t * vx for px, vx in zip(*m))


def get_motion(p0, t0, p1, t1):
    v = tuple((px1 - px0) / (t1 - t0) for px0, px1 in zip(p0, p1))
    return tuple(px - vx * t0 for px, vx in zip(p0, v)), v


def solve(data):
    hails = [tuple(tuple(map(int, part.split(','))) for part in line.replace(' ', '').split('@')) for line in data]
    # hails = [(p[:-1], v[:-1]) for p, v in hails]
    res = filter(bool, [intersect(pv0, pv1) for i, pv0 in enumerate(hails[:-1]) for pv1 in hails[i + 1:]])

    m0, m1 = hails[:2]

    # target = hails[2]

    h = 0.001
    alpha = 0.5
    eps = 0.01
    max_loop = 100

    # best_shot = (393358484459946, 319768494435301, 158856878529751), (-242, -49, 209)

    def get_shot_motion(t0, t1):
        p0, p1 = get_point(m0, t0), get_point(m1, t1)
        return get_motion(p0, t0, p1, t1)

    def search():
        best_shot = (0, 0, 0), (1, 1, 1)
        best_target = hails[2]
        best_dist = motion_dist(best_shot, best_target)[0]

        for target in hails[2:]:

            def get_shot_dist(t0, t1):
                return motion_dist(get_shot_motion(t0, t1), target)[0]

            def loop_search():
                i = 0
                d = 2 * eps
                t0, t1 = motion_dist(m0, best_shot)[1], motion_dist(m1, best_shot)[1]
                shot = best_shot
                while d > eps and i < max_loop:
                    i += 1
                    shot = get_shot_motion(t0, t1)
                    d, t = motion_dist(shot, target)
                    d0, d1 = get_shot_dist(t0 + h, t1), get_shot_dist(t0, t1 + h)
                    g0, g1 = (d0 - d) / h, (d1 - d) / h
                    s = alpha * d / ((g0 ** 2 + g1 ** 2) or 1)
                    t0, t1 = max(t0 - s * g0, 0), max(t1 - s * g1, 0)
                    t1 += (t0 == t1) * h
                return d, shot

            d2, s = loop_search()
            if d2 < best_dist:
                best_target, best_dist, best_shot = target, d2, s

                r_shot = tuple(tuple(map(round, x)) for x in best_shot)
                r_dist = motion_dist(r_shot, target)[0]
                print(r_dist)
                if not r_dist:
                    return r_shot

    # shot = get_shot_motion(t0, t1)
    # print(shot)
    # return t0, t1
    # method = 'Nelder-Mead'
    # s = minimize(lambda x: get_shot_dist(*x), np.array(tt), method=method).x
    # s = tuple(tuple(map(round, x)) for x in get_shot_motion(*s))
    #
    # print(motion_dist(best_shot, target)[0])
    return sum(search()[0])


DATA0 = ['19, 13, 30 @ -2,  1, -2',
         '18, 19, 22 @ -1, -1, -2',
         '20, 25, 34 @ -2, -2, -4',
         '12, 31, 28 @ -1, -2, -1',
         '20, 19, 15 @  1, -5, -3']

DATA = open(__file__.removesuffix('.py') + '.txt').readlines()

_t0 = time_ns()
solution = solve(DATA)
calc_time = (time_ns() - _t0) / 1e6

# 871984779123457 too high
# 871983857424998

print(f'Solution ====> {solution:.0f} | Calc time = {calc_time} ms.')
