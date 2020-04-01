# from django.shortcuts import HttpResponse
# from wsgiref.util import FileWrapper
# from django.http import StreamingHttpResponse
from django.http import FileResponse
from django.shortcuts import render
import json
# import zipfile
# import tempfile
# import os
# from django.shortcuts import render
# import zipstream
# import io
# Create your views here.


def file_down(request):
    if request.method == 'POST':
        json_receive = json.loads(request.body)
        id = json_receive['id']
    print("=======================================================")
    print(id)
    # name = request.POST.get('filename', None)

    #     filename = 'DrugSpaceX-Drug-set-smiles.smi.tar.gz'
    # path_to = 'E:/GitHub/'
    # filename = 'DrugSpaceX-10S.smi.tar.gz'
    filename = ''
    path_to = '/media/'
    # path = path_to + filename
    print("=======================================================")
    print(path_to)
    file = open(path_to, 'rb')
    print(file)
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename='+filename
    return response
    # return render(response, '/streams/card_block.html', {'file': file})


# def DownLoadApiView(request):
#     filename = open('media/3D.txt', 'rb')
#     response = HttpResponse(filename)
#     response['Content-Type'] = 'application/octet-stream'
#     response['Content-Disposition'] = 'attachment;filename="3D.txt"'
#     return response


# class ZipUtilities:
#     zip_file = None

#     def __init__(self):
#         self.zip_file = zipstream.ZipFile(
#             mode='w', compression=zipstream.ZIP_DEFLATED)

#     def toZip(self, file, name):
#         if os.path.isfile(file):
#             self.zip_file.write(file, arcname=os.path.basename(file))
#         else:
#             self.addFolderToZip(file, name)

#     def addFolderToZip(self, folder, name):
#         for file in os.listdir(folder):
#             full_path = os.path.join(folder, file)
#             if os.path.isfile(full_path):
#                 self.zip_file.write(full_path, arcname=os.path.join(
#                     name, os.path.basename(full_path)))
#             elif os.path.isdir(full_path):
#                 self.addFolderToZip(full_path, os.path.join(
#                     name, os.path.basename(full_path)))

#     def close(self):
#         if self.zip_file:
#             self.zip_file.close()


# def zip_download(request):
#     utilities = ZipUtilities()
#     filename = "yasuo.zip"
#     path_to = "media/"
#     tmp_dl_path = os.path.join(path_to, filename)
#     utilities.toZip(tmp_dl_path, filename)
#     # utilities.close()
#     response = StreamingHttpResponse(
#         utilities.zip_file, content_type='application/zip')
#     response['Content-Disposition'] = 'attachment;filename="{0}"'.format(
#         "yasuo.zip")
#     return response
