import sys, wikipedia

filepath = sys.argv[1]
urls = open(filepath, "r").read().split("\n")[:-1]

out = open("summaries.org", "w")
err = open("err", "w")

result = list()
missing = list()

for url in urls:
    raw_title = url.split("/wiki/")[1]
    try:
        page = wikipedia.page(raw_title)
    except:
        print("Error trying to find " + raw_title)
        missing.append(url + "\n")

    title = page.title.lower()
    summ = page.summary
    summ_ = summ.lower()

    if title in summ_:
        start = summ_.find(title)
        end = start + len(title)

        new = summ[:start] + "[[" + url + "][" + summ[start:end] + "]]" + summ[end:]
        result.append(new)
        print(new)    
    
    else:
        missing.append(url + "\n")

out.writelines(result)
err.writelines(missing)
