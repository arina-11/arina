for ticket in range(100000, 100101):
    e = ticket % 10
    d = (ticket // 10) % 10
    s = (ticket // 100) % 10
    t = (ticket // 1000) % 10
    dt = (ticket // 10000) % 10
    st = (ticket // 100000) % 10
    if (st + dt + t) == (s + d + e):
        print(ticket)