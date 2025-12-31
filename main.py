# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
m="false"
k=0
bid={}
k=int(k)
while m=="false":
    s = input("enter name ")
    p = input("enter bid")
    p=int(p)
    bid[s] = p
    t = input("more bidder")
    if t == "yes":
        m="false"
        print("\n"*20)

    else:
        m="true"

a=[]
b=[]
for thing in bid:
    a.append(bid[thing])
    b.append(thing)
    k+=1
r=0
l=0
x=0
s=""
x=int(x)
for t in a:
    r+=1
    if t>x:
        x=t
        l=r

print(b[l-1])
print(x)
