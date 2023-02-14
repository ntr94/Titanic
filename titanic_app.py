# ---------------------------------LiBRARIES--------------------------------------
import streamlit as st
import matplotlib as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px




# ---------------------------------PAGE SETUP--------------------------------------


st.set_page_config(page_title='TITANIC APP', layout='wide',page_icon='🚢')


# ---------------------------------TITANIC DATA--------------------------------------
titanic = pd.read_csv('data/titanic_clean.csv')

#----------------------SIDEBAR------------------------------------

st.set_option('deprecation.showPyplotGlobalUse', False)
st.sidebar.image('imagen/image (2).png', width=300)
st.sidebar.write('---')
st.sidebar.title('Column Index')
index= st.sidebar.selectbox(
            'Choose the column you want to analyze',
            ('Main Page','Survived','Pclass', 'Name', 'Sex', 'Age','SibSp', 'Parch','Ticket', 'Fare', 'Embarked'))
st.sidebar.write('---')

# Choose de column

if index == 'Main Page':
    # Column Main Page
    
    st.image('imagen/descarga.png', width=700)

    st.title("Titanic analysis")

    col1, col2 = st.columns(2)

    col2.subheader("A Streamlit web app by Ignacio Torralba Ruiz")

    # Little introduction
    st.markdown(
        "RMS Titanic was a British passenger liner, operated by the White Star Line, which sank in the North Atlantic Ocean on 15 April 1912 after striking an iceberg during her maiden voyage from Southampton, England, to New York City, United States. Of the estimated 2,224 passengers and crew aboard, more than 1,500 died, making it the deadliest sinking of a single ship up to that time. It remains the deadliest peacetime sinking of a superliner or cruise ship. The disaster drew public attention, provided foundational material for the disaster film genre, and has inspired many artistic works."
    )

    st.markdown(
        'RMS Titanic was the largest ship afloat at the time she entered service and the second of three Olympic-class ocean liners operated by the White Star Line. She was built by the Harland and Wolff shipyard in Belfast. Thomas Andrews, the chief naval architect of the shipyard, died in the disaster. Titanic was under the command of Captain Edward Smith, who went down with the ship. The ocean liner carried some of the wealthiest people in the world, as well as hundreds of emigrants from Great Britain and Ireland, Scandinavia, and elsewhere throughout Europe, who were seeking a new life in the United States and Canada.'
    )

    # More information option
    more_info = st.expander("More information? 👉")
    with more_info:
        st.markdown(
            "If you want more information abaut Titanic, press [Titanic](https://en.wikipedia.org/wiki/Titanic).")
    
    if st.button('You can click here to see the dataframe'):
        st.dataframe(titanic)


elif index == 'Survived':
#SURVIVED COLUMN 
    
    st.title(
        "Survived")

    #Control space and rows (format)
    row1_1, row1_2 = st.columns(
        (1,1))
    
    #First row
    with row1_1:
        
        st.subheader(
            "Count Pclass")

        st.image('imagen/Survived_count.png', width=600)
        
        st.markdown(
        "549 people died and 342 managed to survive.")
    
    with row1_2:
        
        st.subheader(
            "% Survived")
        
        st.image('imagen/Survived_%.png', width=450)
        
        st.markdown(
        "61.62% of people died and 38.38% managed to survive")

#Second row
    with row1_1:
        
        st.subheader(
            "Survived - Sex")

        st.image('imagen/Survived_sex.png', width=600)
        
        st.markdown(
        "Observing the graph it can be seen that most of the people who lost their lives are male and those who survived were female.")
    
    with row1_2:
        
        st.subheader(
            "Survived % - Sex %")
        
        st.image('imagen/Survived_sex%.png', width=520)
        
        st.markdown(
        "Relationship between number of survived and sex in percentage")

