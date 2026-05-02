#name_dir = []
#info_dir = []
#name = input("wha ur name: ")
#name_dir.append(name)

#age = input("whats ur age: ")
#sex = input("whats ur sex: ")
#location = input("whats ur location: ")
#info_dir.append([age, sex, location])
#nedorobene bo nedal dlhsie cas

people = {
    "John": {"age": 20,
             "gender": "M",
             "location": "KE"
    },
    "Kohut": {"age": 30,
              "gender": "M",
              "location": "BA"
    }
}

#print(f"John je stary {people["John"]["age"]} rokov a po")

for meno, udaje in people.items():
    #print(meno)
    #print(udaje)
    print(f"{meno} pochadza z {udaje["location"]} a ma {udaje["age"]} rokov")

list_listov = [
    [
        [
            ["text"]
        ],[]
    ],
    [

    ]
]
print(list_listov[0][0][0]) # prvy list v hlavnom liste, v tom prvy list a v nom prvy element