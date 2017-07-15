
INFO= []
with open("data.csv", 'r') as file:
	rew= file.readline().rstrip()
	while(rew):
		INFO.append(rew.split(","))
		rew= file.readline().rstrip()
		

print INFO