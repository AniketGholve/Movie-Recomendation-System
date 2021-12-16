from tkinter import *
import pandas as pd
import numpy as np
import wget
import requests
import pprint
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image, ImageTk
import cv2

def Recomend():
    def get_title_from_index(index):
        return df[df.index == index]["movie_title"].values[0]
    def get_index_from_title(title):
        title=title.lower()
        try:
            str1=df[df.movie_title==title]["index"].values[0]
            return str1
        except Exception as e:
            txt.insert(0.0,"no movie in data base")  
    df=pd.read_csv("new_data.csv")
    features=['genres','director_name','actor_1_name','actor_2_name','actor_3_name']

    for feature in features:
        df[feature]=df[feature].fillna('')
    def combine_row(row):
        return row['genres']+" "+row['director_name']+" "+row['actor_1_name']+" "+row['actor_2_name']+" "+row['actor_3_name'];
    
    df["combine_features"]=df.apply(combine_row,axis=1)
    cv=CountVectorizer()
    count_matrix=cv.fit_transform(df["combine_features"])
    cosine_sim=cosine_similarity(count_matrix)
    movie_user_likes=moviename.get()


    movie_index=get_index_from_title(movie_user_likes)

    similar_movies=list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movie=sorted(similar_movies,key=lambda x:x[1] , reverse=True)
    i=0
    for movie in sorted_similar_movie:
        ins=get_title_from_index(movie[0])
        if(i>0):
             photo(ins,i)
        i=i+1
        if i>3:
            break;
        
            
            
def photo(mname,i):
    api_key = "c6d9b9c2ffe1197d725e93bfdcf4325c"
    api_base_url = f"https://api.themoviedb.org/3"
    endpoint_path = f"/search/movie"
    searh_query = mname
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={searh_query}"
    # print(endpoint)
    r = requests.get(endpoint)
    # pprint.pprint(r.json())
    if r.status_code in range(200, 299):
        data = r.json()
        results = data['results']
        if len(results) > 0:
            # print(results[0].keys())
            movie_ids = set()
            for result in results:
                _id = result['id']
                # print(result['title'], _id)
                movie_ids.add(_id)
            # print(list(movie_ids))
    for movie_id in movie_ids:
        api_version = 3
        api_base_url = f"https://api.themoviedb.org/{api_version}"
        endpoint_path = f"/movie/{movie_id}/images"
        endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
        r = requests.get(endpoint)
    if r.status_code in range(200, 299):
       data = r.json()
       fetch=data['posters']
       url=fetch[0]['file_path']
       print(url)
       image_url=f"https://image.tmdb.org/t/p/w500{url}"
       image_filename = wget.download(image_url)
       print('Image Successfully Downloaded: ', image_filename)
       str1="D:\\Recomendation System\\"+image_filename
       image=cv2.imread(str1)
       scale_percentage=.50
       wid=int(image.shape[1]*scale_percentage)
       hei=int(image.shape[0]*scale_percentage)
       dimension=(wid,hei)
       resized=cv2.resize(image,dimension,interpolation=cv2.INTER_AREA)
       cv2.imwrite(image_filename,resized)
       image = Image.open(str1)
       photo = ImageTk.PhotoImage(image)
       label = Label(root, image = photo)
       label.image = photo
       if i==1:
           label.grid(row=7,sticky=EW)
       elif i==2:
           label.grid(row=7,sticky=W)
       elif i==3:
           label.grid(row=7,sticky=E)
       
       
       
       
       
       
       
root= Tk()
root.geometry("1200x900")
moviename=StringVar()
label=Label(root, text="Movie Recomendation System",font=('Aerial 15 bold'))
label.grid(row=1, column=0)
label.grid_rowconfigure(1, weight=1)
movie=Entry(root,textvariable=moviename)
movie.grid(row=2,column=0)
button=Button(bg="red",text="Search",command=Recomend)
button.grid(row=4,column=0)
root.grid_rowconfigure(1, weight=0)
root.grid_columnconfigure(0, weight=1)
root.mainloop()