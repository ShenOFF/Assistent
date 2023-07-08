import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')

try:
    page_py = wiki_wiki.page("TypeScript")
    if page_py.exists():
        typescript_data = page_py.text
        print(typescript_data)
    else:
        print("Page not found")
except Exception as e:
    print("An error occurred:", str(e))
