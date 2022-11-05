import csv
import json
import hashlib
import os
import shutil

base_dir = os.path.dirname(os.path.realpath(__file__))

path = os.path.join(base_dir, 'json')
try:
    os.mkdir(path)
except:
    shutil.rmtree(path)
    os.mkdir(path)

def hash(file):
    with open(file,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest()
        return readable_hash

def writeJson(csvFile):
    data = {}
    with open(csvFile, encoding='utf-8') as csvfile:
        read = csv.DictReader(csvfile)

        filenames = []
        for row in read:
            myData = {'format' : 'CHIP-0007'}
            myData.update(row)
            with open(f"json/{row['Filename']}.json", 'w+', encoding='utf-8') as jsonfile:
                 jsonfile.write(json.dumps(myData, indent = 4))
            filenames.append(hash(f"json/{row['Filename']}.json"))

    with open(csvFile, 'r') as file:
        with open('filename.output.csv', 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(file)

            all = []
            rowData = next(reader)
            all.append(rowData)
            all[0].remove('Hash')
            all[0].append('Hash')

            for row in reader:
                row.pop()
                row.append(hash(f"json/{row[1]}.json"))
                all.append(row)

            writer.writerows(all)


writeJson('NFT Naming - Team Bevel.csv')