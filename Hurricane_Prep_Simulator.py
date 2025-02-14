#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 23:33:44 2024

@author: anabeatrizgarciac.
"""

# Hurricane Prep Simulation

shelters = [
    {'name': 'Lockhart Magnet Elementary School', 'address': '3719 N 17th St, Tampa, FL 33610', 'pet_friendly': False, 'special_needs': False},
    {'name': 'Middleton High School', 'address': '4801 N 22nd St, Tampa, FL 33610', 'pet_friendly': True, 'special_needs': False},
    {'name': 'Erwin Technical College', 'address': '2010 E Hillsborough Ave, Tampa, FL 33610', 'pet_friendly': True, 'special_needs': False},
    {'name': 'Sheehy Elementary School', 'address': '6402 N 40th St, Tampa, FL 33610', 'pet_friendly': False, 'special_needs': False},
    {'name': 'Seminole Hard Rock Casino', 'address': '5223 Orient Road, Tampa, FL 33610', 'pet_friendly': True, 'special_needs': False},
    {'name': 'Carrollwood Elementary School', 'address': '3516 McFarland Rd, Tampa, FL 33618', 'pet_friendly': False, 'special_needs': False},
    {'name': 'Old Barnes & Noble', 'address': '11802 N Dale Mabry Hwy, Tampa, FL 33618', 'pet_friendly': True, 'special_needs': False},
    {'name': 'Lake Magdalene Elementary School', 'address': '2002 Pine Lake Dr, Tampa, FL 33612', 'pet_friendly': False, 'special_needs': False},
    {'name': 'Pizzo K-8 School', 'address': '11701 USF Bull Run Dr, Tampa, FL 33617', 'pet_friendly': False, 'special_needs': False},
    {'name': 'Bowers-Whitley High School', 'address': '13609 N 22nd Street, Tampa, FL 33613', 'pet_friendly': False, 'special_needs': False},
    {'name': 'Mort Elementary School', 'address': '1806 E Bearss Ave, Tampa, FL 33613', 'pet_friendly': False, 'special_needs': False},
    {'name': 'Burnett Middle School', 'address': '1010 N Kingsway Rd, Seffner, FL 33584', 'pet_friendly': True, 'special_needs': False},
    {'name': 'Jennings Middle School', 'address': '9325 Governors Run Dr, Seffner, FL 33584', 'pet_friendly': False, 'special_needs': False},
    {'name': 'Armwood High School', 'address': '12000 E US Highway 92, Seffner, FL 33584', 'pet_friendly': False, 'special_needs': False},
    {'name': 'Strawberry Crest High School', 'address': '4691 Gallagher Rd, Dover, FL 33527', 'pet_friendly': True, 'special_needs': True},
    {'name': 'Steinbrenner High School', 'address': '5575 W Lutz Lake Fern Rd, Lutz, FL 33558', 'pet_friendly': True, 'special_needs': False},
    {'name': 'Shields Middle School', 'address': '15732 Beth Shields Way, Ruskin, FL 33573', 'pet_friendly': True, 'special_needs': False},
    {'name': 'Durant High School', 'address': '4748 Cougar Path, Plant City, FL 33567', 'pet_friendly': True, 'special_needs': False},
    {'name': 'Turkey Creek Middle School', 'address': '5005 Turkey Creek Rd, Plant City, FL 33567', 'pet_friendly': False, 'special_needs': False},
    {'name': 'Sessums Elementary School', 'address': '11525 Ramble Creek Dr, Riverview, FL 33569', 'pet_friendly': False, 'special_needs': False},
    {'name': 'Collins Elementary School', 'address': '12424 Summerfield Blvd, Riverview, FL 33569', 'pet_friendly': False, 'special_needs': False},
    {'name': 'Boyette Springs Elementary School', 'address': '10141 Sedgebrook Dr, Riverview, FL 33569', 'pet_friendly': False, 'special_needs': False},
    {'name': 'Boyette Springs Elementary School', 'address': '10141 Sedgebrook Dr, Riverview, FL 33569', 'pet_friendly': False, 'special_needs': False},
    {'name': 'Sumner High School', 'address': '10650 County Road 672, Riverview, FL 33579', 'pet_friendly': True, 'special_needs': False},
    {'name': 'Sickles High School', 'address': '7950 W Gunn Hwy, Tampa, FL 33626', 'pet_friendly': True, 'special_needs': False},
    {'name': 'Reddick Elementary School', 'address': '325 West Lake Dr, Wimauma, FL 33598', 'pet_friendly': False, 'special_needs': False},
    {'name': 'City Furniture', 'address': '3205 S. Frontage Road, Plant City, FL 33566', 'pet_friendly': True, 'special_needs': False},
]

def guide_to_evacuation_zone():
    """Guide the user to find their evacuation zone."""
    print("\nTo determine your evacuation zone:")
    print("Use the Hillsborough County Hurricane Evacuation Assessment Tool (HEAT).")
    print("Visit the following link and enter your address:")
    print("https://hillsborough.maps.arcgis.com/apps/webappviewer/index.html?id=960017149a5c40d0a43860aad988d2ec")
    input("\nPress Enter after finding your zone to continue...")

def check_evacuation_zone():
    """Check if the user needs to evacuate based on their zone."""
    print("\nEvacuation Zone Information")
    zone = input("Enter your evacuation zone (A, B, C, D, or E): ").strip().upper()
    if zone in ['A', 'B']:
        print("You are in a high-risk zone. Evacuate immediately if an order is issued.")
    elif zone == 'C':
        print("You are in a moderate-risk zone. Prepare to evacuate if an order is given.")
    elif zone in ['D', 'E']:
        print("You are in a low-risk zone. Monitor alerts and stay prepared.")
    else:
        print("Invalid input. Please check your zone information again.")

def find_shelters_by_zip():
    """Find shelters based on the user's ZIP code and preferences."""
    print("\nShelter Locator")
    zipcode = input("Enter your ZIP code: ").strip()
    pet_friendly = input("Do you need a pet-friendly shelter? (yes/no): ").strip().lower() == 'yes'
    special_needs = input("Do you need a special needs shelter? (yes/no): ").strip().lower() == 'yes'
    
    found_shelters = []
    for shelter in shelters:
        if zipcode in shelter['address']:
            if (not pet_friendly or shelter['pet_friendly']) and (not special_needs or shelter['special_needs']):
                found_shelters.append(shelter)
    
    if found_shelters:
        print("\nShelters in your ZIP code:")
        for shelter in found_shelters:
            print("- Name:", shelter['name'], "Address:", shelter['address'])
            print("  Pet Friendly:", "Yes" if shelter['pet_friendly'] else "No")
            if shelter['special_needs']:
                print("  Special Needs: Yes")
    else:
        print("\nNo shelters found in your ZIP code.")
        print("Here is a list of all available shelters. Please find the one closest to you:")
        for shelter in shelters:
            print("- Name:", shelter['name'], "Address:", shelter['address'])

