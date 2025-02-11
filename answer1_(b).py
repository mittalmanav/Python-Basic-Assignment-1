# Validate a given email address to check if it’s a valid Gmail address, considering:
# It should contain "@gmail.com".
# The username before "@gmail.com" should contain only lowercase letters , numbers and permitted symbols.
# Provide informative error messages for invalid IP or email.
email = input("enter email")
if email.endswith("@gmail.com"):
    if email[:email.index("@")].islower():
        print("valid email")
   
else:
    print("invalid email")