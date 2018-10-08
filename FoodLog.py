from AddFood import AddFood
from influxdb import InfluxDBClient


def send_data(calories, proteins, carbs, fats):
    name_list = ["calories", "proteins", "carbs", "fats"]
    list = [calories, proteins, carbs, fats]

    for info in range(4):

        json_body = [
            {
            "measurement": name_list[info],    #MacroToday, CaloryToday
                "tags": {
                "type": name_list[info]
                },
                "fields": {
                    "value": list[info]
                }
            }
        ]

        client.write_points(json_body)



client = InfluxDBClient('localhost', 8086, 'root', 'root', 'Macros')
client.create_database('Macros')

client1 = InfluxDBClient('localhost', 8086, 'root', 'root', 'FoodList')
client1.create_database('FoodList')

while True:

    search_food = raw_input("Food name: ")
    result = client1.query("SELECT * FROM FoodList where type = '%s'" %search_food)

    try:
        #print result
        data = list(result.get_points())
        data = test[0].values()

        carbs = data[0]
        calories = data[1]
        proteins = data[2]
        fats = data[3]

        food_amount = float(raw_input("How much did you eat?(in grams) "))

        print (proteins * food_amount)

    except:
        print "\nFood not on the list!\n"
	AddFood()



#    calories = raw_input("Amount of calories: ")
#    proteins = raw_input("Amount of proteins: ")
#    carbs = raw_input("Amount of carbs: ")
#    fats = raw_input("Amount of fats: ")

#    send_data(calories, proteins, carbs, fats)
#    print("Well done")
