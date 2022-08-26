import streamlit as st
import pandas as pd
import psycopg2

from yaml.loader import SafeLoader
import yaml
import streamlit_authenticator as stauth
#from .hasher import Hasher
#from .authenticate import Authenticate
#hashed_passwords = stauth.Hasher(['123', '456']).generate()


# Initialize connection.
# Uses st.experimental_singleton to only run once.
#@st.experimental_singleton
#def init_connection():
    #return psycopg2.connect(**st.secrets["postgres"])

#conn = init_connection()




@st.cache(allow_output_mutation=True)
def get_data():
    return []


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

# Creating a password reset widget
if authentication_status:
    try:
        if authenticator.reset_password(username, 'Reset password'):
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)

# Creating a new user registration widget
try:
    if authenticator.register_user('Register user', preauthorization=False):
        st.success('User registered successfully')
except Exception as e:
    st.error(e)

# Creating a forgot password widget
try:
    username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password('Forgot password')
    if username_forgot_pw:
        st.success('New password sent securely')
        # Random password to be transferred to user securely
    elif username_forgot_pw == False:
        st.error('Username not found')
except Exception as e:
    st.error(e)

if authentication_status:
    user_id = st.text_input("User ID")
    Name = st.text_input("What\'s your name?")
    foo = st.slider("foo", 0, 100)
    bar = st.slider("bar", 0, 100)
    if st.button("Submit"):
        get_data().append({"UserID": user_id,"Name":Name, "foo": foo, "bar": bar})
    #
    st.write(pd.DataFrame(get_data()))
    A=pd.DataFrame(get_data())
