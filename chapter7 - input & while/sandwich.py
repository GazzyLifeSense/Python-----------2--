sandwich_orders = ['a', 'b', 'pastrami']
finished_sandwiches = []
print("pastrami is out of sale")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    finished = sandwich_orders.pop()
    print(f"{finished} is finished")
    finished_sandwiches.append(finished)