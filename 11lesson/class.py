def changing():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10,20,30]
    dictor = {}
    for i, j in zip(keys, values):
        dictor[i] = j
    print(dictor)
changing()

def merge():
    dict1 = {"Ten": 10, "Twenty": 20, "Thirty": 30}
    dict2= {"Thirty": 30, "Fourty": 40, "Fifty": 50}
    dict1.update(dict2)
    print(dict1)
merge()

def history():
    sampleDict = {"class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}}
    print(sampleDict["class"]["student"]["marks"]["history"])
history()