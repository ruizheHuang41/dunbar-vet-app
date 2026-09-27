# Dunbar Vet Clinic Appointment System
class Client:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Pet:
    def __init__(self, pet_name, pet_type, owner):
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.owner = owner

class Appointment:
    def __init__(self, pet, date, time):
        self.pet = pet
        self.date = date
        self.time = time

if __name__ == "__main__":
    client1 = Client("Simone", "0123456789")
    print(f"Created client: {client1.name}")

    pet1 = Pet("Mochi", "Cat", client1)
    print(f"Created pet: {pet1.pet_name}, type: {pet1.pet_type}")

    app1 = Appointment(pet1, "2026-10-01", "14:00")
    print(f"Appointment booked for {pet1.pet_name} on {app1.date} at {app1.time}")
