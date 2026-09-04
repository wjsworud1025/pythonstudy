#🖊  매개변수의 기본
#print_n_times("안녕하세요", 5) 형태로 함수를 호출하므로 
#매개변수 value에는 "안녕하세요"가 들어가고, 매개변수 n에는 5가 들어감
def print_n_times(value, n):    
	for i in range(n):        
		print(value)
		
print_n_times("안녕하세요",5)