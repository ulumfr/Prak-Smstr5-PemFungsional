from functools import reduce

movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Mana: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time To Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Ethernals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

def count_movies_by_genre(movies):
    genre_counts = {genre: len(list(filter(lambda x: x["genre"] == genre, movies)) ) for genre in set(map(lambda x: x["genre"], movies))}
    return genre_counts

def average_rating_by_year(data):
    temp = list(set(data["year"] for data in data))

    def ratingSum(year):
        movieFilter = list(filter(lambda x: x["year"] == year, data))
        ratingFilter = map(lambda x: x["rating"],movieFilter)
        totalSum = reduce(lambda x, y: x + y, ratingFilter)
        return totalSum

    def average(year):
        temp = list(filter(lambda x: x["year"] == year, data))
        totalSum = ratingSum(year)
        totalAverage = totalSum / len(temp)
        return year, totalAverage

    average_ratings = dict(map(average, temp))
    return average_ratings

find_highest_rated_movie = lambda movies: max(movies, key=lambda x: x["rating"])
    
def find_movie_info_by_title(movies, title):
    matching_movies = list(filter(lambda movie: movie["title"].lower() == title.lower(), movies))
    return matching_movies[0] if matching_movies else None

def display_menu():
    print("\n=== Pengolahan Data Film ===")

    while True:
        print("\nPilih tugas yang ingin dilakukan: ")
        print("1. Menghitung jumlah film berdasarkan genre")
        print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
        print("3. Menemukan film dengan rating tertinggi")
        print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
        print("5. Selesai (Exit)")
        pilih = int(input("\nMasukan nomor tugas (1/2/3/4/5) : "))

        if pilih == 1:
            print("Jumlah Film Berdasarkan Genre: ")
            print(count_movies_by_genre(movies))

        elif pilih == 2:
            print("Rata-rata Rating Film Berdasarkan Tahun Rilis:")
            print(average_rating_by_year(movies))

        elif pilih == 3:
            highest_rated_movie = find_highest_rated_movie(movies)
            print("Film dengan Rating Tertinggi:")
            print("\nInformasi Film:", highest_rated_movie["title"])
            print("Rating:", highest_rated_movie["rating"])
            print("Tahun Rilis:", highest_rated_movie["year"])
            print("Genre:", highest_rated_movie["genre"])

        elif pilih == 4:
            title = input("Masukkan judul film yang ingin dicari: ")
            movie = find_movie_info_by_title(movies, title)
            if movie:
                print("\nInformasi Film:", movie["title"])
                print("Rating:", movie["rating"])
                print("Tahun Rilis:", movie["year"])
                print("Genre:", movie["genre"])
            else:
                print("Film dengan judul tersebut tidak ditemukan.")

        elif pilih == 5:
            break

        else:
            print("Pilihan tidak ada, Coba Lagi !!!")

if __name__ == "__main__":
    display_menu()