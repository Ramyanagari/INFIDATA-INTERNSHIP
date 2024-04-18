from streamlit_authenticator.utilities.hasher import Hasher
hashed_passwords = Hasher(['prakash']).generate()
print(hashed_passwords)