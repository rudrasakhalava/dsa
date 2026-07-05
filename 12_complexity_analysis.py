# Time complexity O(log n)

def find(listofname, name):
    left = 0
    right = len(listofname)

    while left <= right:
        mid = (left + right) // 2

        if listofname[mid] == name :
            return mid

        elif listofname[mid] > name:
            right = mid - 1

        else :
            left = mid + 1
        
    return -1

listofname = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h"]

name = "f"

result = find(listofname,name)

if result:
    print(f"Founded at index :: {result}")
else:
    print("Name not found!")