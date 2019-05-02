import os


def creat():
	global panel
	f = open("list_of.txt", 'w')
	panel = {'BMX5': "65.20",
		 	'Skoda': "14.496",
		 	'kodiaq': "85",
		 	'Renault': "45",
		 	'Cherry': "36",
		 	'Mutsubishi': "519"}
	with open ("list_of.txt", 'w') as rob:
		for key,val in panel.items():
			rob.write('{} {}\n'.format(key,val))
			




def tes():
	sea = os.path.exists('./list_of.txt')
	if sea == True:
		print("file is existing")
	elif sea == False:
		creat()
		print ("file is created")

tes()



		 	
nes_lis = {}
with open ('list_of.txt') as checker:
	for line in checker:
		(key, val) = line.split()
		nes_lis[(key)] = val
next_slis = nes_lis




def addcar():
	car_price = float(input("What is car price? "))
	conver_to = input("Conver to EUR or GBP? Type EUR or GBP ")
	if conver_to == "EUR":
			EURO_to_dollar = float(1.11)
			suma = (car_price*EURO_to_dollar)
			print ("In EURO", "%.2f"% suma)
			print (car_name, "in USD", car_price)
			
	elif  conver_to == "GBP":
			Dollar_to_GBP = float(1.23)
			sum1 = (car_price * Dollar_to_GBP)
			print ("In GBP", "%.2f"% sum1)
			print (car_name, "in USD", car_price)
	strin = {}
	strin[car_name]=car_price
	with open('list_of.txt', 'a') as d:
		for key,val in strin.items():
			d.write('{} {}\n'.format(key,val))
		

			
	
with open('list_of.txt') as myfi:
        car_name = (input("Car name "))
        if car_name in myfi.read():
                ab = next_slis.get(car_name)
                print ("It cost USD: ", ab)
        elif car_name not in myfi.read():
                inp = input("Do you wanna continue to add car? Type Yes or No ")
                if inp in ("Yes", "yes", "y", "Y", "YEs", "Ye" ):
                        addcar()
                else:
                        exit()


