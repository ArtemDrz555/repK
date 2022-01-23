f=open('mat_dv.txt','r')
for i in f:
    l=i.split()

    klass=l[2]
    name=l[1]
    fam=l[0]

    max8=0
    max9=0
    max10=0
    max11=0
    smB=int(l[3])+int(l[4])
    if klass=='8':
        if max8<smB:
            max8==smB
    elif klass=='9':
        if max9<smB:
            max9==smB
    elif klass=='10':
        if max10<smB:
            max10==smB
    elif klass=='11':
        if max11<smB:
            max11==smB


    maxbl=0
    maxbl2=0
    if l[3]>maxbl:
        l[3]==maxbl

    if l[4]>maxbl2:
        l[4]==maxbl2


print('победитель в 8 классов - ',fam, name, klass,max8,'баллов')
print('победитель в 9 классов - ',fam, name, klass,max9,'баллов')
print('победитель в 10 классов - ',fam, name, klass,max10,'баллов')
print('победитель в 11 классов - ',fam, name, klass,max11,'баллов')

print('победитель по алгебре-',fam, name, klass,maxbl,'баллов')
print('победитель по алгебре-',fam, name, klass,maxbl2,'баллов')

f.close()