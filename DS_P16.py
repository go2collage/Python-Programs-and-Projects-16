# Python Program / Project

def selectionsort(arr, n):
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    print(arr)
    print("Top five scores is: ")
    for i in range(len(arr)-1, 1, -1):
        print(arr[i])


def bubblesort(arr, n):
    i = 0
    for i in range(n-1):
        for j in range(0, n-i-1):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

    print(arr)
    print("Top five scores is: ")
    for i in range(len(arr)-1, 1, -1):
        print(arr[i])


n = int(input("Number of Students in First Year: "))
arr = []

i = 0
for i in range(n):
    item = float(input("Enter percentage marks: "))
    arr.append(item)

print("You have entered percentage of students is: ")
print(arr)

while(True):
    print("********** Menu **********")
    print("1. Selection Sort.")
    print("2. Bubble Sort.")
    print("3. Exit.")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("The sorted list using Selection Sort is: ")
        selectionsort(arr, n)
    
    elif choice == 2:
        print("The sorted list using Bubble Sort is:")
        bubblesort(arr, n)
    
    else:
        print("You have Exit.")
        exit()
