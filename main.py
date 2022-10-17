# import
from selenium import webdriver
import argparse

# arguments
parse = argparse.ArgumentParser()
parse.add_argument("-u")
parse.add_argument("-h")
args = parse.parse_args()

if "-h" in args:
    print("Help")
elif "-u" in args:
    print("Site: ", args.f)
    url = args.f

    browser= webdrver.Chromium()
    

else :
    print("Invalid Argument")



