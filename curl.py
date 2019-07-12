#!/usr/bin/env python3

from urllib.request import urlopen
import re

delimiters = ["<", ">"]
regexPattern = '|'.join(map(re.escape, delimiters))


class bcolors:
    ENDC = '\033[0m'
    CBOLD = '\33[1m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    CBLINK = '\33[5m'
    CBLINK2 = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

    CBLACKBG = '\33[40m'
    CREDBG = '\33[41m'
    CGREENBG = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG = '\33[46m'
    CWHITEBG = '\33[47m'

    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'


def read_lines_from_file(filename):
    lines = []
    with open('./' + filename, 'r') as f:
        lines = f.readlines()
    return lines


def write_lines_to_file(lines, filename):
    print("write_lines_to_file " + filename)
    with open('./' + filename, 'w') as f:
        f.write("".join(lines))


link_pre = "https://biblija.biblija-govori.hr/glava.php?knjiga="
link_mid = "&prijevod=sve&glava="

books = [
    ['Postanak', 50],
    ['Izlazak', 40],
    ['Levitski%20zakonik', 27],
    ['Brojevi', 36],
    ['Ponovljeni%20zakon', 34],
    ['Jo%C5%A1ua', 24],
    ['Suci', 21],
    ['Ruta', 4],
    ['1.%20Samuelova', 31],
    ['2.%20Samuelova', 24],
    ['1.%20Kraljevima', 22],
    ['2.%20Kraljevima', 25],
    ['1.%20Ljetopisa', 29],
    ['2.%20Ljetopisa', 36],
    ['Ezra', 10],
    ['Nehemija', 13],
    ['Estera', 10],
    ['Job', 42],
    ['Psalam', 150],
    ['Mudre%20izreke', 31],
    ['Propovjednik', 12],
    ['Pjesma%20nad%20pjesmama', 8],
    ['Izaija', 66],
    ['Jeremija', 52],
    ['Tu%C5%BEaljke', 5],
    ['Ezekiel', 48],
    ['Daniel', 12],
    ['Ho%C5%A1ea', 14],
    ['Joel', 4],
    ['Amos', 9],
    ['Obadija', 1],
    ['Jona', 4],
    ['Mihej', 7],
    ['Nahum', 3],
    ['Habakuk', 3],
    ['Sefanija', 3],
    ['Hagaj', 2],
    ['Zaharija', 14],
    ['Malahija', 4],
    ['Matej', 28],
    ['Marko', 16],
    ['Luka', 24],
    ['Ivan', 21],
    ['Djela%20apostolska', 28],
    ['Rimljanima', 16],
    ['1.%20Korin%C4%87anima', 16],
    ['2.%20Korin%C4%87anima', 13],
    ['Gala%C4%87anima', 6],
    ['Efe%C5%BEanima', 6],
    ['Filipljanima', 4],
    ['Kolo%C5%A1anima', 4],
    ['1.%20Solunjanima', 5],
    ['2.%20Solunjanima', 3],
    ['1.%20Timoteju', 6],
    ['2.%20Timoteju', 4],
    ['Titu', 3],
    ['Filemonu', 1],
    ['Hebrejima', 13],
    ['Jakovljeva', 5],
    ['1.%20Petrova', 5],
    ['2.%20Petrova', 3],
    ['1.%20Ivanova', 5],
    ['2.%20Ivanova', 1],
    ['3.%20Ivanova', 1],
    ['Judina', 1],
    ['Otkrivenje', 22]
]

grep_line = "tr class='stih"

stih = "<tr class='stih1'><td><a name='1'></a><a href='glava.php?prijevod=sve&knjiga=Postanak&glava=1#1'>Postanak 1,1</a></td><td>U početku stvori Bog nebo i zemlju.</tr>"

transcripts = [
    [],
    [],
    [],
    []
]

transcripts_lists = [
    [],
    [],
    [],
    []
]

ignore_chapter_change = ['Izlazak 12,30', 'Izlazak 38,29', 'Izlazak 38,25', 'Brojevi 24,52', 'Brojevi 24,9', 'Deuteronom 11,7']

for book in books:
    book_name = book[0]
    for i in range(1, book[1] + 1):
        in_book = 0
        last_verse_index = 1
        chapter = str(i)
        print(book_name, chapter)
        link = link_pre + book_name + link_mid + chapter
        html_lines = urlopen(link).readlines()
        for line in html_lines:
            readable_line = line.decode('utf-8')
            if (grep_line in readable_line):
                splited_line = re.split(regexPattern, readable_line)
                verse_index = int(splited_line[5].split("'")[1])
                chapter = splited_line[10]
                verse = splited_line[16]
                if (verse_index < last_verse_index and verse_index == 1):
                    in_book += 1
                last_verse_index = verse_index

                print("in book", in_book, readable_line)
                transcripts[in_book].append([chapter, verse])

transcripts_lists[0].append("ivan_saric = [" + "\n")
for i in transcripts[0]:
    transcripts_lists[0].append("['" + i[0] + "', '" + i[1] + "']," + "\n")
transcripts_lists[0].append("]" + "\n")
file_name = "biblija_" + "ivan_saric" + ".py"
write_lines_to_file(transcripts_lists[0], file_name)

transcripts_lists[1].append("jeruzalemska_biblija = [" + "\n")
for i in transcripts[1]:
    transcripts_lists[1].append("['" + i[0] + "', '" + i[1] + "']," + "\n")
transcripts_lists[1].append("]" + "\n")
file_name = "biblija_" + "jeruzalemska_biblija" + ".py"
write_lines_to_file(transcripts_lists[1], file_name)

transcripts_lists[2].append("tomislav_dretar = [" + "\n")
for i in transcripts[2]:
    transcripts_lists[2].append("['" + i[0] + "', '" + i[1] + "']," + "\n")
transcripts_lists[2].append("]" + "\n")
file_name = "biblija_" + "tomislav_dretar" + ".py"
write_lines_to_file(transcripts_lists[2], file_name)

transcripts_lists[3].append("danicic_karadzic = [" + "\n")
for i in transcripts[3]:
    transcripts_lists[3].append("['" + i[0] + "', '" + i[1] + "']," + "\n")
transcripts_lists[3].append("]" + "\n")
file_name = "biblija_" + "danicic_karadzic" + ".py"
write_lines_to_file(transcripts_lists[3], file_name)
