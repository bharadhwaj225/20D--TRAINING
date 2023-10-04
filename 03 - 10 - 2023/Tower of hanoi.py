def tower_of_hanoi(n, source, auxiliary, dest):
    if n == 1:
        return 1
    count1 = tower_of_hanoi(n - 1, source, dest, auxiliary)
    count2 = 1
    count3 = tower_of_hanoi(n - 1, auxiliary, source, dest)
    return count1 + count2 + count3


num_disks = int(input())
print(tower_of_hanoi(num_disks, 'A', 'B', 'C'))
#print(f"{total_moves}")