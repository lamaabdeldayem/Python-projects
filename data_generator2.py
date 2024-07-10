import simple_image_download.simple_image_download as simp
import os
my_downloader = simp.Downloader()
my_downloader.extensions = '.jpg'
my_downloader.download('real+dog',limit=5, verbose=True)
my_downloader.directory = os.path.join('.','images')
