requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies")


requested_topping = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_topping:
	print("adding mushrooms.")
if 'pepperoni' in requested_topping:
	print("adding pepperoni.")
if 'extra cheese' in requested_topping:
	print("adding extra cheese.")

print("\nFinished making your pizza!")


requested_topping = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_topping:
	print(f"adding {requested_topping}.")
print("\nFinished making your pizza")

# Если в пицирии закончиться зеленый перец тогда команда if в цикле for может правильно обработать эту ситуацию:

requested_topping = ['mushrooms', 'Зеленый перец', 'extra cheese']

for requested_topping in requested_topping: # Цикл (для)
	if requested_topping == 'Зеленый перец':
		print("Извините, но к сожалению зеленый перец закончился, приномим Вам свои извинения.")
	else:
		print(f"Adding {requested_topping}.")
print("\nЗакончил готовить пиццу.")


Топинг_для_пицы = ['Зеленый_перец']
if Топинг_для_пицы:
	for Топинг_для_пицы in Топинг_для_пицы:
	    print(f"Добавлен {Топинг_для_пицы}.")
	print("\nВаша пица готова приятного аппетита.")
else:
	print("Извините вы точно хотите купить пиццу без добавления топинга?")


available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'peneapple', 'extra cheese']
requested_topping = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_topping:
	if requested_topping in available_toppings:
		print(f"adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}")

print("\nFinished making your pizza!")