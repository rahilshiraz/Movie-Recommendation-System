import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#helper functions
def get_title_from_index(index):
	return df[df['index'] == index].title.values[0]

def get_index_from_title(title):
	return df[df['title'] == title].index.values[0]


#Read CSV File
df = pd.read_csv("movie_dataset.csv")
# print(df.columns)

#Select Features
features = ['keywords','genres','cast','director','vote_count','popularity']
for feature in features:
	df[feature] = df[feature].fillna('')

#Create a column in DF which combines all selected features
def combine_feature(row):
	try:
		return (row['keywords'] + ' ' +  row['genres'] + ' ' + row['cast'] + ' ' +  row['director'] +
					' ' +  str(row['vote_count']) + ' ' +  str(row['popularity']))
	except:
		print("Error:",row)

df['combined_features'] = df.apply(combine_feature,axis = 1)
# print(df['combined_features'].head())

#Create count matrix from this new combined column
cv = CountVectorizer()
count_matrix = cv.fit_transform(df['combined_features'])

#Compute the Cosine Similarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix)
movie = input("Enter your last watched movie: ")

#Get index of this movie from its title
movie_index = get_index_from_title(movie)

#Get a list of similar movies in descending order of similarity score
similarmovies = list(enumerate(cosine_sim[movie_index]))
sorted_similarmovies = sorted(similarmovies,key=lambda x:x[1],reverse=True)

#Print titles of first 50 movies
count = 0
print("You would want to watch these as well: ")
for movie in sorted_similarmovies:
	count += 1
	if count == 1:
		continue
	if count != 10:
		print(' '*8 + get_title_from_index(movie[0]))
	else:
		break