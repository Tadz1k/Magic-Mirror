class News:

    def check_news(self, counter):
        import requests
        from bs4 import BeautifulSoup
        url = "https://www.spidersweb.pl/kategoria/nowe-technologie"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        header = soup.findAll("span", {"class": "postlink-inner"})
        output = [header[counter], header[counter+1], header[counter+2]]
        return output