def supply_checklist():
    """Provide a checklist of necessary hurricane supplies."""
    print("\nHurricane Supply Checklist:")
    supplies = [
        "Non-perishable food (3-day supply)",
        "Water (1 gallon per person per day for 3 days)",
        "Flashlights and extra batteries",
        "Portable phone chargers and power banks",
        "First-aid kit",
        "Medications (7-day supply)",
        "Important documents in a waterproof container",
        "Cash (small bills)",
        "Emergency contacts written down",
        "Pet supplies (food, water, carrier, etc.)",
    ]
    for item in supplies:
        print("- " + item)
        
def check_power_status():
    """Check if the user has power and provide suggestions."""
    power = input("\nDo you currently have power? (yes/no): ").strip().lower()
    if power == "yes":
        print("Great! Charge all devices and backup batteries. Consider freezing water bottles to keep food cold if power is lost.")
    elif power == "no":
        print("Stay calm. Use flashlights, not candles, for safety. Conserve battery power for essential communication.")
    else:
        print("Invalid input. Please answer 'yes' or 'no'.")

def hurricane_simulation():
    """Main hurricane simulation."""
    print("Welcome to the Hurricane Preparedness Simulation!")
    print("This application will help you stay safe during a hurricane.")

    
    check_power_status()

    while True:
        print("\nOptions:")
        print("1. Guide to find your evacuation zone")
        print("2. Check evacuation zone")
        print("3. Find shelters by ZIP code")
        print("4. View hurricane supply checklist")
        print("5. Exit simulation")
        
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            guide_to_evacuation_zone()
        elif choice == "2":
            check_evacuation_zone()
        elif choice == "3":
            find_shelters_by_zip()
        elif choice == "4":
            supply_checklist()
        elif choice == "5":
            print("Stay safe! Thank you for using the Hurricane Preparedness Simulation.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

hurricane_simulation()