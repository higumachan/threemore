#coding: utf-8

import urllib2
import urllib
from xml.etree.ElementTree import *

API_URL = "http://jlp.yahooapis.jp/DAService/V1/parse"
APP_ID = "dj0zaiZpPTlvdkw3QzQxOEI5ZCZkPVlXazlObXhaYlhCdE4yRW1jR285TUEtLSZzPWNvbnN1bWVyc2VjcmV0Jng9MWQ-";

def parse_text(text):
    post_data = urllib.urlencode({"appid": APP_ID, "sentence": text});
    try:
        xml = urllib2.urlopen(API_URL, post_data).read();
    except:
        return []
    elem = fromstring(xml);
    morphems = elem.findall(".//{urn:yahoo:jp:jlp:DAService}Morphem");
    result = [];
    for morphem in morphems:
        result.append({element.tag.replace("{urn:yahoo:jp:jlp:DAService}", ""): element.text for element in list(morphem)});
    return result


if __name__ == "__main__":
    parsed_datas = parse_text(u"千石撫子かわいい".encode("utf-8"));
    print parsed_datas
    for data in parsed_datas:
        print data["Surface"]
        print data["POS"]
        if (data["POS"] in [u"名詞", u"形容詞"]):
            print "OK"
        else:
            print "NG"

