import numpy as np

'''
numpy에서 배열은 동일한 타입의 값으로 배열 차원을 rank라 함 
튜플 = shape -> 행 2 열 3 rank-2 shape(2,3)
'''

def shapeTest():
    list1 = [1,2,3,4]   #1차원 배열 만들기
    a = np.array(list1) #numpy array 넣기
    print(f'튜플은 = {a.shape}') #sahpe 출력
    print("튜플은 %d" %a.shape)  #

    c = np.array([[1,2,3],[4,5,6]])
    print(c.shape) #shape 출력 2행 3열 rank 2
    print(c)       #모든 array(행열) 출력 [ [1,2,3], [4,5,6]]
    print(c[0,0])  #1행 1열 출력

def funcTest():
    za = np.zeros(2) #zeros는 사용자 지정 배열에 모든 값을 0으로 기입
    print(za)  # 1차원 배열
    zb = np.zeros((2,2))
    print(zb)  # 2차원 배열
    zc = np.zeros((2,2,2))
    print(zc)  # 3차원 배열

    oa = np.ones(2) #ones는 사용자가 지정한 배열에 모든 값을 1로 기입
    print(oa)
    ob = np.ones((2,2))
    print(ob)

    fa = np.full((2,2) , 4) #full은 사용자가 지정한 배열에 모든값을 사용자가 지정한 특정 값으로 넣는다
    print(fa)

    ea = np.eye(3) # eye는 parameter에 넣은 숫자 만큼 parmeter행 parameter열 행열을 만들어 주고 대각선으로 1을 채우고 나머지는 0으로 채워준다
    print(ea)
    eb = np.eye(2)
    print(eb)

    ra = np.array(range(20)) # range는 parameter만큼의 크기의 숫자범위를 만들어주고 이것을 array에 넣으면 그 범위 만큼 숫자를 띈 행열을 만들어 준다
    print(ra)
    list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] #이렇게 만들어 주는것과 똑같은 효과
    rx = np.array(list1)
    print(rx)

    rx = np.array(list1).reshape((4,5)) # reshape은 param 에 넣은 행열로 변환해 준다
    print(rx)

    rb = np.array(range(20)).reshape((4,5))
    print(rb)


def sliceTest():
    list1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    #행열 만들기
    sarr = np.array(list1)
    print(sarr)

    #슬라이싱은 배열[시작행:추출할 행의 수 시작열: 추출할 열의 수] 형태로 배열을 자르는것이 가능하다
    #행열(0,0)을 시작으로 1행과 1열을 추출
    sa = sarr[0:1, 0:1]
    print(sa)
    #행열(0,0)을 시작으로 2행과 2열을 추출
    sa = sarr[0:2, 0:2]
    print(sa)
    #행열(0,0)을 시작으로 3행과 3열을 추출
    sa = sarr[0:3, 0:3]
    print(sa)
    #행열(0,0)을 시작으로 1행과 2열을 추출
    sa = sarr[0:1, 0:2]
    print(sa)
    # 행열(0,0)을 시작으로 2행과 1열을 추출
    sa = sarr[0:2, 0:1]
    print(sa)
    #행열(0,0)을 시작으로 2행과 3열을 추출
    sa = sarr[0:2, 0:3]
    print(sa)


    sarr = np.array(list1)
    print(sarr)
    #행열(0,0)을 시작으로 모든 행열 포함 하여 추출
    sa = sarr[0:, 0:]
    print(sa)
    #행열(1,1)을 시작으로 모든 행열 포함하여 추출
    sa = sarr[1:, 1:]
    print(sa)
    #행열(1,0)을 시작으로 모든 행 및 3열만 추출
    sa = sarr[1:, 0:3]
    print(sa)
    # 행열(1,0)을 시작으로 모든 행 및 1열만 추출
    sa = sarr[1:, 0:1]
    print(sa)
    # 행열(1,1)을 시작으로 모든 행 및 3열만 추출 그 뒤에 행열이 없으면 짤림
    sa = sarr[1:, 1:3]
    print(sa)


def intIndexingTest():
    lst = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    a = np.array(lst)

    # 정수 인덱싱
    s = a[[0, 2], [1, 3]]

    print(s)
    # 출력
    # [2 12]


def boolIndexingTest():
    list1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    a = np.array(list1)

    # 배열 a 에 대해 짝수면 True, 홀수면 False
    bool_indexing = (a % 2 == 0)

    print(bool_indexing)
    # 출력: 부울린 인덱싱 배열
    # [[False  True False]
    #  [ True False  True]
    #  [False  True False]]

    # 부울린 인덱스를 사용하여 True인 요소만 뽑아냄
    print(a[bool_indexing])
    # 부울린 인덱스를 사용하여 False인 요소만 뽑아냄
    print(a[bool_indexing == False])

    # 더 간단한 표현
    n = a[a % 2 == 0]
    print(n)

def calTest():
    a = np.array([1,2,3])
    b = np.array([4,5,6])
    #행열 덧셈
    c = a+b
    print(c)
    c = np.add(a,b)
    print(c)
    #행열 뺄셈
    c = a-b
    print(c)
    c = np.subtract(a,b)
    print(c)
    #행열 곱셈 ver1
    c= a * b
    print(c)
    c = np.multiply(a,b)
    print(c)
    #행열
    c = a / b
    print(c)
    c = np.divide(a,b)
    print(c)