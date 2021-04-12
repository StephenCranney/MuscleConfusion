# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Load scraped repository of exercises from bodybuilding.com

import re, json, requests
import pandas as pd

url = 'https://raw.githubusercontent.com/Bipinoli/scraping_body_building_data/master/final_data/allExercises/allExercises.json'
resp = requests.get(url)
data = json.loads(resp.text)
allex = pd.DataFrame.from_dict(data)

#Randomly select one exercise per muscle group, weighted by quality. 

allex['weight']=allex['avg_rating']/ allex['avg_rating'].groupby(allex['targeted_muscle']).sum()

#Could, but too many missing avg_ratings, just use basic random draw

allexlist= allex['targeted_muscle'].unique().tolist()

for i in allexlist:
    print(i+ " exercise for today is "+allex[allex['targeted_muscle']==i].sample(1)['name'].to_string())



