# pyinstaller --add-data "BlankForm/NY IRP_Schedule B.pdf:BlankForm" -F -w app.py -n 妙妙工具

import sys
from operator import index

import pdfplumber
from pypdf import PdfReader, PdfWriter
from pypdf.generic import TextStringObject
import os

BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

if getattr(sys, 'frozen', False):
    BASE_DIR = getattr(sys, '_MEIPASS', None)

usa_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
    "New Hampshire", "New Jersey", "New Mexico", "New York",
    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
    "West Virginia", "Wisconsin", "Wyoming"
]
us_states = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY"
}

def get_Company_Info(filename: str):
    pdf = pdfplumber.open(filename)
    cover_page = pdf.pages[0].extract_text()
    company_name = cover_page[cover_page.index("Address: ") + len("Address: "):cover_page.index(" jurisdiction")]
    president = cover_page[cover_page.index("Submitted by:") + len("Submitted by: "):]
    pdf.close()

    return [company_name,president]

def extract_table(filename: str, result: dict):
    pdf = pdfplumber.open(filename)
    total = 0
    for page in range(1, len(pdf.pages)):
        table = pdf.pages[page].extract_table()
        for row in range(0, len(table)):
            state = table[row][0]
            if state in usa_states:
                state = "ACTUAL DISTANCE" + us_states[state] + " " + state
                if state not in result.keys():
                    result[state] = 0
                mile = int((table[row + 1][1]).replace(',', ''))
                # print(state + ": " + str(mile))
                result[state] += mile
                total += mile
    pdf.close()
    return result,total

def statistics_ifta(filenames: list,textBrowser = None):
    result = {}
    output_text = ""
    company_info = get_Company_Info(filenames[0])
    for filename in filenames:
        result,t = extract_table(filename, result)
        if textBrowser:
            output_text = output_text + "Total mile of " + filename +": " + str(t) + "\n"

    total = 0
    for key, value in result.items():
        total += value

    if textBrowser:
        output_text = output_text + "total: "+ str(total)+ "\n"
        textBrowser.setText(output_text)

    fill_form(result,company_info)


def fill_form(dict: dict,info):
    basefile = os.path.join(BASE_DIR,"BlankForm/NY IRP_Schedule B.pdf")
    reader = PdfReader(open(basefile, "rb"), strict=False)
    writer = PdfWriter(clone_from=reader)
    writer.set_need_appearances_writer(True)

    # print(writer.get_fields())

    fields = {"35 CARRIER":info[0],
              'Name of RegistrantCarrier please print':info[1]}

    for key, value in dict.items():
        fields[(key)] = TextStringObject(value)

    writer.update_page_form_field_values(
        writer.pages[0], fields
    )

    output_path = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), info[0]+"-IFTA filled out.pdf")

    with open(output_path, "wb") as output_stream:
        writer.write(output_stream)


if __name__ == '__main__':
    statistics_ifta(['Q3 2023.pdf', 'Q4 2023.pdf', 'Q1 2024.pdf', 'Q2 2024.pdf'])
