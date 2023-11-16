from dataclasses import dataclass

# TASK 1

# @dataclass
# class Car:
#     number: str
#     model: str
#     color: str

#     def go(self):
#         print("GO!")
    
# my_car = Car("b952ad", "Lada", "Black")
# my_car.go()






# TASK 2

# class Book:
#     def __init__(self, title, author, publisherName):
#         self.title = title
#         self.author = author
#         self.publisherName = publisherName

#     def get_title(self):
#         print(self.title)

#     def get_author(self):
#         print(self.author)

#     def get_publisherName(self):
#         print(self.publisherName)

#     def set_title(self, newTitle):
#         self.title = newTitle

#     def set_author(self, newAuthor):
#         self.author = newAuthor

#     def set_publisherName(self, newPublisherName):
#         self.publisherName = newPublisherName

#     def __str__(self):
#         return f'Book: {self.title}, Author: {self.author}, Publisher: {self.publisherName}'
    
# myBook = Book("Rammov's Earth", "Badili Rammov", "MoskauPub")

# myBook.get_title()
# myBook.get_author()
# myBook.get_publisherName()

# myBook.set_title("Meine Liebe")
# myBook.set_author("Caesar Eugler")
# myBook.set_publisherName("BerlinPub")

# print(myBook)







# TASK 3

# @dataclass
# class Pet:
#     _name: str
#     _animal_type: str
#     _age: int
    
#     def set_name(self, newName):
#         self._name = newName
    
#     def set_animal_type(self, newType):
#         self._animal_type = newType
    
#     def set_age(self, newAge):
#         self._age = newAge

#     def get_name(self):
#         print(self._name)

#     def get_animal_type(self):
#         print(self._animal_type)

#     def get_age(self):
#         print(self._age)


# userPetName = str(input("Введите имя вашего питомца: "))
# userPetType = str(input("Введите вид вашего питомца: "))
# userPetAge = int(input("Введите возраст вашего питомца: "))

# userPet = Pet(userPetName, userPetType, userPetAge)

# userPet.get_name()
# userPet.get_animal_type()
# userPet.get_age()








# TASK 4

# class Car:
#     def __init__(self, year_model, rttake):
#         self._year_model = year_model
#         self._rttake = rttake
#         self._speed = 0

#     def accelerate(self):
#         self._speed += 5
    
#     def bre_ak(self):
#         self._speed -= 5

#     def get_speed(self):
#         return(self._speed)
    
# myCar = Car("1991", "Lada")

# for i in range(0, 5):
#     myCar.accelerate()
#     print(myCar.get_speed())

# for i in range(0, 5):
#     myCar.bre_ak()
#     print(myCar.get_speed())




    








# TASK 5

# class Infonnation:
#     def __init__(self, name, adress, age, phoneNumber):
#         self.name = name
#         self.adress = adress
#         self.age = age
#         self.phoneNumber = phoneNumber

#     def get_name(self):
#         print(self.name)
        
#     def get_adress(self):
#         print(self.adress)

#     def get_age(self):
#         print(self.age)

#     def get_phoneNumber(self):
#         print(self.phoneNumber)

#     def set_name(self, newName):
#         self.name = newName
    
#     def set_adress(self, newAdress):
#         self.adress = newAdress
    
#     def set_age(self, newAge):
#         self.age = newAge

#     def set_phoneNumber(self, newNumber):
#         self.phoneNumber = newNumber

# dasIstIch = Infonnation("Yuri", "Elabuga", 18, 89520190024)
# dasIstMeineMutter = Infonnation("Irina", "Tula", 41, 89539630848)
# dasIstMeinVater = Infonnation("Yuri", "Tula", 42, 89807294544)










# TASK 6

# @dataclass
# class Employee:
#     name: str
#     identifyNumber: int
#     departament: str
#     post: str

#     def get_name(self):
#         print(self.name)

#     def get_identifyNumber(self):
#         print(self.identifyNumber)

#     def get_departament(self):
#         print(self.departament)

#     def get_post(self):
#         print(self.post)


# susan = Employee("Сьюзан Мейерс", 47899, "Бухгалтерия", "Вице-президент")
# mark = Employee("Марк Джоунс", 39119, "ИТ", "Программист")
# joy = Employee("Джой Роджерс", 81774, "Производственный", "Инженер")


# susan.get_name()
# susan.get_identifyNumber()
# susan.get_departament()
# susan.get_post()

# print("===========================")

# mark.get_name()
# mark.get_identifyNumber()
# mark.get_departament()
# mark.get_post()

# print("===========================")

# joy.get_name()
# joy.get_identifyNumber()
# joy.get_departament()
# joy.get_post()











# TASK 7

