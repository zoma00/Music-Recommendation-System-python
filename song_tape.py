import os
import time
from faker import Faker
import random

# Initialize Faker
fake = Faker()

class Song:
    def __init__(self, title, artist, genre):
        self.title = title
        self.artist = artist
        self.genre = genre

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.play_count = {}
        self.top_genres = None

    def listen(self, song):
        if song not in self.play_count:
            self.play_count[song] = 0
        self.play_count[song] += 1

def calculate_top_genres(user):
    sorted_plays = sorted(user.play_count.items(), key=lambda item: item[1], reverse=True)
    if not sorted_plays:
        return None
    user.top_genres = [play[0].genre for play in sorted_plays[:2]]

def recommend_songs(user, song_catalog):
    recommendations = []
    if user.top_genres:
        for genre in user.top_genres:
            for song in song_catalog:
                if song.genre == genre and song not in user.play_count:
                    recommendations.append(song)
                    break
    random_songs = random.sample(song_catalog, min(5, len(song_catalog) - len(recommendations)))
    recommendations.extend(random_songs)
    return recommendations

def generate_random_songs(num_songs):
    genres = ["Pop", "Rock", "Jazz", "Classical", "Hip Hop", "Electronic"]
    return [Song(fake.sentence(nb_words=3), fake.name(), random.choice(genres)) for _ in range(num_songs)]


# Generate a catalog of random songs
song_catalog = generate_random_songs(20)

# User 1
user1 = User(1)
user1.listen(random.choice(song_catalog))
user1.listen(random.choice(song_catalog))
user1.listen(random.choice(song_catalog))
user1.listen(random.choice(song_catalog))

calculate_top_genres(user1)
recommendations_user1 = recommend_songs(user1, song_catalog)

print("User 1 Preferences:")
print(f"User ID: {user1.user_id}")
print("Songs Played:")
for song, count in user1.play_count.items():
    print(f"- {song.title} by {song.artist} (Genre: {song.genre}, Plays: {count})")

print("\nRecommended songs for user", user1.user_id)
for song in recommendations_user1:
    box_width = 40
    title_length = len(song.title)
    padding_left = (box_width - title_length) // 2
    padding_right = box_width - title_length - padding_left
    print("+" + "-" * box_width + "+")
    print(f"| {' ' * padding_left}{song.title}{' ' * padding_right} |")
    print("+" + "-" * box_width + "+")

# User 2
user2 = User(2)
user2.listen(random.choice(song_catalog))
user2.listen(random.choice(song_catalog))
user2.listen(random.choice(song_catalog))
user2.listen(random.choice(song_catalog))

calculate_top_genres(user2)
recommendations_user2 = recommend_songs(user2, song_catalog)

print("\nUser 2 Preferences:")
print(f"User ID: {user2.user_id}")
print("Songs Played:")
for song, count in user2.play_count.items():
    print(f"- {song.title} by {song.artist} (Genre: {song.genre}, Plays: {count})")

print("\nRecommended songs for user", user2.user_id)
for song in recommendations_user2:
    box_width = 40
    title_length = len(song.title)
    padding_left = (box_width - title_length) // 2
    padding_right = box_width - title_length - padding_left
    print("+" + "-" * box_width + "+")
    print(f"| {' ' * padding_left}{song.title}{' ' * padding_right} |")
    print("+" + "-" * box_width + "+")



def draw_tape(position):
    tape_length = 30
    tape = "-" * tape_length
    print(f"\n{' ' * 5}{tape}")
    print(f"{' ' * position}^")