#Third row
    with row1_1:
        
        st.subheader(
            "Survived - Pclass")

        st.image('imagen/Survived_class.png', width=600)
        
        st.markdown(
        "Observing the graph it can be seen that most of the people who lost their lives belonged to third class.")
    
    with row1_2:
        
        st.subheader(
            "Survived - Embarked")
        
        st.image('imagen/Suivived_embarked.png', width=600)
        
        st.markdown(
        "Most of the fatalities embarked on Southamton")

#Fourth row
    with row1_1:
        
        st.subheader(
            "Survived - Age - Fare")

        st.image('imagen/Survived_age_fare.png', width=700)
        
        st.markdown(
        "It can be seen in the graph that the possibility of survival is related to the price of the fare. The better class you have and the more expensive the fare, the more chances of surviving.")


elif index == 'Pclass':
#PCLASS COLUMN 
    
    st.title(
        "Pclass")

    #Control space and rows (format)
    row2_1, row2_2 = st.columns(
        (1,1))
    
    #First row
    with row2_1:
        
        st.subheader(
            "Count Pclass")

        st.image('imagen/Pclass_count.png', width=600)
        
        st.markdown(
        "The graph shows that most of the passengers belong to the third class. Where 491 are Third class, 184 Second class and 216 First class.")
    
    with row2_2:
        
        st.subheader(
            "% Pclass")
        
        st.image('imagen/Pclass_%.png', width=500)
        
        st.markdown(
        "Most of the passengers are third class.")

    #Second row
    with row2_1:
        
        st.subheader(
            "Pclass - Sex")

        st.image('imagen/Pclass_sex.png', width=550)
        
        st.markdown(
        "In all classes men outnumber women. But in third class the number of men doubles that of women.")
    
    with row2_2:
        
        st.subheader(
            "Pclass - Age")
        
        st.image('imagen/Pclass_age.png', width=550)
        
        st.markdown(
        "In the third class, there is a large amount of data on the working ages of many people who immigrated to America. In first class this reasoning is not fulfilled since rich people travel in this class, causing the ages to be concentrated above 30 years.")

    #Third row
    with row2_1:
        
        st.subheader(
            "Pclass - Embarked")

        st.image('imagen/Pclass_embarked.png', width=550)
        
        st.markdown(
        "The graph indicates that the vast majority of passengers who boarded in Southampton regardless of class.")
    
    with row2_2:
        
        st.subheader(
            "Pclass - Embarked - Fare")
        
        st.image('imagen/Pclass_fareembarked.png', width=620)
        
        st.markdown(
        "At first glance it can be seen that the first class is where these rich people are and the third class is poor people. The most expensive fares in each class come from Cherbourg and Southampton. Queenstown has the cheapest fares.")





elif index == 'Name':
#NAME COLUMN 
    
    st.title(
        "Name")
    st.subheader(
            "% Top 10 Names")
    st.image('imagen/Name.png', width=600)
        
    st.markdown(
        "We can see the most popular passenger names and the percentage they represent.")


elif index == 'Sex':
#SEX COLUMN 
    
    st.title(
        "Sex")

    #Control space and rows (format)
    row3_1, row3_2 = st.columns(
        (1,1))
    
    #First row
    with row3_1:
        
        st.subheader(
            "Count Sex")

        st.image('imagen/Sex_count.png', width=550)
        
        st.markdown(
        "The graph shows that most of the passengers are men. Where 577 are male and 314 are female.")
    
    with row3_2:
        
        st.subheader(
            "% Sex")
        
        st.image('imagen/Sex_%.png', width=430)
        
        st.markdown(
        "Most of the passengers are male. There are 64.73% male.")

    #Second row
    with row3_1:
        
        st.subheader(
            "Sex - Fare - Survived")

        st.image('imagen/Sex_faresurvived.png', width=550)
        
        st.markdown(
        "The graph shows that men have the highest mortality rate compared to women. In addition, passenger mortality decreases when the rate is higher.")
    
    with row3_2:
        
        st.subheader(
            "Sex - Age - Pclass")
        
        st.image('imagen/Sex_agepclass.png', width=550)
        
        st.markdown(
        "It seems that there is a higher concentration of data on men. There is a concentration of data between the ages considered working, especially in lower-class men. In the first class, their data is concentrated from the age of 30 and above all on men.")

