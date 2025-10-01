#پیشنهاد موسیقی
all_users = {}
all_albums = {}

def add_user(username: str, age: int, city: str, albums: list, all_users: dict) -> None:
    all_users[username] = {
        'age' : age,
        'city' :city,
        'albums' : albums
    }
def add_album(name: str, artist: str, genre: str, tracks: int, all_albums: dict) -> None:
    all_albums[name] = {
        'artist' :artist,
        'genre' : genre,
        'tracks' : tracks
    }

def query_user_artist(username: str, artist: str, all_users: dict, all_albums: dict) -> int:
    count_track = 0
    if all_users:
        if username in all_users:
            for album in all_users[username]['albums']:
                if album in all_albums and all_albums[album]['artist'] == artist:
                    count_track += all_albums[album]['tracks'] 
    return count_track      

def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    count_track = 0
    if all_users:
        if username in all_users:
            for album in all_users[username]['albums']:
                if album in all_albums and all_albums[album]['genre'] == genre:
                    count_track += all_albums[album]['tracks'] 
    return count_track

def query_age_artist(age: int, artist: str, all_users: dict, all_albums: dict) -> int:
    count_track = 0
    filter_users = {user:info for user,info in all_users.items() if all_users[user]['age'] == age} 
    if filter_users:
        for user in filter_users:
             for album in all_users[user]['albums']:
                if album in all_albums and all_albums[album]['artist'] == artist:
                    count_track += all_albums[album]['tracks'] 
    return count_track

def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
    count_track = 0
    filter_users = {user:info for user,info in all_users.items() if all_users[user]['age'] == age} 
    if filter_users:
        for user in filter_users:
             for album in all_users[user]['albums']:
                if album in all_albums and all_albums[album]['genre'] == genre:
                    count_track += all_albums[album]['tracks'] 
    return count_track

def query_city_artist(city: str, artist: str, all_users: dict, all_albums: dict) -> int:
    count_track = 0
    filter_users = {user:info for user,info in all_users.items() if all_users[user]['city'] == city} 
    if filter_users:
        for user in filter_users:
             for album in all_users[user]['albums']:
                if album in all_albums and all_albums[album]['artist'] == artist:
                    count_track += all_albums[album]['tracks'] 
    return count_track

def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
    count_track = 0
    filter_users = {user:info for user,info in all_users.items() if all_users[user]['city'] == city} 
    if filter_users:
        for user in filter_users:
             for album in all_users[user]['albums']:
                if album in all_albums and all_albums[album]['genre'] == genre:
                    count_track += all_albums[album]['tracks'] 
    return count_track

add_user("SAliB", 19, "Tehran", ["tekunbede", "barf", "gavazn"], all_users)
add_user("Saeid", 22, "Esfehan", ["eclipse", "barf", "gavazn"], all_users)
add_album("eclipse", "malmsteen", "classic", 10, all_albums)
add_album("barf", "beeptunes", "pop", 22, all_albums)
add_album("tekunbede", "beeptunes", "pop", 14, all_albums)
add_album("gavazn", "sorena", "persian", 18, all_albums)
add_user("Ali", 12, "Bushehr", ["bidad", "blaze"], all_users)
add_album("bidad", "shajarian", "classic", 10, all_albums)
add_album("blaze", "ghorbani", "pop", 9, all_albums)
query_user_artist("Ali", "ghorbani", all_users, all_albums)
query_user_genre("Ali", "classic", all_users, all_albums)
query_age_artist(12, "shajarian", all_users, all_albums)
query_age_genre(12, "pop", all_users, all_albums)
query_city_artist("Bushehr", "ghorbani", all_users, all_albums)
print(query_city_genre("Bushehr", "pop", all_users, all_albums))