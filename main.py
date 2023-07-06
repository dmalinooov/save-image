import requests

def save_image_from_url(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Image saved as {file_name}")
    else:
        print("Failed to download the image")

# Usage: Call the function with the URL of the image and the desired file name
save_image_from_url("https://example.com/image.jpg", "my_image.jpg")
