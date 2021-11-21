import sys
import osxphotos


file_to_list = '/Users/Rob/Pictures/FPA_Test.photoslibrary'


phdb = osxphotos.PhotosDB(dbfile=file_to_list)

print(phdb.keywords)

all_photos = phdb.photos()

ernie = all_photos[26].exif_info

print('Finished')