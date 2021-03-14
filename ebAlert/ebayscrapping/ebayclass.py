import requests
from ebAlert import create_logger

log = create_logger(__name__)

try:
    from bs4 import BeautifulSoup
except ImportError:
    log.error('bs4 must be installed.\npip install bs4')


class EbayItem:
    """Class ebay item"""
    def __init__(self, contents):
        self.contents = [con for con in contents if con != "\n"][0]
        self.link = "https://www.ebay-kleinanzeigen.de" + self.contents.a['href']
        self.title = self.contents.a.text
        for div in self.contents.findAll("p"):
            if div.attrs.get("class"):
                if "price" in div.attrs["class"][0]:
                    self.price = div.text.strip()
                elif "description" in div.attrs["class"][0]:
                    self.description = div.text.replace("\n", " ")
        self.id = self.contents['data-adid']
        details = self.get_details()
        self.distance = details["distance"]
        self.city = details["city"]

    def __repr__(self):
        return '{}; {}; {}'.format(self.title, self.city, self.distance)


    def get_details(self):
        details = self.contents.find_all("div", {'class': "aditem-main--top--left"})[0].text.split("\n")
        details = [det.strip() for det in details]
        return {"distance": details[-1], "city": details[-2]}


def get_post(link):
    session = requests.Session()
    custom_header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}
    response = session.get('{}'.format(link),
                           headers=custom_header)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find(attrs={"id": "srchrslt-adtable"})
        if result:
            articles = result.find_all(attrs={"class": "ad-listitem lazyload-item"})
            items = [EbayItem(item) for item in articles]
            return items

