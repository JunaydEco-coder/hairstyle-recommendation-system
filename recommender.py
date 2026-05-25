def recommend_hairstyles(face_shape, hair_type):
    mapping = {
        ("Oval", "Curly"): [
            "Layered Curly Cut",
            "Side-Parted Waves",
            "Shoulder Length Curls"
        ],
        ("Round", "Straight"): [
            "Long Layers",
            "Side Bangs",
            "Straight Bob"
        ]
    }

    return mapping.get((face_shape, hair_type), ["Classic Cut"])
