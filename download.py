import urllib.request
destination = 'название_файла.pdf'
url = 'https://drive.usercontent.google.com/uc?id=1G4x8ac-FSuuKPoZjMtIiAkT4AUwTJ_Yt&export=download'
urllib.request.urlretrieve(url, destination)