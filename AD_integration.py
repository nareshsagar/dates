import bcrypt
import saml
import ldap
from fastapi import Depends, FastAPI, HTTPException, status

app = FastAPI()

def authenticate_user(username: str, password: str):
    # Validate username and password against AD
    ldap_connection = ldap.initialize('ldap://your-ldap-server')
    ldap_connection.simple_bind_s(username, password)

    # Query user's group membership
    user_dn = ldap.search_user_dn(username)
    is_member = ldap.check_group_membership(user_dn, 'AD Group Name')

    if is_member:
        return True
    else:
        return False

def hash_password(password: str):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(password: str, hashed_password: str):
    # Verify if the provided password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def is_group_member(username: str, password: str):
    authenticated = authenticate_user(username, password)
    if authenticated:
        return True
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not authorized')

@app.post('/login')
def login(username: str, password: str):
    is_member = is_group_member(username, password)
    if is_member:
        # Hash the password before storing it
        hashed_password = hash_password(password)
        # Store the username and hashed password in your database or any other storage mechanism
        return {'message': 'Login successful'}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not authorized')









from pyad import *

def get_group_members(group_name):
    pyad.set_defaults(ldap_server="ldap://your_domain_controller")
    
    try:
        group = pyad.adgroup.ADGroup.from_cn(group_name)
        members = group.get_members(recursive=False)
        
        member_list = []
        for member in members:
            member_list.append(member.get_attribute("sAMAccountName"))
            
        return member_list
    
    except pyad.pyadexceptions.ADObjectNotFoundError:
        print("Group not found.")
        return []
    
# Replace "your_domain_controller" with the LDAP server address of your domain controller.
# Make sure to install the required dependencies by running "pip install pyad"

group_name = "Your Group Name"
members = get_group_members(group_name)

print(f"Members of '{group_name}':")
for member in members:
    print(member)

