import sys
import osxphotos


file_to_list = '/Users/Rob/Pictures/FPA_Test.photoslibrary'


phdb = osxphotos.PhotosDB(dbfile=file_to_list)

print(phdb.keywords)

all_keywords = phdb.keywords

all_photos = phdb.photos()

ernie = all_photos[26].exif_info
iso = ernie.iso

sb = []
sb.append(",".join(str(x) for x in all_keywords))
sb.append(str(iso))

single_line_csv = ','.join(sb)

print('Finished')