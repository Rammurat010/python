
# for nat_nub in range(1,20):
#     if nat_nub%2==0:
#         print(nat_nub)

# for i in range(1,5):
#     if i==0 or i==1 or i==n:
#       print("*")
#     else:
#       print(" ")



pappu="RAM"
out=' '
for i in pappu:
    if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        out=out+i
    else:
        q=ord(i)+32
        out=out+chr(q)
print(out)

