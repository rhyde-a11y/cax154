# TODO: Create your tuple here
destination = (34.0522, -118.2437)

# TODO: Access index 0 and index 1 using square brackets [] and print them
lat_index = destination[0]
lon_index = destination[1]
print(f"Indexed Lat: {lat_index}, Lon: {lon_index}")

# TODO: Unpack the destination tuple into 'latitude' and 'longitude' variables
latitude, longitude = destination

# --- Test Your Mission ---
print(f"Unpacked Latitude: {latitude}")
print(f"Unpacked Longitude: {longitude}")