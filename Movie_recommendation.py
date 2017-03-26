import numpy as np
import pandas as pd

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')
ratings.drop(['timestamp'],axis=1,inplace = True)

movies.head()

ratings.head()

def replace_name(x):
	return movies[movies['movieId']==x].title.values[0]

ratings.movieId = ratings.movieId.map(replace_name)

ratings.head()

M = ratings.pivot_table(index=['userId'],columns=['movieId'],values='rating')
M.shape

def corr(s1,s2):
	#take 2 pd.series objects and return correlation between them
	s1_c = s1 - s1.mean()
	s2_c = s2 - s2.mean()
	return np.sum(s1_c * s2_c)/np.sqrt(np.sum(s1_c**2)*np.sum(s2_c**2))
	
def get_recs(movie_name,M,num):
	#num : number of recommendations
	import numpy as np
	genres = []
	reviews = []
	for title in M.columns:
		if title == movie_name:
			genres.append()
		cor = corr(M[movie_name], M[title])
		if np.isnan(cor):
			continue
		else:
			reviews.append((title,cor))
	
	reviews.sort(key = lambda tup: tup[1], reverse = True)
	return reviews[:num]

n = int(raw_input('Enter the required no. of recommendations:'))
mov = raw_input('Enter the name of a movie that you liked:')

lst = get_recs(mov,M,n)
print 'Recommendations for you:',lst