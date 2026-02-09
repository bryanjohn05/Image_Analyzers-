import sys
from vision_client import analyze_image
from config import AZURE_ENDPOINT, AZURE_KEY
from decision_engine import interpret_results, extract_description
from draw_boxes import draw_bounding_boxes



def main():
    if len(sys.argv) < 2:
        image_path = input("📂 Enter image path: ").strip()
    else:
        image_path = sys.argv[1]



    print(f"🖼️ Analyzing image: {image_path}")
    vision_result = analyze_image(image_path, AZURE_ENDPOINT, AZURE_KEY)

    insights = interpret_results(vision_result)

    description, desc_confidence = extract_description(vision_result)

    output_image = draw_bounding_boxes(image_path, vision_result)
    print(f"\n📦 Output image saved with detections: {output_image}")

    print("\n===== IMAGE DESCRIPTION =====")
    print(f"📝 {description}")
    print(f"Confidence: {desc_confidence:.2f}")

    print("\n===== PROBABILISTIC INSIGHTS =====\n")
    for item in insights:
        print(
            f"{item['type'].upper():7} | "
            f"{item['value']:<15} | "
            f"Confidence: {item['confidence']:.2f} | "
            f"{item['decision']}"
        )

    print("\n⚠️ AI outputs are probabilistic, not absolute.")

if __name__ == "__main__":
    main()
