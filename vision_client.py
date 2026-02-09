import requests

def analyze_image(image_path, endpoint, api_key):
    analyze_url = f"{endpoint}/vision/v3.2/analyze"

    params = {
        "visualFeatures": "Tags,Objects,Description"
    }

    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Content-Type": "application/octet-stream"
    }

    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    response = requests.post(
        analyze_url,
        headers=headers,
        params=params,
        data=image_data
    )

    response.raise_for_status()
    return response.json()
