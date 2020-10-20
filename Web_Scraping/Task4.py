# Author    Daniyal Ibrahim | Telematics Engineer
# Date      20.10.2020
# Python    3.7.5
import requests
from bs4 import BeautifulSoup
import re

def get_events_as_string() -> str:

    url = "https://www.th-wildau.de/hochschule/aktuelles/veranstaltungen/"
    web_r = requests.get(url)
    soup = BeautifulSoup(web_r.text, 'html.parser')
    script_tags = soup.find_all("script", {"type": "text/javascript"})
    substring = "var calendarEvents"
    for script_tag in script_tags:
        for child in script_tag.children:
            if substring in child:
                dirty_string = str(child)
                string_tuple = dirty_string.partition("calendarEvents = ")
                return str(string_tuple[2])


def string_to_dict_list(incoming):
    myString = re.sub(r"[\[\]\t\s\'\{]*", "", incoming)
    try:
        anystring = myString.replace("title:", "").replace("start:", "").replace("end:", "").replace("overlap:", "").replace("url:", "").replace("className:", "").replace("},","\n")
        any="title"+","+"start"+","+"end"+","+"overlap"+","+"url"+","+"className"+"\n"+anystring
        with open('events.csv', 'w') as file:
            file.write(any)
            file.close()
            print("file is written")

    except:
        raise ValueError('A very specific bad thing happened.')
        raise Exception('I know Python!')


if __name__ == "__main__":
    somestring = get_events_as_string()
    if somestring is not None:
        string_to_dict_list(somestring)
