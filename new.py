def solution(X, Y):
    x_sorted = X[:]
    y_sorted = Y[:]
    n = len(x_sorted)
    if len(Y) != n:
        return -1 
    sorted_indices = sorted(range(len(X)), key=lambda i: X[i])
    x_sorted = [X[i] for i in sorted_indices]
    y_sorted = [Y[i] for i in sorted_indices]

    area = 0
    for i in range(1, len(x_sorted)):
        width = x_sorted[i] - x_sorted[i - 1]
        height = (y_sorted[i] + y_sorted[i - 1]) / 2
        area += width * height

    return area


print(solution([0.00,0.2,0.33,0.43,0.63,0.66,1.00],[0.00,0.25,0.25,0.50,0.50,1.00,1.00]))