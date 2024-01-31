import argparse
import re
import pdftotext

def extract_page_data(page_content: str) -> dict:
    """use regex functions to search informations in the code and return a dict"""
    # . = search any character, * = no limit of number,
    # ? = to the next space before the word "Téléphone" (here).

    # there is one group reg (.), group(1). Without this method,
    # the regex take everything from "Raison sociale" to "Téléphone".
    ret = {
        "company": re.search("Raison sociale ou nom (.*?) Téléphone", page_content).group(1),
        "start": re.search("Date de début du contrat\) (.*?) Contrat", page_content).group(1),
        "end": re.search("fin du contrat de travail (.*?) Motif", page_content).group(1),
        "pay": re.search("TOTAL = (.*?) 5", page_content).group(1)
    }

    # 2 groups here, first for the number of hours
    # second for the numbers of days
    hours_days = re.search("Nombre de JOURS travaillés d'un accord commun (.*?) (.*?) de", page_content)
    ret["hours"] = hours_days.group(1)
    ret["days"] = hours_days.group(2)

    return ret

def extract_pdf_data(pdf_path: str) -> list[dict]:
    """parse the pdf and call the search function"""
    # physical sets to True respect the original format of the pdf
    with open(pdf_path, "rb") as f:
        pdf = pdftotext.PDF(f, physical=True)

    ret = []
    for page in pdf:
        # add a dict to the list for each page of the doc
        page_content = " ".join(page.split())
        ret.append(extract_page_data(page_content))

    return ret

def main():
    """parse the command line"""
    # arguments in this method are called if -h is called on the program
    parser = argparse.ArgumentParser(
                    prog='aem',
                    description='Extrait les données utiles des fiches AEM')

    # give a name to the first arg given (the arg given after the name of the program)
    # add_argument can take a parameter type, set on "str" by default
    parser.add_argument('aem', help="Chemin vers un fichier AEM au format PDF")

    # the command line : python aem.py /path/to/pdf
    # /path/to/aem.py /path/to/pdf (defines as 'aem')
    args = parser.parse_args()

    # call the second arg given (the path)
    data = extract_pdf_data(args.aem)
    print(data)

if __name__ == "__main__":
    main()