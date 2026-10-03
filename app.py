# LegalEase - AI-Powered Legal Document Generator

print("===== LEGALEASE =====")
print("AI-Powered Legal Document Generator")

print("\n1. Rental Agreement")
print("2. Leave Letter")
print("3. Legal Notice")

choice = input("\nEnter your choice: ")

name = input("Enter your name: ")
address = input("Enter your address: ")
date = input("Enter date: ")

if choice == "1":
    document = f"""
RENTAL AGREEMENT

Name: {name}
Address: {address}
Date: {date}

This agreement is made between the concerned parties
for the purpose of renting the mentioned property.

Both parties agree to follow the terms and conditions
of the rental agreement.

Signature: ______________
"""

elif choice == "2":
    reason = input("Enter reason: ")

    document = f"""
LEAVE LETTER

From: {name}
Address: {address}
Date: {date}

Subject: Leave Request

I, {name}, request leave due to {reason}.

Kindly consider my request.

Thank you.

Signature: ______________
"""

elif choice == "3":
    issue = input("Enter the legal issue: ")

    document = f"""
LEGAL NOTICE

Name: {name}
Address: {address}
Date: {date}

Subject: Legal Notice

This notice is regarding the following issue:

{issue}

The concerned person is requested to take
appropriate action.

Signature: ______________
"""

else:
    document = "Invalid choice."

print("\n===== GENERATED DOCUMENT =====")
print(document)