import util
import streamlit as st
import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="mysql",
#     database="adult_census"
# )
#mycursor = mydb.cursor()

st.title("Adult Census Income Prediction")

workclass_list = [' Federal-gov', ' Local-gov', ' Private', ' Self-emp-inc', ' Self-emp-not-inc', ' State-gov', ' Without-pay']
education_list = [' 10th', ' 11th', ' 12th', ' 1st-4th', ' 5th-6th', ' 7th-8th', ' 9th', ' Assoc-acdm', ' Assoc-voc', ' Bachelors', ' Doctorate', ' HS-grad', ' Masters', ' Preschool', ' Prof-school', ' Some-college']
gender = [' Female', ' Male']
occupation_list = [' Adm-clerical', ' Armed-Forces', ' Craft-repair', ' Exec-managerial', ' Farming-fishing', ' Handlers-cleaners', ' Machine-op-inspct', ' Other-service', ' Priv-house-serv', ' Prof-specialty', ' Protective-serv', ' Sales', ' Tech-support', ' Transport-moving']
country_list = [' Cambodia', ' Canada', ' China', ' Columbia', ' Cuba', ' Dominican-Republic', ' Ecuador', ' El-Salvador', ' England', ' France', ' Germany', ' Greece', ' Guatemala', ' Haiti', ' Holand-Netherlands', ' Honduras', ' Hong', ' Hungary', ' India', ' Iran', ' Ireland', ' Italy', ' Jamaica', ' Japan', ' Laos', ' Mexico', ' Nicaragua', ' Outlying-US(Guam-USVI-etc)', ' Peru', ' Philippines', ' Poland', ' Portugal', ' Puerto-Rico', ' Scotland', ' South', ' Taiwan', ' Thailand', ' Trinadad&Tobago', ' United-States', ' Vietnam', ' Yugoslavia']
marital_status_list = [' Never-married', ' Married-civ-spouse', ' Divorced', ' Married-spouse-absent', ' Separated', ' Married-AF-spouse', ' Widowed']
relationship_list = [' Not-in-family', ' Husband', ' Wife', ' Own-child', ' Unmarried', ' Other-relative']
race_list = [' White', ' Black', ' Asian-Pac-Islander', ' Amer-Indian-Eskimo', ' Other']

a,b,c = st.columns(3)
age = a.number_input("Enter age:")
fnlwgt = b.number_input("Enter fnlwgt:")
education_number = c.number_input("Enter education number:")

d,e,f = st.columns(3)
c_gain = d.number_input("Enter capital gain:")
c_loss= e.number_input("Enter capital loss:")
hours_per_week = f.number_input("Enter hours-per-week:")

g,h,i = st.columns(3)
workclass = g.selectbox("Workclass",workclass_list)
education = h.selectbox("Education",education_list)
sex = i.selectbox("Gender",gender)

j,k = st.columns(2)
occupation = j.selectbox("Occupation",occupation_list)
country = k.selectbox("Country",country_list)

l,m,n = st.columns(3)
marital_status = l.selectbox("Marital-Status",marital_status_list)
relationship = m.selectbox("Relationship",relationship_list)
race = n.selectbox("Race",race_list)

btn = st.button("Predict Salary")


if btn:
    util.load_saved_artifacts()
    x = util.get_salary(age,hours_per_week,education,occupation,sex)
    if x == '1':
    #     salary = " >50K"
          st.header("Salary is greater than 50K")
    #     mycursor.execute("INSERT INTO inputs VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
    #     age, workclass, fnlwgt, education, education_number, marital_status, occupation, relationship, race, sex,
    #     c_gain, c_loss, hours_per_week, country, salary))
    #     mydb.commit()
    else:
    #     salary = " <=50K"
          st.header("Salary is less than 50K")
    #     mycursor.execute("INSERT INTO inputs VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
    #     age, workclass, fnlwgt, education, education_number, marital_status, occupation, relationship, race, sex,
    #     c_gain, c_loss, hours_per_week, country, salary))
    #     mydb.commit()





