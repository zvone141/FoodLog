from influxdb import InfluxDBClient


def send_data(food_name, calories, proteins, carbs, fats):

    json_body = [
                {
                "measurement": "FoodList",
                    "tags": {
                    "type": food_name
                    },
                    "fields": {
                        "calories": calories,
                        "proteins": proteins,
                        "carbs": carbs,
                        "fats": fats
                    }
                }
            ]

    client.write_points(json_body)

    print "Food added!"
    return 



client = InfluxDBClient('localhost', 8086, 'root', 'root', 'FoodList')
client.create_database('FoodList')


def AddFood():

    food_name = raw_input("Food name to add: ")
    food_amount = float(input("Food amount in grams: "))
    calories = float(raw_input("How much calories: "))
    proteins = float(raw_input("How much proteins: "))
    carbs = float(raw_input("How much carbs: "))
    fats = float(raw_input("How much fats: "))

    calories = calories / food_amount
    proteins = proteins / food_amount
    carbs = carbs / food_amount
    fats = fats / food_amount

    send_data(food_name, calories, proteins, carbs, fats)


