from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# django rest framwork library importing method
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#models
from .models import Dropbox
#serilizers
from .serializers import DropboxSerializer
import cv2
import pytesseract
from pytesseract import Output
def index(request):
    return HttpResponse("Hello, world!")

from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
class DropboxList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    parser_classes = (FileUploadParser, MultiPartParser, FormParser)
    #parser_classes = [FileUploadParser]
    def get(self, request, format=None):
        dropbox = Dropbox.objects.all()
        serializer = DropboxSerializer(dropbox, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        file_obj = request.data['file']
        serializer = DropboxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DropboxDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    #parser_classes = (MultiPartParser, FormParser)
    def get_object(self, pk):
        try:
            return Dropbox.objects.get(pk=pk)
        except Dropbox.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dropbox = self.get_object(pk)
        serializer = DropboxSerializer(dropbox)
        return Response(serializer.data)
        
    parser_classes = (FileUploadParser, MultiPartParser, FormParser)
    def put(self, request, pk, format=None):
        dropbox = self.get_object(pk)
        serializer = DropboxSerializer(dropbox, data=request.data)
        #file = self.request.FILES['file']
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def last(request):
    documents = Dropbox.objects.all()
    #rank = Document.objects.latest('id')
    #print(rank)
    for obj in documents:
        rank = obj.document.url
        #print(rank)
    print(rank)
    #return HttpResponse("Hello, world!")
    return HttpResponse("http://127.0.0.1:8000"+rank)


from django.http import JsonResponse
from PIL import Image
import urllib.request
def imgtotext(request):
    documents = Dropbox.objects.all()
    #rank = Document.objects.latest('id')
    #print(rank)
    for obj in documents:
        rank = obj.document.url
        #print(rank)
    print(rank)
    #return HttpResponse("Hello, world!")
    #file_name = "test.JPEG"
    file_name= rank
    #image_file = 'location'
    #file_name = Image.open(rank)
    #URL = 'http://www.w3schools.com/css/trolltunga.jpg'
   
    #img = Image.open('temp.jpg')
    URL = "http://127.0.0.1:8000"+rank

    with urllib.request.urlopen(URL) as url:
        with open('temp.jpg', 'wb') as f:
            f.write(url.read())
    #file_name = Image.open('temp.jpg')
    file_name = "temp.jpg"
    image = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE) 
    custom_config = r'--oem 1 --psm 3'
    extracted_text = pytesseract.image_to_string(image, config=custom_config)
    #print(extracted_text)
    words_list = extracted_text.split('\n')
    #print(words_list)
    res = []
    for i in words_list:
        if i.strip() != '':
            res.append(i)
    print(res)
    #return HttpResponse("http://127.0.0.1:8000"+rank)
    return JsonResponse({'code': 1, 'status':'200', 'data': res})
    #return HttpResponse("http://127.0.0.1:8000"+rank)


# from PIL import Image
# import urllib.request
# def imgtotext(request):
#     documents = Dropbox.objects.all()
#     #rank = Document.objects.latest('id')
#     #print(rank)
#     for obj in documents:
#         rank = obj.document.url
#         #print(rank)
#     print(rank)
#     #return HttpResponse("Hello, world!")
#     #file_name = "test.JPEG"
#     #file_name= rank
#     #image_file = 'location'
#     file_name = Image.open(+rank)
#     URL = 'http://www.w3schools.com/css/trolltunga.jpg'

#     with urllib.request.urlopen(URL) as url:
#         with open('temp.jpg', 'wb') as f:
#             f.write(url.read())

#     img = Image.open('temp.jpg')

#     image = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE) 
#     custom_config = r'--oem 1 --psm3'
#     extracted_text = pytesseract.image_to_string(image, config=custom_config)
#     #print(extracted_text)
#     words_list = extracted_text.split('\n')
#     print(words_list)
#     res = []
#     for i in words_list:
#         if i.strip() != '':
#             res.append(i)
#     print(res)
#     return HttpResponse("http://127.0.0.1:8000"+rank)

def xml(request):
    documents = Dropbox.objects.all()
    for obj in documents:
        rank = obj.document.url
        #print(rank)
    print(rank)
    file_name= rank
    #URL = 'http://www.w3schools.com/css/trolltunga.jpg'
    #img = Image.open('temp.jpg')
    URL = "http://127.0.0.1:8000"+rank

    with urllib.request.urlopen(URL) as url:
        with open('temps.jpg', 'wb') as f:
            f.write(url.read())
    file_name = "temps.jpg"
    #img = cv2.imread('sample.JPEG')
    img = cv2.imread(file_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    adaptiveThresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 12)
    config = r'--oem 1 --psm 3'
    #config = 'tesseract stdin stdout -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz0123456789 -l eng --oem 1 --psm 3'
    #pdf = pytesseract.image_to_pdf_or_hocr(adaptiveThresh, config=config, extension='pdf')
    hocr = pytesseract.image_to_pdf_or_hocr(adaptiveThresh, config=config, extension='hocr')
    #with open('test.xml',mode ='w+b') as file:
    with open('./media/xml/test.xml',mode ='w+b') as file:
        file.write(hocr)
        file.close
    return HttpResponse("Hello, world!")