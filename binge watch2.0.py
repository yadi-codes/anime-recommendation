import pandas as pd
from jikanpy import Jikan
jikan=Jikan()
anime_data=jikan.top(type='anime',page=1)
anime_list=[]
for anime in anime_data['data']:
    anime_info={
        'Title':anime['title'],
        'Genre':','.join([genre['name'] for genre in anime['genres']]),
        'Episodes':anime['episodes'],
        'Score': anime['score'],
        'Rank':anime['rank'],
        'URL':anime['url']
    }
    anime_list.append(anime_info)
anime_df=pd.DataFrame(anime_list)
print(anime_df.head())
def recommend_anime(genre=None,min_score=0):
    filtered_df=anime_df
    if genre:
        filtered_df=filtered_df[filtered_df['Genre'].str.contains(genre,case=False,na=False)]
    if min_score>0:
        filtered_df=filtered_df[filtered_df['Score']>=min_score]
        return filtered_df[['Title','Genre','Score','Episodes','Rank','URL']]
try:
    genre_input = input('Which genre would you like to watch? ')
    score_input = int(input('Enter the minimum score for your anime: '))
    
    recommended_animes = recommend_anime(genre=genre_input, min_score=score_input)
    print(recommended_animes)
except ValueError:
    print("Please enter a valid number for the score.")
