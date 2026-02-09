CONFIDENCE_HIGH = 0.75
CONFIDENCE_MEDIUM = 0.50

def interpret_results(vision_result):
    insights = []

    # Tags
    for tag in vision_result.get("tags", []):
        name = tag["name"]
        confidence = tag["confidence"]

        decision = classify_confidence(confidence)
        insights.append({
            "type": "tag",
            "value": name,
            "confidence": confidence,
            "decision": decision
        })

    # Objects
    for obj in vision_result.get("objects", []):
        name = obj["object"]
        confidence = obj["confidence"]

        decision = classify_confidence(confidence)
        insights.append({
            "type": "object",
            "value": name,
            "confidence": confidence,
            "decision": decision
        })

    return insights


def classify_confidence(score):
    if score >= CONFIDENCE_HIGH:
        return "High confidence – likely correct"
    elif score >= CONFIDENCE_MEDIUM:
        return "Medium confidence – needs verification"
    else:
        return "Low confidence – uncertain"

def extract_description(vision_result):
    captions = vision_result.get("description", {}).get("captions", [])
    if not captions:
        return "No description available", 0.0

    best_caption = captions[0]
    return best_caption["text"], best_caption["confidence"]