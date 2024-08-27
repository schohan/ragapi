import requests


class URLFetcher:
    def download_and_save_document(self, url, save_location, save_file_name):
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_location + save_file_name, 'wb') as file:
                file.write(response.content)
                print("Document saved successfully.")
        else:
            print(f"Failed to download document. Code={response.status_code}. Error={response.raise_for_status()}")

    
if __name__ == "__main__":
    url_fetcher = URLFetcher()
    url = "https://docs.google.com/document/d/1AY4YqV6FHxpFvuZ_1HldYxWf1w0FfB1jGi9kBCLcaBk"
    save_location = "/Users/shailenderchohan/projects/ragapi/data/out/"
    url_fetcher.download_and_save_document(url, save_location, "kit2.docx")
