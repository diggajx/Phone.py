import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

while True:
    a = input('''press q to quit this code
    Enter Your PhoneNumber with +country_code :''')
    if a=="q":
        print("We SuccessFully Exited this code")
        break

    phone_number = phonenumbers.parse(a)

    print("Origin country is",geocoder.description_for_number(phone_number ,"en"))

    print("Company oF Sim is",carrier.name_for_number(phone_number, "en"))

import os
os.system('pkg install python')
os.system('pip install requests')
os.system ("pip install phonenumbers")
os.system('pip install pyfiglet')
import requests
import phonenumbers
from phonenumbers import carrier,timezone, geocoder
import os
import pyfiglet
os.system('clear')
rs = requests.session()
R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[0;94m"
Y = "\033[1;33m"
nu = 0
n = 0
br = pyfiglet.figlet_format("Diggajx")
print(B+br)
print('''
[Check Phone Number Information]
Coded By : Diggajx
________________________________________
''')

try:
    sign = ('+')
    country_code =(input(R+'Enter Your Country Code  without + :'))
    number = (input(R+'Enter Taregt Number :'))
    a=(sign+country_code+number)
    print(Y+"Your Targeted Number is",a)

    phone_number = phonenumbers.parse(a, "GB")

    print(G+"Valid check: ",phonenumbers.is_valid_number(phone_number))
    print(G+"Company oF Sim is: ",carrier.name_for_number(phone_number, "en"))
    print(G+"Location: ",timezone.time_zones_for_number(phone_number))                                                    print(G+"Origin country is: ",geocoder.description_for_number(phone_number, 'en'))

except:
    print('Something is wrong')
    print('Contact Owner of Script')

    os.system ("xdg-open https:/codeax.herokuapp.com/")
