def make_album(singer_name,singer_album,music_number=""):
    musician={"singer_name":singer_name.title(),"singer_album":singer_album.title()}
    if music_number:
        musician["music_number"]=music_number
    return musician
album1=make_album("Jay zhou","青花瓷",30)
print(album1)