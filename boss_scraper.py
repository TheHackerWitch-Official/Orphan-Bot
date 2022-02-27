from bs4 import BeautifulSoup as bs
import requests
import discord

def get_page(url):
    return requests.get(url)


def main():
    webpage = get_page("https://mmotimer.com/bdo/")

    if webpage.status_code != 200:
       quit() 

    print("Making soup!")
    soup = bs(webpage.content, 'html.parser')


if __name__ == '__main__':
    main()
