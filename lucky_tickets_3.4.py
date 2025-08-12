total_number_of_lucky_tickets=0
total_number_of_tickets=0
for st in range(0, 10):
    for dt in range(0, 10):
        for t in range(0, 10):
            for s in range(0, 10):
                for d in range(0, 10):
                    for e in range(0, 10):
                        if (st+dt+t)==(s+d+e):
                            total_number_of_lucky_tickets += 1
                        total_number_of_tickets += 1
n=total_number_of_lucky_tickets/total_number_of_tickets*100
print('total number of lucky tickets', total_number_of_lucky_tickets)
print(n,'% of the total number of tickets')