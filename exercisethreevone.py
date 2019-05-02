import re

f = open("list_of.txt", 'w')


panel = {"BMX5" : {"costUSD" : "65.02", "costEUR" : "55.66", "costGBP": "48.11"},
	"Skoda": {"costUSD" : "14.496", "costEUR" : "12.91", "costGBP" : "12.91"},
	"kodiaq": {"costUSD" : "85",  "costEUR" : "75.68",  "costGBP" : "73.47"},
	"Renault": {"costUSD" : "45", "costEUR" : "40.03",  "costGBP" : "38.9"},
	"Chery":  {"costUSD" : "36", "costEUR" : "32.02",  "costGBP" : "31.12"},
	"Mutsubishi": {"costUSD" : "519", "costEUR" : "462.08", "costGBP" : "462.08 "}}


with open ("list_of.txt", 'w+') as op:
	op.write(str(panel))



def exer():
	empty_c = {}
	empty_c[car_nam] = ger
	panel.update(empty_c)
	another_string = empty_c
	reg = re.compile('[{}]')
	text = ("It's USD = ")
	print (text,(reg.sub('', str(another_string))))
	with open('list_of.txt', 'a') as last:
		last.write(str(empty_c))


with open ("list_of.txt", 'r+') as oa:
	pane = eval(oa.read())
	car_nam = input("Type car name? ")
	if car_nam in pane:
		cost = ("costUSD")
		ge = panel.get(car_nam)[cost]
		print (car_nam, "cost in USD ", ge)
	else:
		print("Add price to car in ? ")
		ger = float(input())
		print ("What valuta EUR or GBP?")
		val = input("")
		if val == "EUR":
			EURO_to_dollar = float(1.11)
			suma = (ger*EURO_to_dollar)
			print ("In EURO", "%.2f"% suma)
			exer()
		elif val == "GBP":
			Dollar_to_GBP = float(1.23)
			sum1 = (ger * Dollar_to_GBP)
			print ("In GBP", "%.2f"% sum1)
			exer()
		else:
			exer()

f.close()




