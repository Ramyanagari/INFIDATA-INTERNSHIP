l1=[20, 30, 40, 50]
l2=[10, 20, 30, 40]
sub=list()
for i in range(len(l1)):
    new=l1[i]-l2[i]
    sub.append(new)
print(sub)