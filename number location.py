import phonenumbers
from phonenumbers import geocoder
num1 = phonenumbers.parse("+221781094411")
print("\n LOCALISATION DU NUMERO...")
print("\n LE NUMERO SE TROUVE Á ...")
print(geocoder.description_for_number(num1,"fr"))