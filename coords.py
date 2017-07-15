import requests.exceptions as Error
import requests

destination= open("result.csv", 'w')
INFO= []
with open("data.csv", 'r') as file:
	rew= file.readline().rstrip()
	while(rew):
		INFO.append(rew.split(","))
		rew= file.readline().rstrip()

print "read complete"
FINAL= []

def get_location(url, payload):
	reply= ""
	try:
		reply= requests.get(url, params=payload)
	except Error.ConnectionError as e:
		print payload["address"]+"Not found"
	print payload,
	print " complete!"
	return reply

KEY= "AIzaSyBybtSNB8gBPm5QwaE4hF_k0hwBF8uiCbo"
CORE_URL= "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyBybtSNB8gBPm5QwaE4hF_k0hwBF8uiCbo&";

for county in INFO:
	location= {}
	location["address"]= county[0]+", "+county[1]
	try:
		data= get_location(CORE_URL, location).json()["results"][0]["geometry"]["location"]
	except IndexError as e:
		print "One failed"
		continue
	FINAL.append(data)
	destination.write(county[0]+","+county[1]+","+str(data["lat"])+","+str(data["lng"])+"\n")

print "data complete"
		

print "writing complete"