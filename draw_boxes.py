from PIL import Image, ImageDraw, ImageFont


def get_color_by_confidence(confidence: float) -> str:
    if confidence >= 0.75:
        return "green"
    elif confidence >= 0.5:
        return "orange"
    else:
        return "red"


def draw_bounding_boxes(image_path, vision_result, output_path="output.jpg"):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Load font (Windows-safe)
    try:
        font = ImageFont.truetype("arial.ttf", size=24)
    except IOError:
        font = ImageFont.load_default()

    for obj in vision_result.get("objects", []):
        rect = obj["rectangle"]
        confidence = obj["confidence"]
        label = f"{obj['object']} ({confidence:.2f})"

        color = get_color_by_confidence(confidence)

        x, y, w, h = rect["x"], rect["y"], rect["w"], rect["h"]

        # Draw bounding box
        draw.rectangle(
            [(x, y), (x + w, y + h)],
            outline=color,
            width=3
        )

        # Measure text size
        text_bbox = draw.textbbox((0, 0), label, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Text background rectangle
        text_bg = [
            (x, max(0, y - text_height - 8)),
            (x + text_width + 8, y)
        ]
        draw.rectangle(text_bg, fill=color)

        # Draw label text
        draw.text(
            (x + 4, y - text_height - 4),
            label,
            fill="white",
            font=font
        )

    image.save(output_path)
    return output_path
