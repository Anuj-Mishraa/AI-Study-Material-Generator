'''
This part of code is use to get the most relevant image for the content that is provide with the study material in this i have used 
google api of customize search engine For further details kindly go through 
https://developers.google.com/custom-search/v1/overview
Change all necessory variables like api_key and ids
'''
import requests
import json
def get_image_url(search_query, api_key, cx):
    base_url = url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}&searchType=image&num=2".format(api_key, cx, search_query)
    response = requests.get(base_url)
    if response.status_code == 200:
        try:
            data = response.json()
            if "items" in data:
                image_urls = [item["link"] for item in data.get("items", [])]
                return image_urls
            else:
                return None
        except json.JSONDecodeError:
            print("Error parsing JSON response:", response.text)
            return None
    else:
        print("API request failed with status code:", response.status_code)
        return None
# if __name__ == "__main__":
#     api_key = "customize_google_search_engine_api_key"
#     cx = "your_customize_google_search_engine_id"
#     search_query = input("Enter your search query: ")

#     image_urls = get_image_url(search_query, api_key, cx)

#     if image_urls:
#         print("Image URLs:")
#         for idx, url in enumerate(image_urls, start=1):
#             print(f"{idx}. {url}")
#     else:
#         print("No images found.")
