import re, sys, wikipedia
import urllib.parse

filepath = sys.argv[1]
urls = open(filepath, "r").read().split("\n")[:-1]

out = open("summaries.org", "w")
err = open("err", "w")

result = list()
missing = list()

for url in urls:
    url = urllib.parse.unquote(url)
    raw_title = url.split("/wiki/")[1]
    raw_title = raw_title.replace("_", " ")

    try:
        page = wikipedia.page(raw_title)
    except:
        print("Error trying to find " + raw_title)
        missing.append(url + "\n")
        continue

    title = page.title.lower()
    plain_title = re.sub("[\(\[].*?[\)\]]", "", title)
    summ = page.summary
    summ_ = summ.lower()

    if plain_title in summ_:
        start = summ_.find(title)
        end = start + len(title)

        new = summ[:start] + "[[" + url + "][" + summ[start:end] + "]]" + summ[end:] + "\n"
        result.append(new)
    
    else:
        new = "[[" + url + "][" + summ + "]]\n"
        result.append(new)

    print("Added " + title)

# TODO: make this a web server

out.writelines(result)
err.writelines(missing)
