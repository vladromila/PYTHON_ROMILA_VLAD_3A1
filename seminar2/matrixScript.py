def spiralOrder(m):

    orderArray = []

    while m:
        if m[0]:
            orderArray.extend(m[0])
            m = m[1:]
        if m and m[0]:
            for row in m:
                orderArray.append(row.pop())
        if m:
            orderArray.extend(m.pop()[::-1])
        if m and m[0]:
            for row in m[::-1]:
                orderArray.append(row.pop(0))

    print("".join(orderArray))
