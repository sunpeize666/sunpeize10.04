'''
    작성일 : 2023년 10월 4일
    작성자 : 202195057 손패택
    설명 :  조건에 따라 반복하는 while문
            교재 129 페이지
            
            1~10까지의 합계를 계산하여 출력하기
            시작 값 : 1
            종료 값 : 10
            증가 값 : 1
            for i in range(1, 11) : => while 문으로..
            
            필요한 변수 : num, sum = 0(반드시 초기값 있어야 함.)
'''
num = 1   
sum = 0   

while num <= 10 :    
    sum = sum + num  
    num += 1    
print("합계 : ", sum)