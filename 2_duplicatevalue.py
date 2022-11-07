# how to find the duplicate value using python.
def find_duplicates(x):
    length=len(x)
    duplicates=[]
    for i in range(length):
        n=i+1
        for a in range(n, length):
            if x[i] == x[a] and x[i] not in duplicates:
                duplicates.append(x[i])
    return duplicates
names = ["sharad", "harsha", "sanjay", "diksha", "sharad", "sanjay", "dhanraj"]
print(find_duplicates(names))