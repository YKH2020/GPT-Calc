# This script has partial code from a real world project that parses images and video information and file names and
# creates a file structure with directories based on that information. The partial code below has several problems that would benefit from testing.
# Your task is to write unit tests for this code in test_main.py. Each problem area that you need to focus on is marked with a comment as "TODO".
import datetime


# Wrote unit tests for this function. Used the example string and come up with different variations
def whatsapp_mp4(image):
    """
    File comes in the form of VID-20190517-WA0001.mp4
    """
    parts = image.split('VID-')[-1].split('-')
    raw_date = parts[0]
    date_format = "%Y%m%d"
    return datetime.datetime.strptime(raw_date, date_format)


# Wrote unit tests for this function. Used the example string and come up with different variations
def pxl_mp4(image):
    """
    File comes in the form of PXL_20210111_184412498.mp4
    """
    parts = image.split('_')
    raw_date = parts[1]
    date_format = "%Y%m%d"
    return datetime.datetime.strptime(raw_date, date_format)


# Wrote unit tests for this function. Used the example string and come up with different variations
def whatsapp_image(image):
    """
    File comes in as IMG-20190408-WA0004.jpg
    """
    parts = image.split('IMG-')[-1].split('-')
    raw_date = parts[0]
    date_format = "%Y%m%d"
    return datetime.datetime.strptime(raw_date, date_format)


# RESOLVED: All of these if conditions could be simplified with 2 functions, one for detecting if a file ends in mp4 and another one tot detect if it is a whatsapp file
# create those functions and add tests for them.
# Finally, refactor this function to use those functions and fix the possibility of having `timestamp` undefined when the if conditions are not met.
def detect_mp4(image):
    if image.lower().endswith(".mp4"):
        if 'VID-' in image:
            return whatsapp_mp4(image)
        if 'PXL-' in image:
            return pxl_mp4(image)
        else:
            return "Some other .mp4 file"
    return None

def detect_whatsapp_file(image):
    if "-WA" in image:
        if 'IMG-' in image:
            return whatsapp_image(image)
        if 'VID-' in image:
            return whatsapp_mp4(image)
        else:
            return "Some other whatsapp file"
    return None

def main(image):
    """[SOURCE] filepath to process, defaults to stdin"""
    image = image.strip('\n')
    if detect_mp4(image): return detect_mp4(image)
    if detect_whatsapp_file(image): return detect_whatsapp_file(image)
    else: return "no timestamp could be resolved"