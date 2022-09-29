# City Cab Service Application

class Cabservice:
    selectedoption = ""
    userinput = ""
    systemoption = ""
    vehicleoption = 0
    VehicleList = [
        #CARS
        {"Vehicle": "Car", "Vehicle No": "ABC5812", "Passengers": 3, "AC Type": "AC"},
        {"Vehicle": "Car", "Vehicle No": "ABC5452", "Passengers": 3, "AC Type": "AC"},
        {"Vehicle": "Car", "Vehicle No": "ABC4812", "Passengers": 3, "AC Type": "NonAC"},
        {"Vehicle": "Car", "Vehicle No": "ABC4512", "Passengers": 4, "AC Type": "AC"},
        {"Vehicle": "Car", "Vehicle No": "ABC7852", "Passengers": 4, "AC Type": "AC"},
        {"Vehicle": "Car", "Vehicle No": "ABC9852", "Passengers": 4, "AC Type": "NonAC"},
        {"Vehicle": "Car", "Vehicle No": "ABC7422", "Passengers": 4, "AC Type": "NonAC"},

        #VANS
        {"Vehicle": "Van", "Vehicle No": "DEF5812", "Passengers": 6, "AC Type": "AC"},
        {"Vehicle": "Van", "Vehicle No": "DEF4562", "Passengers": 6, "AC Type": "AC"},
        {"Vehicle": "Van", "Vehicle No": "DEF7582", "Passengers": 6, "AC Type": "NonAC"},
        {"Vehicle": "Van", "Vehicle No": "DEF5512", "Passengers": 8, "AC Type": "AC"},
        {"Vehicle": "Van", "Vehicle No": "DEF5852", "Passengers": 8, "AC Type": "NonAC"},
        {"Vehicle": "Van", "Vehicle No": "DEF5752", "Passengers": 8, "AC Type": "NonAC"},

        #THREE WHEELERRS`   2
        {"Vehicle": "Three Wheel", "Vehicle No": "BQE5812", "Passengers": 3, "AC Type": "-"},

        #TRUCKS
        {"Vehicle": "Truck", "Vehicle No": "CVB5782", "Size(ft)": 7, "AC Type": "-"},
        {"Vehicle": "Truck", "Vehicle No": "CVB4412", "Size(ft)": 8, "AC Type": "-"},

        #LORRIES
        {"Vehicle": "Lorry", "Vehicle No": "WER5812", "Max Load(kg)": 2500, "AC Type": "-"},
        {"Vehicle": "Truck", "Vehicle No": "CVB5452", "Max Load(kg)": 3500, "AC Type": "-"}
    ]

    availablevehiclelist = VehicleList
    job = []

    #Customer Function
    @staticmethod
    def customer():
        print("\n************* Welcome Customer *************")
        while True:
            run.SelectVehicle()
            run.userinput = int(input("Enter Vehicle : "))
            if run.userinput == 1:
                run.chooseoption(1)
                run.vehicleoption = int(input("Enter Vehicle Type : "))
                run.availablequeue(run.vehicleoption,"Car")
            run.main()
            if run.userinput == 2:
                run.chooseoption(2)
                run.vehicleoption = int(input("Enter Vehicle Type : "))
                run.availablequeue(run.vehicleoption,"Van")
            run.main()
            if run.userinput == 3:
                run.chooseoption(3)
                run.vehicleoption = int(input("Enter Vehicle Type : "))
                run.availablequeue(run.vehicleoption,"Three Wheel")
            run.main()
            if run.userinput == 4:
                run.chooseoption(4)
                run.vehicleoption = int(input("Enter Vehicle Type : "))
                run.availablequeue(run.vehicleoption,"Truck")
            run.main()
            if run.userinput == 5:
                run.chooseoption(5)
                run.vehicleoption = int(input("Enter Vehicle Type : "))
                run.availablequeue(run.vehicleoption,"Lorry")
            run.main()
            if run.userinput == 99:
                print('''\n************* Thank you for joining with us. *************''')
                run.main()

    #Admin Function
    @staticmethod
    def admin():
        print("\n************* Welcome Admin *************")
        while True:
            print('''
                (1) Add a new vehicle to the system
                (2) Remove a vehicle from the system
                (3) Assign a job
                (4) Release form assigned job
                (5) See available vehicles in each category
                (99) Exit\n''')
            run.systemoption = int(input("Enter the Task : \n"))
            if run.systemoption == 1:
                run.addvehicle()
                run.admin()
            elif run.systemoption == 2:
                no = input("Enter Vehicle No")
                for i in run.VehicleList:
                    if no in i.values():
                        run.VehicleList.remove(i)
                print(*run.VehicleList, sep="\n")
                run.admin()
            elif run.systemoption == 3:
                run.jobQueue()
                print("Contact Drivers")
                run.admin()
            elif run.systemoption == 4:
                run.availablevehiclelist.clear()
                print("\nVehicle Released Successfuly")
                print(run.VehicleList)
                run.admin()
            elif run.systemoption == 5:
                print(*run.availablevehiclelist, sep= "\n")
                run.admin()
            elif run.systemoption == 99:
                print('''\n************* Thank you for joining with us. *************''')
                run.main()
            else:
                print("Invalid Entry")
                run.admin()

    @staticmethod
    def addvehicle():
        print('''
            (1) Add Car
            (2) Add Van
            (3) Add Three Wheel
            (4) Add Truck
            (5) Add Lorry
            ''')
        inputvehicle = int(input("Enter Your Choice"))
        if inputvehicle == 1:
            type = input("Enter Vehicle Type\n")
            vehicleno = input("Enter Vehicle No\n")
            maxx = input("Enter Passengers/Load?Size")
            ac_type = input("Enter AC Type")
            vehicle = {"Vehicle": type, "Vehicle No": vehicleno, "Passengers/Load?Size": maxx, "AC Type": ac_type}
            run.VehicleList.append(vehicle)
            print("Vehicle Added Succesfuly")
        elif inputvehicle == 2:
            type = input("Enter Vehicle Type\n")
            vehicleno = input("Enter Vehicle No\n")
            maxx = input("Enter Passengers/Load?Size")
            ac_type = input("Enter AC Type")
            vehicle = {"Vehicle": type, "Vehicle No": vehicleno, "Passengers/Load?Size": maxx, "AC Type": ac_type}
            run.VehicleList.append(vehicle)
            print("Vehicle Added Succesfuly")
        elif inputvehicle == 3:
            type = input("Enter Vehicle Type\n")
            vehicleno = input("Enter Vehicle No\n")
            maxx = input("Enter Passengers/Load?Size")
            ac_type = input("Enter AC Type")
            vehicle = {"Vehicle": type, "Vehicle No": vehicleno, "Passengers/Load?Size": maxx, "AC Type": ac_type}
            run.VehicleList.append(vehicle)
            print("Vehicle Added Succesfuly")
        elif inputvehicle == 4:
            type = input("Enter Vehicle Type\n")
            vehicleno = input("Enter Vehicle No\n")
            maxx = input("Enter Passengers/Load?Size")
            ac_type = input("Enter AC Type")
            vehicle = {"Vehicle": type, "Vehicle No": vehicleno, "Passengers/Load?Size": maxx, "AC Type": ac_type}
            run.VehicleList.append(vehicle)
            print("Vehicle Added Succesfuly")
        elif inputvehicle == 5:
            type = input("Enter Vehicle Type\n")
            vehicleno = input("Enter Vehicle No\n")
            maxx = input("Enter Passengers/Load?Size")
            ac_type = input("Enter AC Type")
            vehicle = {"Vehicle": type, "Vehicle No": vehicleno, "Passengers/Load?Size": maxx, "AC Type": ac_type}
            run.VehicleList.append(vehicle)
            print("Vehicle Added Succesfuly")

    @staticmethod
    def availablequeue(vehicleop, vehicle):
        if vehicle == "Car" and vehicleop == 1:
            run.checkavailability(3,"AC")
        elif vehicle == "Car" and vehicleop == 2:
            run.checkavailability(3,"NonAC")
        elif vehicle == "Car" and vehicleop == 3:
            run.checkavailability(4,"AC")
        elif vehicle == "Car" and vehicleop == 4:
            run.checkavailability(4,"NonAC")
        elif vehicle == "Van" and vehicleop == 1:
            run.checkavailability(6,"AC")
        elif vehicle == "Van" and vehicleop == 2:
            run.checkavailability(6,"NonAC")
        elif vehicle == "Van" and vehicleop == 3:
            run.checkavailability(8,"AC")
        elif vehicle == "Van" and vehicleop == 4:
            run.checkavailability(8,"-")
        elif vehicle == "Three Wheeler" and vehicleop == 0:
            run.checkavailability(8,"NonAC")
        elif vehicle == "Truck" and vehicleop == 1:
            run.checkavailability(7,"-")
        elif vehicle == "Truck" and vehicleop == 2:
            run.checkavailability(12,"-")
        elif vehicle == "Lorry" and vehicleop == 1:
            run.checkavailability(2500,"-")
        elif vehicle == "Lorry" and vehicleop == 1:
            run.checkavailability(3500,"-")

    @staticmethod
    def checkavailability(maximum, ac_type):
        print("Available Vehicles")
        j = 1
        for i in run.availablevehiclelist:
            if maximum in i.values() and ac_type in i.values():
                print("(", j, ")", i)
                j+=1
        run.selectFromQueue(maximum,ac_type)

    @staticmethod
    def selectFromQueue(maximum,ac_type):
        run.selectedoption = int(input("\nEnter your vehicle : "))
        s = 1
        for i in run.availablevehiclelist:
            if maximum in i.values() and ac_type in i.values():
                if run.selectedoption == s:
                    print("You selected option", s)
                    run.jobQueue(i)
                    print("************* Booking Successfully.... !!! *************")
                    for j in run.job:
                        print(j)
                        s += 1

    @staticmethod
    def jobQueue(i):
        run.job.append(i)

    @staticmethod
    def chooseoption(option):
        while True:
            if option == 1:
                print('''Select Wehicle
                        (1) Car - 3 Passengers - AC Vehicle
                        (2) Car - 3 Passengers - NonAC  Vehicle
                        (2) Car - 4 Passengers - AC Vehicle
                        (2) Car - 4 Passengers - NonAC Vehicle\n''')
            elif option == 2:
                print('''Select Wehicle
                        (1) Van - 6 Passengers - AC Vehicle
                        (2) Van - 6 Passengers - NonAC Vehicle
                        (2) Van - 8 Passengers - AC Vehicle
                        (2) Van - 8 Passengers - NonAC Vehicle\n''')
            elif option == 3:
                print('''Maximum Number of Passengers - 3\n''')
            elif option == 4:
                print('''Select Wehicle
                        (1) Truck - 7ft
                        (2) Truck - 12ft\n''')
            elif option == 5:
                print('''Select Wehicle
                        (1) Lorry - 2500kg
                        (2) Lorry - 3500kg\n''')
            else:
                print("Invalid Choice")
            break

    @staticmethod
    def SelectVehicle():
        print('''
                (1) Car
                (2) Van
                (3) Three Wheel
                (4) Truck
                (5) Lorry
                (99) Exit\n''')
    
    @staticmethod 
    def main():
        # Select Whether Customer or Admin
        print('''************* Welcome to the City Cab Service *************
            Select User
            (1) Customer
            (2) Admin
            (99) Exit
            \n''')

        run.userinput = int(input("Enter: "))
        if run.userinput == 1:
            run.customer()
        elif run.userinput == 2:
            run.admin()
        elif run.userinput == 99:
            exit()
        else:
            print("Invalid Choice")
            run.main()

run = Cabservice()
run.main()
    
