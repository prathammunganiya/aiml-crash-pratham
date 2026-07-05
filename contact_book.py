contacts = [
    {
        "name": "Pratham Munganiya",
        "phone": "8000673052",
        "email": "prathammunganiya9900@gmail.com"
    },
    {
        "name": "Purvam Suthar",
        "phone": "9876501234",
        "email": "purvam@gmail.com"
    },
    {
        "name": "Karan",
        "phone": "9876512340",
        "email": "karan@gmail.com"
    },
    {
        "name": "Nandini Jha",
        "phone": "9876523450",
        "email": "nandini@gmail.com"
    },
    {
        "name": "Rajat",
        "phone": "9876534560",
        "email": "rajat@gmail.com"
    }
]

def find_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact

    return "Contact not found."

search_name = input("Enter contact name: ")

result = find_contact(search_name)

print(result)