import csv
import datetime

data = 'data.txt'
showrecomms = 'recoms.txt'
fieldnames = ['name', 'time', 'closed_days', 'type', 'special_info']


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def entering():
    restaurant = []
    enter = True
    while enter:
        name = input('Enter restaurant name: ')
        restaurant.append(name)

        dis = input('How long does it take to get the food?')
        if is_int(dis):
            pass
        else:
            print("None")
            dis = None
        restaurant.append(dis)

        closeday = input('What days is it closed? (0 is sunday, separate with commas)')
        restaurant.append(closeday)

        type = input('What type of food is it?')
        restaurant.append(type)

        special_info = input('Anything special?')
        restaurant.append(special_info)

        writing(restaurant)
        enter = False
    else:
        pass


def writing(rlist):
    with open(data, 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        row = {'name': str(rlist[0]), 'time': str(rlist[1]), 'closed_days': str(rlist[2]),
               'type': str(rlist[3]), 'special_info': str(rlist[4])}
        writer.writerow(row)
        print(row)


def finding():
    timesys = datetime.datetime.now()
    dayofweek = str(timesys.strftime('%w'))  # 0 is sunday
    # dayofweek = str(0)
    recomms = []

    max_time = input("Max Wait Time: ")
    print("finding...")

    with open(data, 'r') as f:
        reader = csv.DictReader(f)

        for line in reader:
            closeday = line['closed_days']
            closedaylist = closeday.split(',')
            if dayofweek in closedaylist:
                pass # not open
            else:
                taketime = line['time']
                if int(taketime) <= int(max_time):
                    recomms.append(line)
                else:
                    pass

    with open(showrecomms, 'w') as f:
        fnames = ['name', 'time', 'special_info']
        writer = csv.DictWriter(f, fieldnames=fnames)
        writer.writeheader()
        for rlist in recomms:
            del rlist['type']
            del rlist['closed_days']
            writer.writerow(rlist)


def print_alldata(text):
    with open(text, 'r') as f:
        csv_reader = csv.DictReader(f)

        for line in csv_reader:  # expecting commas
            print(line)


def clear():
    with open(data, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()


def delete():
    resta = input('which restaurant do you want to delete?')

    keeps = []
    with open(data, 'r') as f:
        csv_reader = csv.DictReader(f)
        for line in csv_reader:  # expecting commas
            if resta != line['name']:
                keeps.append(line)
            else:
                print(resta, "deleted")

    with open(data, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for k in keeps:
            writer.writerow(k)

def main():
    run = True

    while run:
        choice = input('Find restaurant or enter one?')
        string = choice.lower()

        if string == "find":
            finding()
            print_alldata(showrecomms)

        elif string == "enter":
            entering()
            print("entered")

        elif string == "clear":
            really = input("Do you really want to clear?")
            if really == "yes":
                clear()
            else:
                pass

        elif string == "read":
            print_alldata(data)

        elif string == "delete":
            delete()

        elif string == "quit":
            run = False

        else:
            print("Invalid request")


main()

