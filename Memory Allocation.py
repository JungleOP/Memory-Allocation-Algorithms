import sys


def first_fit(holes,m,processes,n):
    allocation = [-1] *n
    # print(allocation)
    for i in range(n):
        for j in range(m):
            if holes[j] >= processes[i]:
                allocation[i] = j
                holes[j] = holes[j] - processes[i]
                break
    print(" Process   Process Size  Hole no.")
    for i in range(n):
        print(" ", "P"+str(i+1), "         ", processes[i],
              "         ", end=" ")
        if allocation[i] != -1:
            print(allocation[i]+1)
        else:
            print("Not Allocated")
    # print(allocation) to know which block it was allocated to



def best_fit(holes,m,processes,n):
    allocation = [-1] * n
    for i in range(n):
        index = -1
        for j in range(m):
            if holes[j] >= processes[i]:
                if index == -1:
                    index = j
                elif holes[index] > holes[j]:
                    index = j
        if index != -1:
            allocation[i] = index
            holes[index] = holes[index] - processes[i]
    print(" Process   Process Size  Hole no.")
    for i in range(n):
        print(" ", "P" + str(i + 1), "         ", processes[i],
              "         ", end=" ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")




def worst_fit(holes,m,processes,n):
    allocation = [0]*n
    for i in range(n):
        index = -1
        for j in range(m):
            if holes[j] >= processes[i]:
                if index == -1:
                    index = j
                elif holes[index] < holes[j]:
                    index = j
        if index != -1:
            allocation[i] = index
            holes[index] = holes[index] - processes[i]
    print(" Process   Process Size  Hole no.")
    for i in range(n):
        print(" ", "P" + str(i + 1), "         ", processes[i],
              "         ", end=" ")
        if allocation[i] != 0:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")












def Option(Alg,holes,m,processes,n):
    print()
    if Alg == 1:
        first_fit(holes,m,processes,n)
    elif Alg == 2:
        best_fit(holes,m,processes,n)
    elif Alg == 3:
        worst_fit(holes, m, processes, n)
    else:
        sys.exit("Invalid algorithm!")






def readInput():
    print("  1:First Fit")
    print("  2:Best Fit")
    print("  3:Worst Fit")
    Alg = int(input("Choose An Algorithm: "))
    print(" ")
    if Alg == 1:
        AlgName = "First Fit"
    elif Alg == 2:
        AlgName = "Best Fit"
    elif Alg == 3:
        AlgName = "Worst Fit"
    else:
        print("Unregnizable  Algorithm")
        sys.exit(0)
    print("Algorithm:", AlgName)
    processes = []
    holes = []
    n = int(input('Enter the no of Process : '))
    for i in range(n):
        # processes.append([])
        # processes[i].append(input('Enter process name : '))
        processes.append(int(input('Enter process size : ')))

    m = int(input('Enter the no of Holes : '))
    for i in range(m):
        # holes.append([])
        # holes[i].append(input('Enter hole name : '))
        holes.append(int(input('Enter hole size : ')))
    # print(processes)
    return Option(Alg,holes,m,processes,n)

if __name__ == '__main__':
    readInput()
