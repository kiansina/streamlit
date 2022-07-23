import streamlit as st
import pandas as pd
#import psycopg2
#import hidden

#secrets = hidden.secrets()


#conn = psycopg2.connect(host=secrets['host'],
#        port=secrets['port'],
#        database=secrets['database'],
#        user=secrets['user'],
#        password=secrets['pass'],
#        connect_timeout=3)


@st.cache(allow_output_mutation=True)
def get_data():
    return []

user_id = st.text_input("User ID")
Name = st.text_input("What\'s your name?")
foo = st.slider("foo", 0, 100)
bar = st.slider("bar", 0, 100)

if st.button("Submit"):
    get_data().append({"UserID": user_id,"Name":Name, "foo": foo, "bar": bar})

st.write(pd.DataFrame(get_data()))
A=pd.DataFrame(get_data())
A.to_excel('Vic.xlsx')

conn.autocommit = True




sql = """INSERT INTO tst (sas ,name ,foo ,hoo) VALUES ('{}','{}','{}','{}')""".format(A['UserID'].loc[0], A['Name'].loc[0], A['foo'].loc[0], A['bar'].loc[0])


cursor = conn.cursor()
cursor.execute(sql)
