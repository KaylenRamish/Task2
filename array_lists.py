class Album:
    def __init__(self, albumName, albumArtist, numberOfSongs):
        self._albumName = albumName
        self._albumArtist = albumArtist
        self._numberOfSongs = numberOfSongs
        
    @property
    def albumName(self):
        return self._albumName
    
    @albumName.setter
    def albumName(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._albumName = value
        else:
            raise ValueError("Invalid album name")
    
    @property
    def albumArtist(self):
        return self._albumArtist
    
    @albumArtist.setter
    def albumArtist(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._albumArtist = value
        else:
            raise ValueError("Invalid artist name")
    
    @property
    def numberOfSongs(self):
        return self._numberOfSongs
    
    @numberOfSongs.setter
    def numberOfSongs(self, value):
        if isinstance(value, int) and value >= 0:
            self._numberOfSongs = value
        else:
            raise ValueError("Invalid number of songs")
        
    def __str__(self):
        return f"({self._albumName}, {self._albumArtist}, {self._numberOfSongs})"
    
def print_albums(album_list, title):
    print(f"\n{title}:")
    for album in album_list:
        print(album)

def sort_albums_by_songs(album_list):
    album_list.sort(key=lambda album: album.numberOfSongs)

def swap_albums(album_list, index1, index2):
    album_list[index1], album_list[index2] = album_list[index2], album_list[index1]

def search_album_by_name(album_list, search_name):
    index = next((i for i, album in enumerate(album_list) if album.albumName == search_name), None)
    return index

# Creating and manipulating albums1 list
albums1 = [
    Album("Album1", "Artist1", 10),
    Album("Album2", "Artist2", 8),
    Album("Album3", "Artist3", 12),
    Album("Album4", "Artist4", 5),
    Album("Album5", "Artist5", 7)
]

print_albums(albums1, "Albums1 List")
sort_albums_by_songs(albums1)
print_albums(albums1, "Sorted Albums1 List")
swap_albums(albums1, 1, 2)
print_albums(albums1, "Albums1 List after swapping")

# Creating and manipulating albums2 list
albums2 = [
    Album("Album6", "Artist6", 9),
    Album("Album7", "Artist7", 15),
    Album("Album8", "Artist8", 11),
    Album("Album9", "Artist9", 4),
    Album("Album10", "Artist10", 6)
]

print_albums(albums2, "Albums2 List")
albums2.extend(albums1)

# Adding new albums
albums2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
albums2.append(Album("Oops!... I Did It Again", "Britney Spears", 16))

# Sorting albums2 list alphabetically by album name
albums2.sort(key=lambda album: album.albumName)

print_albums(albums2, "Sorted Albums2 List")

# Search for "Dark Side of the Moon" in albums2 and print its index
search_album = "Dark Side of the Moon"
index = search_album_by_name(albums2, search_album)
if index is not None:
    print(f"\nIndex of '{search_album}' in Albums2: {index}")
else:
    print(f"'{search_album}' not found in Albums2")
