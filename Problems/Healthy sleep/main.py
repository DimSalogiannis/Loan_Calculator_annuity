A = int(input())
B = int(input())
H = int(input())

if H >= A and H <= B:
    print("Normal")
else:
    if H < A:
        print("Deficiency")
    else:
        print("Excess")