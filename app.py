import streamlit as st
import pandas as pd
import preprocessor
import helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import scipy

df = pd.read_csv('athlete__info.csv')
region_df = pd.read_csv('noc.csv')


df = preprocessor.preprocess(df,region_df)

st.sidebar.title("Olympics Analysis")
st.sidebar.image('data:image/png;base64,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')
user_menu = st.sidebar.radio(
    'Select an option',
    ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete-wise Analysis')
)


if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country",country)
    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")

    if selected_year != "Overall" and selected_country == 'Overall':
        st.title("Medal Tally in "+str(selected_year) + "Olympics")

    if selected_year == "Overall" and selected_country != 'Overall':
        st.title("Medals Won by" + selected_country)

    if selected_year != "Overall" and selected_country != 'Overall':
        st.title("Medals Won by " + selected_country + " in " + str(selected_year) + " Olympics")

    st.table(medal_tally)

if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0] -1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    nations_over_time = helper.data_over_time(df,'region')
    fig = px.line(nations_over_time, x="Year", y="region")
    st.title("Participating Nations over the Years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x="Year", y="Event")
    st.title("Events over the Years")
    st.plotly_chart(fig)

    athlete_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athlete_over_time, x="Year", y="Name")
    st.title("Athletes over the Years")
    st.plotly_chart(fig)

    st.title("No. of Events over time(Every Sport)")
    fig, ax = plt.subplots(figsize = (20,20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
        annot=True)
    st.pyplot(fig)

    st.title("Most Successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')
    selected_sport = st.selectbox('Select a Sport',sport_list)
    x = helper.most_successful(df, selected_sport)
    st.table(x)

if user_menu == 'Country-wise Analysis':

    st.sidebar.title('Country-wise Analysis')
    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox('Select a Country',country_list)

    country_df =  helper.yearwise_medal_tally(df, selected_country)
    fig = px.line(country_df, x="Year", y="Medal")
    st.title(selected_country + " Medal Tally over the Years")
    st.plotly_chart(fig)

    st.title(selected_country + " shines in the following sports")
    pt = helper.country_event_heatmap(df,selected_country)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pt,annot=True)
    st.pyplot(fig)

    st.title("Top 10 athletes of " + selected_country)
    top10_df = helper.most_successful_countrywise(df,selected_country)
    st.table(top10_df)

if user_menu == 'Athlete-wise Analysis':
    athlete_df = df.drop_duplicates(subset = ['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
          show_hist = False, show_rug = False)
    fig.update_layout(autosize=False, width = 1000, height=600)
    st.title("Distribution of Age")
    st.plotly_chart(fig)

    x = []
    name=[]
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-of-War', 'Athletics', 'Swimming', 'Badminton', 'Sailing',
                     'Gymnastics', 'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling', 'Water Polo', 'Hockey',
                     'Rowing', 'Fencing', 'Shooting', 'Boxing', 'Taekwondo', 'Cycling','Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery', 'Volleyball', 'Synchronized Swimming', 'Table Tennis',
                     'Baseball', 'Rhythmic Gymnastics', 'Rugby Sevens', 'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        if not temp_df.empty:
         temp_age = temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna()
         x.append(temp_age)
         name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=600)
    st.title("Distribution of Age wrt Sports")
    st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('Height vs Weight')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df = helper.weight_v_height(df,selected_sport)
    fig,ax = plt.subplots()
    ax = sns.scatterplot(x='Weight', y='Height', data=temp_df, hue ='Medal', style='Sex', s=60)
    st.pyplot(fig)

    st.title("Men vs Women Participation over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x='Year', y=['Male', 'Female'])
    st.plotly_chart(fig)
