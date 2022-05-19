
import requests
import sys
import dewiki


def req_wiki():
    if len(sys.argv) != 2:
        print("Something wrong")
    else:
        param = sys.argv[1]
        s = requests.Session()

        url = 'https://en.wikipedia.org/w/api.php'

        params = {
            "action": "parse",
            "page": param,
            "prop": "wikitext",
            "format": "json",
            "redirects": True,
            "formatversion": 2
        }

        r = s.get(url=url, params=params)
        data = r.json()
        result = dewiki.from_string(data['parse']['wikitext'])
        result = result.replace("\n\n", "\n")

        file = open(param + ".wiki", "w")
        file.write(result)
        file.close()


if __name__ == '__main__':
    req_wiki()