elif index == 'Age':
#AGE COLUMN 
    
    st.title(
        "Age")

    #Control space and rows (format)
    row4_1, row4_2 = st.columns(
        (1,1))
    
    #First row
    with row4_1:
        
        st.subheader(
            "Count Age")

        st.image('imagen/Age_count.png', width=580)
        
        st.markdown(
        "It seems that the greatest concentration of passenger ages is between 15 and 35 years. These are suitable ages for professional development and the search for a new life in America. It should also be mentioned that there is a large concentration of very young passengers.")
    
    with row4_2:
        
        st.subheader(
            "Age - Pclass")
        
        st.image('imagen/Age_pclass.png', width=750)
        
        st.markdown(
        "In the third class, there is a large amount of data on the working ages of many people who immigrated to America. In first class this reasoning is not fulfilled since rich people travel in this class, causing the ages to be concentrated above 30 years.")

#Second row
    with row4_1:
        
        st.subheader(
            "Age - Fare")

        st.image('imagen/Age_Fare.png', width=560)
        
        st.markdown(
        "This graph shows that more than half of the passengers have a very low fare and that their ages are between 15 and 35 years.")
    
    with row4_2:
        
        st.subheader(
            "Age - Fare - Survived")
        
        st.image('imagen/Age_survivedfare.png', width=550)
        
        st.markdown(
        "It can be seen in the graph that the possibility of survival is related to the price of the fare. The better class you have and the more expensive the fare, the more chances of surviving.")

elif index == 'SibSp':
#SIBSP COLUMN 
    
    st.title(
        "SibSp")
    st.markdown(
        'The SibSp column is defined as the number of siblings/spouses present of the person under consideration.')

    #Control space and rows (format)
    row5_1, row5_2 = st.columns(
        (1,1))
    
    #First row
    with row5_1:
        
        st.subheader(
            "SipSp - Survived")

        st.image('imagen/SibSp_Survived.png', width=580)
        
        st.markdown(
        "Relationship between number of siblings/spouses and survival.")
    
    with row5_2:
        
        st.subheader(
            "SipSp - Sex")
        
        st.image('imagen/SibSp_Sex.png', width=580)
        
        st.markdown(
        "Relationship between number of siblings/spouses and sex.")

    #Second row
    with row5_1:
        
        st.subheader(
            "SipSp - Age")

        st.image('imagen/SibSp_age.png', width=580)
        
        st.markdown(
        "Relationship between number of siblings/spouses and age.")
    
    with row5_2:
        
        st.subheader(
            "SipSp - Fare")
        
        st.image('imagen/SibSp_fare.png', width=580)
        
        st.markdown(
        "Relationship between number of siblings/spouses and fare.")

    #Third row
    with row5_1:
        
        st.subheader(
            "SipSp - Embarked")

        st.image('imagen/SibSp_Embarked.png', width=580)
        
        st.markdown(
        "Relationship between number of siblings/spouses and embarked.")

elif index == 'Parch':
#PARCH COLUMN 
    
    st.title(
        "Parch")
    st.markdown(
        'The Parch column is defined as the number of parents/children present of the person under consideration..')

    #Control space and rows (format)
    row6_1, row6_2 = st.columns(
        (1,1))
    
    #First row
    with row6_1:
        
        st.subheader(
            "Parch - Survived")

        st.image('imagen/Parch_survived.png', width=580)
        
        st.markdown(
        "Relationship between number of parents/children and survival.")
    
    with row6_2:
        
        st.subheader(
            "Parch - Sex")
        
        st.image('imagen/Parch_Sex.png', width=580)
        
        st.markdown(
        "Relationship between number of parents/children and sex.")

   #Second row
    with row6_1:
        
        st.subheader(
            "Parch - Embarked")

        st.image('imagen/Parch_Embarked.png', width=580)
        
        st.markdown(
        "Relationship between number of parents/children and embarked.")


