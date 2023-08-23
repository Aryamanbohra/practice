sale=input("enter thetotal sale in rs.")
sale=int(sale)
if sale >=100000 :
    bs=4000
    hra=20* bs/100
    da =110*bs/100
    cv=500
    incentive=sale*10/100
    bonus=1000
    print("bs",bs)
    print("hra", hra)
    print("da",da)
    print("cv",cv)
    print("incentive",incentive)
    print("bonus",bonus)
else:
    bs=4000
    hra=20* bs/100
    da =110*bs/100
    cv=500
    incentive=sale*4/100
    bonus=500
ts=bs+hra+da+cv+incentive+bonus
print("bs",bs)
print("hra" ,hra)
print("da",da)
print("cv",cv)
print("incentive",incentive)
print("bonus",bonus)