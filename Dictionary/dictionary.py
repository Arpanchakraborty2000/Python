## Dictionary dicclaration ......
add=dict(fast_name ="Arpan",last_naem="chakraborty", age="30",location = "Madhyamgram")
print(add)
print(type(add))
print(add["fast_name"])  ## Index calling .......


## Another type of dictionary declaration  ..........

my_dict={"car1": "TATA", "car2":"nano","car3":"BMW"}
print(my_dict)
print(type(my_dict))
print(my_dict['car1']) ## Index calling .......

for i in my_dict.items():
    print(i)

for i in my_dict:
    print(i)


### value addition ..........

my_dict['car4'] = " Volvo "

print("MY new dict is : ",my_dict)


### Nested Dictionary .........
car1_model={'TATA': 1960}
car2_model={'Hyndai': 1990}
car3_model={'Maruti': 1980}

car_type={'car1':car1_model,'car2':car2_model,'car3':car3_model}

print(car_type)

print(car_type["car1"])

print("Hyndai car year: ",car_type["car2"]['Hyndai'])