elif index == 'Ticket':
#TICKET COLUMN 
    
    st.title(
        "Ticket")
    st.subheader(
            "% Top 10 Tickets")
    st.image('imagen/Ticket.png', width=600)
        
    st.markdown(
        "We can see the most popular passenger tickets and the percentage they represent.")


elif index == 'Fare':
#FARE COLUMN 
    
    st.title(
        "Fare")

    #Control space and rows (format)
    row7_1, row7_2 = st.columns(
        (1,1))
    
    #First row
    with row7_1:
        
        st.subheader(
            "Fare - Survived")

        st.image('imagen/Fare_survived.png', width=680)
        
        st.markdown(
        "Relationship between number of fare and survival.")
    
    with row7_2:
        
        st.subheader(
            "Fare - Sex - Survived")
        
        st.image('imagen/Sex_faresurvived.png', width=580)
        
        st.markdown(
        "The graph shows that men have the highest mortality rate compared to women. In addition, passenger mortality decreases when the rate is higher.")

#Second row
    with row7_1:
        
        st.subheader(
            "Fare - Embarked - Pclass")

        st.image('imagen/Pclass_fareembarked.png', width=680)
        
        st.markdown(
        "At first glance it can be seen that the first class is where these rich people are and the third class is poor people. The most expensive fares in each class come from Cherbourg and Southampton. Queenstown has the cheapest fares.")
    
    with row7_2:
        
        st.subheader(
            "Fare - Age - Survived")
        
        st.image('imagen/Age_survivedfare.png', width=620)
        
        st.markdown(
        "It can be seen in the graph that the possibility of survival is related to the price of the fare. The better class you have and the more expensive the fare, the more chances of surviving.")


else:
    
    st.title(
        "Embarked")

    #Control space and rows (format)
    row8_1, row8_2 = st.columns(
        (1,1))
    
    #First row
    with row8_1:
        
        st.subheader(
            "Count Embarked")

        st.image('imagen/Embarked_count.png', width=680)
        
        st.markdown(
        "The graph shows that the majority of passengers boarded at Southampton. Where 646 in Southampton, 168 in Cherbourg and 77 in Queenstown.")
    
    with row8_2:
        
        st.subheader(
            "% Embarked")
        
        st.image('imagen/Embarked_%.png', width=580)
        
        st.markdown(
        "Most of the passengers boarded at Southampton.")

#Second row
    with row8_1:
        
        st.subheader(
            "Embarked - Survived")

        st.image('imagen/Embarked_survived.png', width=720)
        
        st.markdown(
        "The graph shows that the majority of passengers boarded at Southampton. Relationship between number of fare and survival.")
    
    with row8_2:
        
        st.subheader(
            "Embarked - Pclass")
        
        st.image('imagen/Pclass_embarked.png', width=560)
        
        st.markdown(
        "The graph indicates that the vast majority of passengers who boarded in Southampton regardless of class.")

#Third row
    with row8_1:
        
        st.subheader(
            "Embarked - Fare - Pclass")

        st.image('imagen/Pclass_fareembarked.png', width=720)
        
        st.markdown(
        "At first glance it can be seen that the first class is where these rich people are and the third class is poor people. The most expensive fares in each class come from Cherbourg and Southampton. Queenstown has the cheapest fares..")


st.set_option('deprecation.showPyplotGlobalUse', False)


#SIDEBAR part 2
music= st.sidebar.checkbox('Do you want to listen to music?', help='If you want to listen to music, you have to click')
if music:
    st.sidebar.audio('music/titanic_song.mp3', 'rb')

st.sidebar.write('---')

st.sidebar.write('Do you know there is a Titanic movie?')

if(st.sidebar.button("Curiosity")):
    st.sidebar.write('Everybody knew that Jack would fit on the board')
    st.sidebar.image('https://imagenes.20minutos.es/files/article_default_content/uploads/imagenes/2012/09/13/3009744.jpg', 
        width=300,caption='New from Cinemania')
