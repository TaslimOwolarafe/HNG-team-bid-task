import csv
import json
import hashlib

def hash(file):
    with open(file,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest()
        print(readable_hash)
        return readable_hash

def writeJson(csvFile):
    data = {}
    with open(csvFile, encoding='utf-8') as csvfile:
        read = csv.DictReader(csvfile)

        filenames = []
        for row in read:
            filenames.append(hash(f"json/{row['Filename']}.json"))
            myData = {'format' : 'CHIP-0007'}
            myData.update(row)
            with open(f"json/{row['Filename']}.json", 'w', encoding='utf-8') as jsonfile:
                 jsonfile.write(json.dumps(myData, indent = 4))

    with open(csvFile, 'r') as file:
        with open('csv/filename.output.csv', 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(file)

            all = []
            rowData = next(reader)
            rowData.append('sha25 of json')
            all.append(rowData)

            for row in reader:
                print(row)
                row.append(hash(f"json/{row[1]}.json"))
                all.append(row)

            writer.writerows(all)


writeJson('NFT Naming - Team Bevel.csv')