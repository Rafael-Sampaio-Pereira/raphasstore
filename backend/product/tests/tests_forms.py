from PIL import Image
from io import BytesIO # Python 2: from StringIO import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from ..forms import CsvImportForm

def test_csvform(self):
    im = Image.new(mode='RGB', size=(200, 200)) # create a new image using PIL
    im_io = BytesIO() # a BytesIO object for saving image
    im.save(im_io, 'JPEG') # save the image to im_io
    im_io.seek(0) # seek to the beginning

    image = InMemoryUploadedFile(
        im_io, None, 'random-name.jpg', 'image/jpeg', len(im_io.getvalue()), None
    )

    post_dict = {'title': 'Test Title'}
    file_dict = {'image': image}

    form = CsvImportForm(data=post_dict, files=file_dict)