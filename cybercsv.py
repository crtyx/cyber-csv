import json
import csv
import random
import string
from colorama import Fore, Style, init
import os
import subprocess

init(autoreset=True)


def generate_random_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))


def csv_to_json(input_csv_file, output_json_file):
    with open(input_csv_file, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = []
        profiles_by_name = {}

        for row in csv_reader:
            profile = {
                'name': row['Group Name'],
                'profile_name': row['Profile Name'],
                'email': row['Email'],
                'phone': row['Phone'],
                'billingDifferent': row['Different Billing'] == 'true',
                'card': {
                    'number': row['Card Number'],
                    'expMonth': row['Card Exp Month'],
                    'expYear': row['Card Exp Year'],
                    'cvv': row['Card CVV']
                },
                'delivery': {
                    'firstName': row['Delivery First Name'],
                    'lastName': row['Delivery Last Name'],
                    'address1': row['Delivery Address 1'],
                    'address2': row['Delivery Address 2'],
                    'city': row['Delivery City'],
                    'zip': row['Delivery ZIP'],
                    'country': row['Delivery Country'],
                    'state': row['Delivery State']
                },
                'billing': {
                    'firstName': row['Billing First Name'],
                    'lastName': row['Billing Last Name'],
                    'address1': row['Billing Address 1'],
                    'address2': row['Billing Address 2'],
                    'city': row['Billing City'],
                    'zip': row['Billing Zip'],
                    'country': row['Billing Country'],
                    'state': row['Billing State']
                }
            }

            if profile['name'] in profiles_by_name:
                profile['id'] = profiles_by_name[profile['name']]['id']
                profiles_by_name[profile['name']]['profiles'].append(profile)
            else:
                profile['id'] = generate_random_id()
                profiles_by_name[profile['name']] = {
                    'id': profile['id'],
                    'name': profile['name'],
                    'profiles': [profile]
                }

        data.extend(profiles_by_name.values())

    with open(output_json_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def json_to_csv(input_json_file, output_csv_file):
    with open(input_json_file, 'r') as json_file:
        data = json.load(json_file)

    with open(output_csv_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        header = ['Group Name', 'Profile Name', 'Email', 'Phone', 'Card Number', 'Card Exp Month', 'Card Exp Year', 'Card CVV', 'Delivery First Name', 'Delivery Last Name', 'Delivery Address 1', 'Delivery Address 2', 'Delivery City', 'Delivery ZIP', 'Delivery Country', 'Delivery State', 'Different Billing', 'Billing First Name', 'Billing Last Name', 'Billing Address 1', 'Billing Address 2', 'Billing City', 'Billing Zip', 'Billing Country', 'Billing State']
        csv_writer.writerow(header)

        if isinstance(data, list):
            for profile in data:
                for profile_info in profile.get('profiles', []):
                    row = [
                        profile['name'],
                        profile_info.get('name', ''), 
                        profile_info.get('email', ''),
                        profile_info.get('phone', ''),
                        profile_info.get('card', {}).get('number', ''), 
                        profile_info.get('card', {}).get('expMonth', ''),  
                        profile_info.get('card', {}).get('expYear', ''),  
                        profile_info.get('card', {}).get('cvv', ''),  
                        profile_info.get('delivery', {}).get('firstName', ''),
                        profile_info.get('delivery', {}).get('lastName', ''),
                        profile_info.get('delivery', {}).get('address1', ''),
                        profile_info.get('delivery', {}).get('address2', ''),
                        profile_info.get('delivery', {}).get('city', ''),
                        profile_info.get('delivery', {}).get('zip', ''),
                        profile_info.get('delivery', {}).get('country', ''),
                        profile_info.get('delivery', {}).get('state', ''),
                        'true' if profile_info.get('billingDifferent') else 'false',
                        profile_info.get('billing', {}).get('firstName', ''),
                        profile_info.get('billing', {}).get('lastName', ''),
                        profile_info.get('billing', {}).get('address1', ''),
                        profile_info.get('billing', {}).get('address2', ''),
                        profile_info.get('billing', {}).get('city', ''),
                        profile_info.get('billing', {}).get('zip', ''),
                        profile_info.get('billing', {}).get('country', ''),
                        profile_info.get('billing', {}).get('state', '')
                    ]
                    csv_writer.writerow(row)



def export_payment_methods(input_csv_file):
    payment_methods = []
    with open(input_csv_file, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            payment_method = {
                'Card Number': row['Card Number'],
                'Card Exp Month': row['Card Exp Month'],
                'Card Exp Year': row['Card Exp Year'],
                'Card CVV': row['Card CVV']
            }
            payment_methods.append(payment_method)

    with open('payment_methods.csv', 'w', newline='') as payment_file:
        payment_writer = csv.DictWriter(payment_file, fieldnames=['Card Number', 'Card Exp Month', 'Card Exp Year', 'Card CVV'])
        payment_writer.writeheader()
        payment_writer.writerows(payment_methods)


def install_requirements():
    subprocess.run(['pip', 'install', 'colorama'])


def main():
    title = f"""
{Fore.GREEN}  ____  _     _ _ _     _            
  /$$$$$$  /$$     /$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$         /$$$$$$   /$$$$$$  /$$    /$$
 /$$__  $$|  $$   /$$/| $$__  $$| $$_____/| $$__  $$       /$$__  $$ /$$__  $$| $$   | $$
| $$  \__/ \  $$ /$$/ | $$  \ $$| $$      | $$  \ $$      | $$  \__/| $$  \__/| $$   | $$
| $$        \  $$$$/  | $$$$$$$ | $$$$$   | $$$$$$$/      | $$      |  $$$$$$ |  $$ / $$/
| $$         \  $$/   | $$__  $$| $$__/   | $$__  $$      | $$       \____  $$ \  $$ $$/ 
| $$    $$    | $$    | $$  \ $$| $$      | $$  \ $$      | $$    $$ /$$  \ $$  \  $$$/  
|  $$$$$$/    | $$    | $$$$$$$/| $$$$$$$$| $$  | $$      |  $$$$$$/|  $$$$$$/   \  $/   
 \______/     |__/    |_______/ |________/|__/  |__/       \______/  \______/     \_/    
                                                                                         
{Style.RESET_ALL}
   {Fore.MAGENTA}  CYBERSOLE CSV/JSON CONVERTOR BY CURTY // @crtyx_ {Style.RESET_ALL}
"""

    while True:
        print(title)
        print("Select conversion type:")
        print("1. CSV to JSON")
        print("2. JSON to CSV")
        print("3. Export payment methods from CSV")
        print("4. Install Requirements")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            input_csv_file = "billing.csv"
            output_json_file = "billing.json"
            csv_to_json(input_csv_file, output_json_file)
            print("Conversion from CSV to JSON completed.")
            input("Press any key to go back.")
        elif choice == "2":
            input_json_file = "billing.json"
            output_csv_file = "billing.csv"
            json_to_csv(input_json_file, output_csv_file)
            print("Conversion from JSON to CSV completed.")
            input("Press any key to go back.")
        elif choice == "3":
            input_csv_file = input("Enter the CSV file name: ")
            export_payment_methods(input_csv_file)
            print("Payment methods exported to 'payment_methods.csv'.")
            input("Press any key to go back.")
        elif choice == "4":
            install_requirements()
            input("Press any key to go back.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter '1', '2', '3', '4', or '5'.")

if __name__ == "__main__":
    main()
