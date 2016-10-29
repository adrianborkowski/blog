from wall.models import Post
from PIL import Image
from PIL.ExifTags import TAGS


def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


def add_coordinates():
    post = Post.objects.last()
    metadata = get_exif(post.image)

    def dms2dd(i):
        decs = float(i[0][0])
        mins = float(i[1][0])/60
        secs = float(i[2][0])/36000000
        return decs + mins + secs

    post.lat = dms2dd(metadata['GPSInfo'][2])
    post.lon = dms2dd(metadata['GPSInfo'][4])
    post.save()


