def commonElement(l1,l2):

    common=False
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                common = True
                break
    return common

p=commonElement([1,2,3,4],[0,6,"Jit"])
print(p)
