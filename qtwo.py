def f(A, i, j, penalty, visited, cache) -> int:
    """Returns the minimum penalty to pay to reach top-left => bottom-right."""

    m, n = len(A), len(A[0])
    if (i, j) == (m-1, n-1):
        return penalty

    if (i, j) in cache:
        return cache[(i, j)]

    candidates = []
    if i-1 >= 0 and (i-1, j) not in visited:
        visited.add((i-1, j))
        candidates.append(f(A, i-1, j, penalty+1 if A[i][j] != "UP" else penalty, visited, cache))
    if i+1 < m and (i+1, j) not in visited:
        visited.add((i+1, j))
        candidates.append(f(A, i+1, j, penalty+1 if A[i][j] != "DOWN" else penalty, visited, cache))
    if j-1 >= 0 and (i, j-1) not in visited:
        visited.add((i, j-1))
        candidates.append(f(A, i, j-1, penalty+1 if A[i][j] != "LEFT" else penalty, visited, cache))
    if j+1 < n and (i, j+1) not in visited:
        visited.add((i, j+1))
        candidates.append(f(A, i, j+1, penalty+1 if A[i][j] != "RIGHT" else penalty, visited, cache))

    cache[(i, j)] = min(candidates)
    return cache[(i, j)]

def ff(A) -> int:
    return f(A, 0, 0, 0, {(0, 0)}, dict())

def test_ff():
    A = [
        ["DOWN", "RIGHT", "RIGHT"],
        ["RIGHT", "UP", "DOWN"],
    ]

    assert ff(A) == 1
