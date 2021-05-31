import itunespy
#kind, collectionName, trackName, collectionPrice, trackPrice, primaryGenreName, trackCount, trackNumber, releaseDate.
artist = itunespy.search_artist('The Beatles')  # Returns a list
albums = artist[0].get_albums()  # Get albums from the first result
for album in albums:
    album_name = album
    album = itunespy.lookup(album.collection_id)
    tracks = album[0].get_tracks()  # Get tracks from the first result
    if tracks == []:
        pass
    else:
        print("---------------------------------------")
        print("collectin name^^^^")
        print(album_name.collection_name, album_name.primaryGenreName, album_name.track_count, album_name.release_date, album_name.collection_id)
        for track in tracks:
           print(str(track.track_number) + " " + track.kind + " " + track.collection_name + ': ' + track.track_name + " price " + str(track.track_price) + "time: "  + str(track.get_track_time_minutes()))
        print('Total playing time: ' + str(album[0].get_album_time()))



