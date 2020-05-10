def make_album(singer_name,singer_album,music_number=""):
    musician = {"singer_name":singer_name.title(),"singer_album":singer_album.title()}
    if music_number:
        musician["music_number"] = music_number
    return musician
while True:
    print("\nplease enter the infos to make album.")
    print("enter 'q' to quit !")
    singer_name = input("singer_name:")
    if singer_name == "q":
        break
    singer_album = input("singer_album:")
    music_number = input("music_number:")
    album = make_album(singer_name,singer_album,music_number)
    print(album)
