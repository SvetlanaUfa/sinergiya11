import collection
pets = {
    1:{
        "Мухтар":{
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        },
    },
2:{
    "Каа": {
        "Вид питомца": "желторотый питон",
        "Возраст питомца": 14,
        "Имя владельца": "Саша"
    },
},
}
def get_suffix(age):
    if age == 1:
        return "год"
    elif age > 1 and age < 5:
        return "года"
    else:
        return "лет"
def create():
print("### Команда create")
key = Input("Кличка питомца: ")
fields = ["Вид питомца", "Возраст питомца", "Имя владельца"]
temp = {key: dict()}
for field in fields:
    res = input(f"{field}:")
temp[key][field] = int(res) if res.isnumeric() else res
last = collection.deque(pets, maxlen = 1)[0]
pets[last+1] = temp
def read():
    print("### Команда read")
    ID = int(input("Введите ID: "))
    pet = get_pet(ID)
    if not pet:
print(f"Нет питомца с таким ID:{ID}")


    