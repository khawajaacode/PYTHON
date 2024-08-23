from lib2to3.fixes.fix_input import context


def movies_to_file():
    with open('movies.txt', 'w') as file:
        while True:
            movie = input("Enter a movie name(or type 'done' to finish): ")
            if movie == 'done':
                break
            file.write(movie+ "\n")


movies_to_file()
print("Movies has been Saved to 'movies.txt'.")




def read_movies_to_file():
 with open('movies.txt', 'r') as file:
  for line in file:
    print(line)



read_movies_to_file()


def copy_movies_to_file(source, destination):
 with open(source, 'r') as src:
  content = src.read()

  with open(destination, 'w') as dest:
   dest.write(content)


copy_movies_to_file("movies.txt", "movies_copy.txt")
print("Movies has been copied to 'movies_copy.txt'.")



def count_words_in_filename(filename):
    with open(filename, "r") as file:
        content = file.read()
        words = content.split()
        return len(words)


word_count = count_words_in_filename("movies.txt")
print(f"The file contains {word_count} words.")



from datetime import datetime

def log_current_time():
    with open("log.txt", "a") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Log entry at: {current_time}\n")

log_current_time()
print("Current time has been logged.")
