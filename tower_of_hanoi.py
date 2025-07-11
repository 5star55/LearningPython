#Python code to solve the tower of hanoi problem using recursion
def hanoi(disks, source, helper, destination):
    if disks==1:
        print(f"Disk {disks} moved from {source} to {destination}")
        return
    hanoi(disks-1, source, destination, helper)
    print(f"Disk {disks} moved from {source} to {destination}")
    hanoi(disks-1, helper, source, destination)

print(hanoi(10,'A','B','C'))