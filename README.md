# 🧠 Image Analyser App (Azure Vision API)

An end-to-end **Image Analysis Application** built using **Python** and **Azure Computer Vision (Vision API)**.

This project demonstrates how real-world AI systems:

* Handle **binary image data**
* Parse **complex JSON responses**
* Make **probabilistic decisions** using confidence scores
* Explicitly handle **uncertainty in AI predictions**

The application supports both:

* **Command-line (CLI) execution**
* **Interactive Streamlit UI**

---

## 🚀 Features

* 📤 Dynamic image input (CLI argument or file upload)
* 🧾 Natural language image description with confidence score
* 🎯 Object detection with bounding boxes
* 🎨 Confidence-based color coding:

  * 🟢 Green – High confidence (≥ 0.75)
  * 🟠 Orange – Medium confidence (0.50 – 0.74)
  * 🔴 Red – Low confidence (< 0.50)
* 📊 Probabilistic insights (not binary decisions)
* ⚠️ Explicit uncertainty handling
* 🔐 Secure configuration using `.env`

---

## 🛠️ Tech Stack

* Python 3.10+
* Azure Computer Vision (Vision API)
* Streamlit (UI)
* Pillow (image processing)
* Requests (HTTP API calls)
* python-dotenv (environment variables)

---

## 📁 Project Structure

```
image_analyser/
│
├── app.py                 # Streamlit UI
├── main.py                # CLI entry point
├── vision_client.py       # Azure Vision API client
├── decision_engine.py     # Probabilistic logic & parsing
├── draw_boxes.py          # Bounding box visualization
├── config.py              # Environment configuration
├── requirements.txt
├── .env                   # Azure credentials (not committed)
└── sample_images/
    └── test.jpg
```

---

## 🔐 Environment Setup

Create a `.env` file in the project root:

```
AZURE_VISION_ENDPOINT=https://<your-resource-name>.cognitiveservices.azure.com
AZURE_VISION_KEY=<your-api-key>
```

> ⚠️ Do NOT commit the `.env` file to version control.

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### 1️⃣ Command Line Interface (CLI)

```bash
python main.py sample_images/test.jpg
```

Or run interactively:

```bash
python main.py
```

You will be prompted to enter an image path.

---

### 2️⃣ Streamlit UI

```bash
streamlit run app.py
```

Then open the browser link shown in the terminal.

---

## 🖼️ Output

* Annotated image saved as:

  ```
  output.jpg / output_streamlit.jpg
  ```
* Bounding boxes drawn around detected objects
* Labels include object name + confidence score
* Colors indicate certainty level

---

## 🧪 Probabilistic Decision Logic

The system **does not treat AI predictions as facts**.

Confidence thresholds:

| Confidence | Interpretation                         |
| ---------- | -------------------------------------- |
| ≥ 0.75     | High confidence – likely correct       |
| 0.50–0.74  | Medium confidence – needs verification |
| < 0.50     | Low confidence – uncertain             |

Low-confidence predictions are clearly flagged instead of hidden.

---

## ⚠️ Uncertainty Handling (Responsible AI)

* No hard yes/no decisions
* Visual uncertainty via color coding
* Explicit messaging that AI can be wrong
* Human-in-the-loop friendly design

---

## 🧠 Academic Justification

This project demonstrates:

* **Binary data handling** via raw image byte transmission
* **JSON parsing** of nested AI responses
* **Probabilistic reasoning** using confidence scores
* **Uncertainty-aware system design**

> AI outputs are probabilistic, not absolute.

---

