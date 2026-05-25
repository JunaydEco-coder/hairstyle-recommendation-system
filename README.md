# 💇 Hairstyle Recommendation System

A machine learning-powered web application that recommends hairstyles based on a user's face shape, detected from an uploaded photo.

## ✨ Features

- **Face Shape Detection** — Automatically detects your face shape (oval, round, square, heart, oblong) from a photo
- **Personalised Recommendations** — Suggests the most flattering hairstyles for your detected face shape
- **Web Interface** — Clean, easy-to-use browser-based UI built with HTML and Python
- **Deep Learning Model** — Powered by a trained image classification model

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python (Django / Flask) |
| Frontend | HTML, CSS |
| ML Model | TensorFlow / Keras (CNN) |
| Dataset | Custom face shape image dataset |

## 📁 Project Structure

```
hairstyle-recommendation-system/
│
├── hairstyle-recommendation-system/   # Web application (views, URLs, templates)
│   └── templates/                     # HTML templates
│
├── model/                             # ML model training & prediction scripts
│   ├── train.py                       # Model training script
│   └── predict.py                     # Face shape prediction logic
│
└── README.md                          # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/JunaydEco-coder/hairstyle-recommendation-system.git
cd hairstyle-recommendation-system
```

**2. Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the application**
```bash
python manage.py runserver      # For Django
# or
python app.py                   # For Flask
```

**5. Open in your browser**
```
http://127.0.0.1:8000
```

## 🧠 How It Works

1. The user uploads a photo through the web interface
2. The image is passed to the trained CNN model in the `model/` folder
3. The model predicts the face shape (oval, round, square, heart, or oblong)
4. Based on the detected face shape, the system displays recommended hairstyles

## 📊 Face Shape Guide

| Face Shape | Recommended Hairstyles |
|---|---|
| **Oval** | Almost any style works — lucky you! |
| **Round** | Long layers, side parts, voluminous tops |
| **Square** | Soft waves, side-swept bangs, long bobs |
| **Heart** | Chin-length bobs, side-swept styles |
| **Oblong** | Waves, curls, blunt bobs with volume |

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to your fork: `git push origin feature/your-feature`
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**JunaydEco-coder**
- GitHub: [@JunaydEco-coder](https://github.com/JunaydEco-coder)

---

⭐ If you find this project helpful, please give it a star!
