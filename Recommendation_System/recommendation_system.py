"""Content-Based Movie Recommendation System.
Run: python recommendation_system.py
"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.DataFrame({
    'title': [
        'The Matrix', 'John Wick', 'Inception', 'Interstellar', 'The Dark Knight',
        'Avengers', 'Iron Man', 'Shutter Island', 'Tenet', 'Doctor Strange'
    ],
    'description': [
        'sci fi virtual reality artificial intelligence action',
        'action crime assassin revenge thriller',
        'dreams subconscious mind sci fi thriller',
        'space time black hole science fiction emotional',
        'superhero crime action dark justice',
        'superhero team action alien invasion marvel',
        'superhero technology billionaire action marvel',
        'psychological thriller mystery mental hospital',
        'time inversion spy sci fi action thriller',
        'magic multiverse superhero fantasy marvel'
    ]
})

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(movies['description'])
similarity = cosine_similarity(tfidf_matrix)


def recommend(movie_title, top_n=5):
    movie_title = movie_title.strip().lower()
    matches = movies[movies['title'].str.lower() == movie_title]
    if matches.empty:
        return []
    idx = matches.index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    return [(movies.iloc[i]['title'], round(score, 2)) for i, score in scores]


if __name__ == '__main__':
    print('Available movies:')
    for title in movies['title']:
        print('-', title)

    choice = input('\nEnter a movie name: ')
    results = recommend(choice)

    if not results:
        print('Movie not found. Please enter a movie from the list.')
    else:
        print('\nRecommended Movies:')
        for title, score in results:
            print(f'{title}  | Similarity Score: {score}')
