import requests

# Set the URL of the XMRIG Download Site

url = "https://github.com/xmrig/xmrig/releases/download/v6.18.1/xmrig-6.18.1-linux-x64.tar.gz"

# Send a GET request to the URL

response = requests.get(url)

# Check if the request was successful

if response.status_code == 200:

    # Save the downloaded file to a local file

    with open("xmrig-6.18.1-linux-x64.tar.gz", "wb") as file:
        file.write(response.content)
        print("Download completed successfully!")

else:
    print("Failed to download XMRIG miner. Status code:", response.status_code)