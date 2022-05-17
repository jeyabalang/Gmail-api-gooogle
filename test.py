 
from datetime import datetime
s=input('enter value:')
date=[]
for i in range(int(s)):
	s=i+1
	print("count"+" "+str(s))
	my_string = str(input('Enter date(yyyy-mm-dd ): '))
	my_date1 = datetime.strptime(my_string, "%Y-%m-%d")
	my_string = str(input('Enter time(hh:mm): ')) 
	my_date = datetime.strptime(my_string, "%H:%M")
	date.append(my_date)
	date.append(my_date1)
print("Following are the order wise date and time.")
print(date)
