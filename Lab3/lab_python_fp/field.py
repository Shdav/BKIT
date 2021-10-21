def field(items, *args):

    assert len(args) > 0
    count=0
    if (len(args) == 1 ):
        for i in items:
            mean = i.get(args[0])
            if( mean != None):
                yield mean
                
    else:
        for i in items:
            ans = {}
            for j in args:
                mean = i.get(j)
                if mean != None:
                    ans[j] = mean
                    count+=1
            if count > 0:
                yield ans
                    
if __name__ == "__main__":
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    ans1 = []
    ans2 = []

    for i in field(goods,"title"):
        ans1.append(i)
    print(ans1)    

    for i in field(goods,"title","price"):
        ans2.append(i)
    print(ans2)