#Script for car prices
#prices of cars are in US dollars
#Mr Koomson car shop
car_prices = {
    'ford': 4500,
    'tesla': 6000,
    'nissan': 25000,
    'jeep': 85400,
    'toyotaAstraMotor': 15000,
    'jaguar': 48000,
    'honda': 105000,
    'BMW': 30500,
    'kia': 100000,
    'audi': 67000,
    'benz': 910000,
    'cadillac': 4300,
    'subaru': 42000,
    'luxus': 12500,
    'hyundai': 67000,
    'volvo': 12000,
    'landRover': 35000,
    'mitsubishi': 70000,
    'buick': 92800,
    'porche': 83500,
    'volkswagen': 13000,
    'chevrolet': 56000,
    'rangeRover': 2000,
    'bugatti': 39000,
    'rollsRoyce': 96000,
    'ferrari': 81000,
    'lamborghini': 99000,
    'pagani': 56000,
    'astonMartin': 33000,
    'mazda': 21700
}

car_brand = input('Enter car brand: ').lower()

if car_brand in car_prices:
    print(f"The price of {car_brand} is ${car_prices[car_brand]:,}")
else:
    print(f"Sorry, {car_brand} is not in our list.")
    
#Github account line= http://github.com/Bdarko100  
 
