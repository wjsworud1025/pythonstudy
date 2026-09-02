#70 if else 구문으로 조건 출력
s=int(input())
if s//3==1:
    print('spring')
else:
    if s//3==2:
        print('summer')
    else:
        if s//3==3:
            print('fall')
        else:
            print('winter')
