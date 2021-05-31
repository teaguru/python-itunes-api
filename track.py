import itunespy

album = itunespy.search_album('The Beatles for Kids - Morning, Afternoon & Night - EP')  # Returns a list
print(album)
print("album[0", album[0])
tracks = album[0].get_tracks()  # Get tracks from the first result

for track in tracks:
    print(track.artist_name + ': ' + track.track_name + str(track.get_track_time_minutes()))
print('Total playing time: ' + str(album[0].get_album_time()))