# arrayOfGoodsDesc = ["Пиджак", "Дизайнерские джинсы", "Рубашка"]
# arrayOfQuantity = [12, 40, 20]
# arrayOfPrices = [5995, 3495, 2495]

# @dataclass
# class RetailItem:
#     description: str
#     quantity: int
#     price: int



# def create_goods(objQuan, descArr, quanArr, priceArr):
#     arrayOfGoods = []
#     if objQuan > len(descArr):
#         raise TypeError("ERROR!ERROR!ERROR!")
#     for i in range (0, objQuan):
#         arrayOfGoods.append(RetailItem(descArr[i], quanArr[i], priceArr[i]))
#     return arrayOfGoods

# myGoods = create_goods(3, arrayOfGoodsDesc, arrayOfQuantity, arrayOfPrices)
# print(myGoods)











# TASK 8

# class Patient:
#     def __init__(self, surname, firstname, lastname, adress, city, area, postalCode, phoneNumber, emergencyName, emergencyPhoneNumber):
#         self.surname = surname
#         self.firstname = firstname
#         self.lastname = lastname
#         self.adress = adress
#         self.city = city
#         self.area = area
#         self.postalCode = postalCode
#         self.phoneNumber = phoneNumber
#         self.emergencyName = emergencyName
#         self.emergencyPhoneNumber = emergencyPhoneNumber

#     def get_surname(self):
#         print(self.surname)
#     def set_surname(self, newSurname):
#         self.surname = newSurname

#     def get_firstname(self):
#         print(self.firstname)
#     def set_firstname(self, newFirstName):
#         self.firtsname = newFirstName

#     def get_lastname(self):
#         print(self.lastname)
#     def set_lastname(self, newLastName):
#         self.lastname = newLastName
    
#     def get_adress(self):
#         print(self.adress)
#     def set_adress(self, newAdress):
#         self.adress = newAdress
    
#     def get_city(self):
#         print(self.city)
#     def set_city(self, newCity):
#         self.city = newCity
    
#     def get_area(self):
#         print(self.area)
#     def set_area(self, newArea):
#         self.area = newArea
    
#     def get_postalCode(self):
#         print(self.postalCode)
#     def set_postalCode(self, newPostalCode):
#         self.postalCode = newPostalCode

#     def get_phoneNumber(self):
#         print(self.phoneNumber)
#     def set_phoneNumber(self, newNumber):
#         self.phoneNumber = newNumber
    
#     def get_emergencyName(self):
#         print(self.emergencyName)
#     def set_emergencyName(self, newName):
#         self.emergencyName = newName
    
#     def get_emergencyPhoneNumber(self):
#         print(self.emergencyPhoneNumber)
#     def set_emergencyPhoneNumber(self, newNumber):
#         self.emergencyPhoneNumber = newNumber


# class Procedure:
#     def __init__(self, procedureName, procedureDate, doctorName, price):
#         self.procedureName = procedureName
#         self.procedureDate = procedureDate
#         self.doctorName = doctorName
#         self.price = price

#     def get_procedureName(self):
#         print(self.procedureName)
#     def set_procedureName(self, newName):
#         self.procedureName = newName
    
#     def get_procedureDate(self):
#         print(self.procedureDate)
#     def set_procedureDate(self, newDate):
#         self.procedureDate = newDate
    
#     def get_doctorName(self):
#         print(self.doctorName)
#     def set_doctorName(self, newName):
#         self.doctorName = newName

#     def get_price(self):
#         print(self.price)
#     def set_price(self, newPrice):
#         self.price = newPrice

# myPatient = Patient("Yurin", "Yuri", "Yurievich", "South Park", "Elabuga", "Elabuga", 123, 89520190024, "Irina", 89539630848)

# firstProc = Procedure("Врачебный осмотр", "Сегодня", "Ирвин", 250)
# secondProc = Procedure("Рентгеноскопия", "Сегодня", "Джемисон", 500)
# thirdProc = Procedure("Анализ крови", "Сегодня", "Смит", 200)

# myPatient.get_surname()
# myPatient.get_firstname()
# myPatient.get_lastname()
# myPatient.get_adress()
# myPatient.get_city()
# myPatient.get_area()
# myPatient.get_postalCode()
# myPatient.get_phoneNumber()
# myPatient.get_emergencyName()
# myPatient.get_emergencyPhoneNumber()

# print("==========================")

# firstProc.get_procedureName()
# firstProc.get_procedureDate()
# firstProc.get_doctorName()
# firstProc.get_price()

# print("==========================")

# secondProc.get_procedureName()
# secondProc.get_procedureDate()
# secondProc.get_doctorName()
# secondProc.get_price()

# print("==========================")

# thirdProc.get_procedureName()
# thirdProc.get_procedureDate()
# thirdProc.get_doctorName()
# thirdProc.get_price()