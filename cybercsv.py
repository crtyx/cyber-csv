import json
import csv
import random
import string
from colorama import Fore, Style, init

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
                'name': row['name'],
                'email': row['profile_email'],
                'phone': row['profile_phone'],
                'billingDifferent': row['profile_billingDifferent'] == 'true',
                'card': {
                    'number': row['profile_card_number'],
                    'expMonth': row['profile_card_expMonth'],
                    'expYear': row['profile_card_expYear'],
                    'cvv': row['profile_card_cvv']
                },
                'delivery': {
                    'firstName': row['profile_delivery_firstName'],
                    'lastName': row['profile_delivery_lastName'],
                    'address1': row['profile_delivery_address1'],
                    'address2': row['profile_delivery_address2'],
                    'city': row['profile_delivery_city'],
                    'zip': row['profile_delivery_zip'],
                    'country': row['profile_delivery_country'],
                    'state': row['profile_delivery_state']
                },
                'billing': {
                    'firstName': row['profile_billing_firstName'],
                    'lastName': row['profile_billing_lastName'],
                    'address1': row['profile_billing_address1'],
                    'address2': row['profile_billing_address2'],
                    'city': row['profile_billing_city'],
                    'zip': row['profile_billing_zip'],
                    'country': row['profile_billing_country'],
                    'state': row['profile_billing_state']
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

        header = ['name', 'profile_name', 'profile_email', 'profile_phone', 'profile_billingDifferent',
                  'profile_card_number', 'profile_card_expMonth', 'profile_card_expYear', 'profile_card_cvv',
                  'profile_delivery_firstName', 'profile_delivery_lastName', 'profile_delivery_address1',
                  'profile_delivery_address2', 'profile_delivery_city', 'profile_delivery_zip',
                  'profile_delivery_country', 'profile_delivery_state', 'profile_billing_firstName',
                  'profile_billing_lastName', 'profile_billing_address1', 'profile_billing_address2',
                  'profile_billing_city', 'profile_billing_zip', 'profile_billing_country', 'profile_billing_state']
        csv_writer.writerow(header)

        if isinstance(data, list):
            for profile in data:
                for profile_info in profile.get('profiles', []):
                    row = [
                        profile['name'],
                        profile_info['name'],
                        profile_info['email'],
                        profile_info['phone'],
                        'true' if profile_info['billingDifferent'] else 'false',
                        profile_info['card']['number'],
                        profile_info['card']['expMonth'],
                        profile_info['card']['expYear'],
                        profile_info['card']['cvv'],
                        profile_info['delivery']['firstName'],
                        profile_info['delivery']['lastName'],
                        profile_info['delivery']['address1'],
                        profile_info['delivery']['address2'],
                        profile_info['delivery']['city'],
                        profile_info['delivery']['zip'],
                        profile_info['delivery']['country'],
                        profile_info['delivery']['state'],
                        profile_info['billing']['firstName'],
                        profile_info['billing']['lastName'],
                        profile_info['billing']['address1'],
                        profile_info['billing']['address2'],
                        profile_info['billing']['city'],
                        profile_info['billing']['zip'],
                        profile_info['billing']['country'],
                        profile_info['billing']['state']
                    ]
                    csv_writer.writerow(row)

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
   {Fore.MAGENTA}  CYBERSOLE CSV/JSON CONVERTOR BY CURTY (@crtyx_) {Style.RESET_ALL}
"""

    print(title)
    print("Select conversion type:")
    print("1. CSV to JSON")
    print("2. JSON to CSV")

    choice = input("Enter your choice (1/2): ")

    if choice == "[1]":
        input_csv_file = input("Enter the CSV file name: ")
        output_json_file = input("Enter the JSON file name: ")
        csv_to_json(input_csv_file, output_json_file)
        print("Conversion from CSV to JSON completed.")
    elif choice == "[2]":
        input_json_file = input("Enter the JSON file name: ")
        output_csv_file = input("Enter the CSV file name: ")
        json_to_csv(input_json_file, output_csv_file)
        print("Conversion from JSON to CSV completed.")
    else:
        print("Invalid choice. Please enter '1' or '2'.")

if __name__ == "__main__":
    main()
