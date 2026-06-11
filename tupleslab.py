destination = 40.7060, -73.9970
latitude=destination[0]
longitude=destination[1]
print(f"Indexed Lat: {latitude}, Lon: {longitude}")

latitude, longitude = destination
print(f"Unpacked Latitude: {latitude}")
print(f"Unpacked Longitude: {longitude}")