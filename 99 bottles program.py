for x in range(99,0,-1):
    if x >=1:
        print(x,"bottles of beer on the wall",x,"bottles of beer.")
        print("Take one down and pass it around,")
        print(x-1,"bottles of beer on the wall.")
    elif x==2:
        print(x, "bottles of beer on the wall",x,"bottles of beer.")
        print("Take one down, pass it around,")
        print(x-1,"bottles of beer on the wall.")
    elif x==0:
        print("No more bottles of beer on the wall.")
