import os
import requests
from googlesearch import search
import PyPDF2

def download_pdf(url, book_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{book_name}.pdf", "wb") as f:
            f.write(response.content)
        print(f"Downloaded {book_name}.pdf")
    else:
        print(f"No PDF found for {book_name}")

def read_pdf(book_name):
    with open(f"{book_name}.pdf", "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            print(f"Page {page_num+1}:\n{text}\n")

def search_and_download_books(books):
    for book in books:
        query = f"download {book} pdf"
        print(f"Searching for '{query}'...")
        search_results = search(query, num_results=5, lang='en')

        counter = 0
        for url in search_results:
            if url.endswith(".pdf"):
                download_pdf(url, book)
                read_pdf(book)
                break
            counter += 1
            if counter >= 1:
                break
        else:
            print(f"No PDF found for {book}")

if __name__ == "__main__":
    book_list = ["jungle book"]
    search_and_download_books(book_list)





    
