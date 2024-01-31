import pdftotext

with open("test-aem-jules.pdf", "rb") as f:
    pdf = pdftotext.PDF(f, physical = True)

# for page in pdf:
#     print(page)

with open("text_extracted.txt", "w", encoding = "utf-8") as f:
    for page in pdf:
        f.write(page)