'''
    작성일 : 2023년 10월 4일
    작성자 : 202195057 손패택
    설명 :  조건에 따라 반복하는 while문
            교재 127 페이지
'''


under_construction = True    


while under_construction :
    response = input("공사가 완료 되었습니까?")
    if response == "예" :  
        under_construction = False     
        
print("루프 탈출!!!")