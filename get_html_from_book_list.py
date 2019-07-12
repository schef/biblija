#!/usr/bin/env python3

from urllib.request import urlopen
import re

import helper
import book_list

delimiters = ["<", ">"]
regexPattern = '|'.join(map(re.escape, delimiters))

link_pre = "https://biblija.biblija-govori.hr/glava.php?knjiga="
link_mid = "&prijevod=sve&glava="

html_path = "html/"

for e,book in enumerate(book_list.book_list):
    book_name = book[0]
    for i in range(1, book[1] + 1):
        chapter = str(i)
        print(book_name, chapter)
        link = link_pre + book_name + link_mid + chapter
        filename = html_path + "biblija_" + str(e).zfill(2) + "_" + book_name.lower() + "_" + chapter.zfill(2) + ".html"
        html = urlopen(link).read().decode('utf-8')
        helper.write_lines_to_file([html], filename)