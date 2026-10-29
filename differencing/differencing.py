def differencing(series: list, order: int) -> list:
    """
    Returns the series after the requested differencing order.
    """
    n = len(series)
    for i in range(order):
        dx = [0] * (n - i - 1)
        for j in range(1,n-i):
            dx[j-1] = series[j] - series[j-1]

        series = dx.copy()
    return dx
            