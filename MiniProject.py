details = [
    {
        'name': 'Car',
        'Passenger/Size': 3,
        'Model': 'AC'
    },
    {
        'name': 'Car',
        'Passenger/Size': 4,
        'Model': 'AC'
    },
{
        'name': 'Car',
        'Passenger/Size': 3,
        'Model': 'Non AC'
    },
    {
        'name': 'Car',
        'Passenger/Size': 4,
        'Model': 'Non AC'
    },
    {
        'name': 'Van',
        'Passenger/Size': 6,
        'Model': 'AC'
    },
    {
        'name': 'Van',
        'Passenger/Size': 8,
        'Model': 'AC'
    },
{
        'name': 'Van',
        'Passenger/Size': 6,
        'Model': 'Non AC'
    },
    {
        'name': 'Van',
        'Passenger/Size': 8,
        'Model': 'Non AC'
    },
{
        'name': '3 Wheelers',
        'Passenger/Size' : '3',
        'Model':'Non AC',
    },
{
        'name': 'Trucks',
        'Passenger/Size': '7 ft',
        'Model':'Non AC',
    },
{
        'name': 'Trucks',
        'Passenger/Size': '12 ft',
        'Model':'Non AC',
    },
{
        'name': 'Lorry',
        'Passenger/Size': '2500kg',
        'Model':'Non AC',
    },
{
        'name': 'Lorry',
        'Passenger/Size': '3500kg',
        'Model':'Non AC',
    },

]


temDetails = []
print("Welcome to Cab Service")

while True:
    mainOption = input("1 for Add\n2 for remove\n3 for Assign\n4 for Release\n5 for View\n6 for Exit\n")
    if mainOption == '6':
        break
    elif mainOption == '1':
        name = input("Enter the name: ")
        passe = int(input("Number of the Passenger/Size: "))
        model = input('AC or Non AC: ')

        newDic = {
                'name': name,
                'Passenger/Size': passe,
                'Model': model
            }
        details.append(newDic)
    elif mainOption == '2':
        for detail in details:
            print("ID", details.index(detail), "Name: ", detail['name'], "  Passenger/Size: ", detail['Passenger/Size'])
        remId = int(input("Select the ID: "))
        details.pop(remId)
    elif mainOption == '3':
        for detail in details:
            print("ID", details.index(detail), "Name: ", detail['name'], "  Passenger/Size: ",
                  detail['Passenger/Size'], " Model: ", detail['Model'])
        userSelection = input("Assign 1 for AC\nAssign 2 for Non AC\n")
        if userSelection == '1':
            for detail in details:
                if detail['Model'] == 'AC':
                    dic = detail
                    id = details.index(detail)
                    break
        elif userSelection == '2':
            for detail in details:
                if detail['Model'] == 'Non AC':
                    dic = detail
                    id = details.index(detail)
                    break
        temDetails.append(dic)
        details.pop(id)
    elif mainOption == '4':
        for detail in temDetails:
            print("ID", temDetails.index(detail), "Name: ", detail['name'], "  Passenger/Size: ", detail['Passenger/Size'], " Model: ", detail['Model'])

        userSelection = int(input("Enter the id: "))
        relId = userSelection
        obj = temDetails[relId]
        details.append(obj)
        temDetails.pop(relId)
    elif mainOption == '5':
        print("Available Vehicles")
        for detail in details:
            print("ID", details.index(detail), "Name: ", detail['name'], "  Passenger/Size: ", detail['Passenger/Size'], " Model: ", detail['Model'])
        print("Assigned Vehicles")
        for detail in temDetails:
            print("ID", temDetails.index(detail), "Name: ", detail['name'], "  Passenger/Size: ", detail['Passenger/Size'], " Model: ",
                  detail['Model'])