#!/usr/bin/env python3

# ---------- Geometrické pomocné funkce ----------

def on_segment(p, q, r):
    (px, py), (qx, qy), (rx, ry) = p, q, r
    return (min(px, rx) <= qx <= max(px, rx) and
            min(py, ry) <= qy <= max(py, ry))

def orientation(p, q, r):
    (px, py), (qx, qy), (rx, ry) = p, q, r
    val = (qy - py) * (rx - qx) - (qx - px) * (ry - qy)
    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0

def segments_properly_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 * o2 < 0 and o3 * o4 < 0:
        return True

    return False  # doteky a hrany jsou povolené

def point_on_polygon_boundary(pt, poly):
    n = len(poly)
    for i in range(n):
        p1 = poly[i]
        p2 = poly[(i + 1) % n]
        if orientation(p1, p2, pt) == 0 and on_segment(p1, pt, p2):
            return True
    return False

def point_in_polygon(pt, poly):
    # nejdřív boundary check
    if point_on_polygon_boundary(pt, poly):
        return True

    x, y = pt
    inside = False
    n = len(poly)

    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]

        if y1 == y2:
            continue

        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        if y1 <= y < y2:
            xinters = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
            if xinters > x:
                inside = not inside

    return inside


# ---------- Hlavní výpočet ----------

def largest_rectangle_area_with_red_corners(red_tiles):
    poly = red_tiles[:]
    n = len(poly)

    if n < 2:
        return 0

    max_area = 0

    for i in range(n):
        x1, y1 = poly[i]
        for j in range(i + 1, n):
            x2, y2 = poly[j]

            if x1 == x2 or y1 == y2:
                continue

            xmin, xmax = sorted((x1, x2))
            ymin, ymax = sorted((y1, y2))

            c1 = (xmin, ymin)
            c2 = (xmin, ymax)
            c3 = (xmax, ymin)
            c4 = (xmax, ymax)

            corners = [c1, c2, c3, c4]

            # všechny 4 rohy musí být uvnitř nebo na hraně polygonu
            if not all(point_in_polygon(c, poly) for c in corners):
                continue

            # zkontroluj, že žádná hrana obdélníku neprotíná polygon
            rect_edges = [
                (c1, c3),
                (c2, c4),
                (c1, c2),
                (c3, c4),
            ]

            invalid = False
            for e_start, e_end in rect_edges:
                for k in range(n):
                    p1 = poly[k]
                    p2 = poly[(k + 1) % n]
                    if segments_properly_intersect(e_start, e_end, p1, p2):
                        invalid = True
                        break
                if invalid:
                    break

            if invalid:
                continue

            width = xmax - xmin + 1
            height = ymax - ymin + 1
            area = width * height

            if area > max_area:
                max_area = area

    return max_area


# ---------- Načtení vstupu: test.txt ----------

points = []
with open("input.txt") as f:
    for l in f.readlines():
        l = l.strip()
        if not l:
            continue
        a, b = l.split(",")
        points.append((int(a), int(b)))

# Odstraň případné duplikované zakončení polygonu
if len(points) > 1 and points[0] == points[-1]:
    points = points[:-1]

result = largest_rectangle_area_with_red_corners(points)
print(result)