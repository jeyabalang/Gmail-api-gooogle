 
from datetime import datetime
s=input('enter value:')
for i in range(int(s)):
	s=i+1
	print("count"+" "+str(s))
	my_string = str(input('Enter date(yyyy-mm-dd ): '))
	my_date = datetime.strptime(my_string, "%Y-%m-%d")
	my_string = str(input('Enter time(hh:mm): ')) 
	my_date = datetime.strptime(my_string, "%H:%M")
	print(my_date)
