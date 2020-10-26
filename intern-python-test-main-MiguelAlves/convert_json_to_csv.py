import csv,json

pathJsonFile = "./json/shopping.json"
pathCSVFile = "./gerados/shopping-convertido.csv"

with open(pathJsonFile,encoding="utf-8") as jsonFile:
    data = json.load(jsonFile)

total=0
with open(pathCSVFile, "w",encoding="utf-8") as csvFile:
    csv_file = csv.writer(csvFile,delimiter="|")
    csv_file.writerow(["ID","Name","Description","Quantity","Value","Total"])
    for item in data["order"]:
        price = (item["quantity"])*float(item["value"])
        total = price + total
        csv_file.writerow([item["id"],item["name"],item["description"],item["quantity"],item["value"],price])
    csv_file.writerow(["Total","","","","",total])