import firebase_admin
from firebase_admin import credentials, auth

def initialize_firebase_admin():
    # Initialize Firebase Admin with your project's credentials
    cred = credentials.Certificate('path/to/your/firebase-service-account-file.json')
    firebase_admin.initialize_app(cred)

def set_custom_user_claim(uid, role):
    # Set a custom user claim indicating the user's role
    claims = {'role': role}
    auth.set_custom_user_claims(uid, claims)
    print(f"Custom claim set for user {uid}: {claims}")

# Example usage:
# initialize_firebase_admin()
# set_custom_user_claim('some-unique-user-uid', 'doctor')
