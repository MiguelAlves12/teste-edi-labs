import csv,json
csv.register_dialect("piper", delimiter="|", quoting=csv.QUOTE_NONE)

pathCSVFile = "./csv/shopping.csv"
pathJsonFile = "./gerados/shopping-convertido.json"

#reading csv and adding data to dictionary
data = {}
obj = {}
order = []
total = 0
with open(pathCSVFile,encoding='utf-8') as csvFile:
    csvReader = csv.DictReader(csvFile,dialect="piper")
    for csvRow in csvReader:
        id = csvRow['ID']
        name = csvRow['Name']
        description = csvRow['Description']
        quantity = csvRow['Quantity']
        value = csvRow['Value']
        obj = {"id":id,"name":name,"description":description,"quantity":quantity,"value":value}
        order.append(obj)
        price = float(value)*float(quantity)
        total = price+total
    data["order"] = order 
    data["total"] = total

#write to json file
with open(pathJsonFile,'w',encoding='utf-8') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4,ensure_ascii=False))


