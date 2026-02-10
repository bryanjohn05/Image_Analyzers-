import requests
import os


def analyze_image(image_input, endpoint, api_key):
    analyze_url = f"{endpoint}/vision/v3.2/analyze"

    params = {
        "visualFeatures": "Tags,Objects,Description"
    }

    headers = {
        "Ocp-Apim-Subscription-Key": api_key
    }

    # 🌐 Case 1: Image URL
    if image_input.startswith("http://") or image_input.startswith("https://"):
        headers["Content-Type"] = "application/json"
        data = {"url": image_input}

        response = requests.post(
            analyze_url,
            headers=headers,
            params=params,
            json=data
        )

    # 📂 Case 2: Local image file
    else:
        if not os.path.exists(image_input):
            raise FileNotFoundError(f"Image not found: {image_input}")

        headers["Content-Type"] = "application/octet-stream"

        with open(image_input, "rb") as image_file:
            image_data = image_file.read()

        response = requests.post(
            analyze_url,
            headers=headers,
            params=params,
            data=image_data
        )

    response.raise_for_status()
    return response.json()
