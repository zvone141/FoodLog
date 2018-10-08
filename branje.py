from influxdb import InfluxDBClient

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'FoodList')
client.create_database('FoodList')


while True:

    search_food = raw_input("Food name: ")

    result = client.query("SELECT * FROM FoodList where type = '%s'" %search_food)

    try:
        #print result
        test = list(result.get_points())
        test = test[0].values()

        carbs = test[0]
        calories = test[1]
        proteins = test[2]
        fats = test[3]

        #print proteins

        food_amount = float(raw_input("How much did you eat?(in grams) "))

        print (proteins * food_amount)

    except:
        print "Food not on the list!"

    
