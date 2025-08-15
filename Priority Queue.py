import heapq

class Patient:
    def __init__(self, Name, Surname, idNumber, Priority):
        self.name = Name
        self.surname = Surname
        self.idNumber = idNumber
        self.priority = Priority  
    def print_info(self):
        print(f"Name: {self.name}, Surname: {self.surname}, ID: {self.idNumber}, Priority: {self.priority}")
  
    def __lt__(self, compared):
        return self.priority >compared.priority  


class Scheduler:
    def __init__(self):
        self.patients = []  

    def addPatient(self, patient):
        heapq.heappush(self.patients, patient) 

    def Queue(self):
        if self.patients:
            return heapq.heappop(self.patients)  
        else:
            print("No patients in the queue.")  
            return None  
        
    def viewPatients(self):
        if not self.patients:
            print("No patients waiting in queue.")  
        else:
            self.patients.sort(reverse=True) 
            for patient in self.patients:
                patient.print_info() 

    def saveIntoFile(self, patient):
        
        with open("Project file.txt", "a") as f:  
            f.write(f"{patient.name}, {patient.surname}, {patient.idNumber}\n")  
            
    def readFile(self):
        with open("Project file.txt", "r") as f: 
          print(f.read())  
       
scheduler = Scheduler() 

def mainMenu():
    while True:  
        print("\n1. Add Patient")  
        print("2. Consult Next Patient")
        print("3. View Waiting List")  
        print("4. Read Consultation Log")
        print("5. Exit")  
        choice = input("Choose an option: ") 

        if choice == '1': 
            Name = input("Enter name: ")  
            Surname = input("Enter surname: ")
            idNumber = input("Enter ID number: ")
            priority = int(input("Enter priority (1-5): "))
            patient = Patient(Name, Surname, idNumber, priority) 
            scheduler.addPatient(patient)
        elif choice == '2':  
            patient = scheduler.Queue()
            if patient:  
                patient.print_info() 
                scheduler.saveIntoFile(patient) 
        elif choice == '3':  
            scheduler.viewPatients() 
        elif choice == '4':  
            scheduler.readFile()  
        elif choice == '5':  
            print("Ending program...")
            break 
        else:  
            print("Invalid option .Enter a number between 1 and 5  ")
mainMenu()
