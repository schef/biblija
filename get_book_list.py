#!/usr/bin/env python

#Usage: python get_book_list.py > book_list.py

from urllib.request import urlopen
import re

delimiters = ["<", "glava.php?knjiga=", "&amp;prijevod=sve&amp;glava=", "\">"]
regexPattern = '|'.join(map(re.escape, delimiters))

html = urlopen("https://biblija.biblija-govori.hr/").readlines()
grep_line = "glava.php?knjiga"
last_book = ""
last_chapter_index = 0

string = "book_list = [" + "\n"
for line in html:
    readable_line = line.decode('utf-8')
    if grep_line in readable_line:
        splited_lines = re.split(regexPattern, readable_line)
        book = splited_lines[2]
        chapter_index = int(splited_lines[3])
        # print(readable_line.strip())
        if (last_book != book):
            if last_chapter_index != 0:
                string += "    " + "['" + last_book + "', " + str(last_chapter_index) + "]," + "\n"
            last_book = book
        last_chapter_index = chapter_index
string += "    " + "['" + last_book + "', " + str(last_chapter_index) + "]" + "\n"
string += "]" + "\n"

print(string, end="")