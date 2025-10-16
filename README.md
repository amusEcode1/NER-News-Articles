## 📰 Named Entity Recognition (NER) from News Articles
This project is a Natural Language Processing (NLP) application designed to extract and categorize named entities such as **people**, **organizations**, **locations**, et.c from news articles using spaCy.

## 🧩 Key Steps:
- Data Cleaning: Split into Train (14,041), Validation (3,250), and Test (3,453) samples.
- Entity Extraction: Identified entities like PERSON, ORG, GPE, and LOC from article content.
- **NER Approaches:**
  - Rule-based methods (using **spaCy’s Matcher** and **Span**)
  - Model-based approaches using pre-trained spaCy pipelines
- Visualization: Displayed recognized entities directly in text using **displaCy**.
- Model Comparison: Compared results using two different spaCy models:
  - **en_core_web_sm** 
  - **en_core_web_md**
- Deployment: Built a simple Streamlit app for interactive prediction.

## 📂 Dataset
Used the  CoNLL003 dataset (20,000+ samples) for Named Entity Recognition tasks.
- Available on:
  - [Kaggle - CoNLL003 Dataset](https://www.kaggle.com/datasets/alaakhaled/conll003-englishversion)
  - [Google Drive - CoNLL003 Dataset](https://drive.google.com/drive/folders/1-pXQkcKVd7_UD7Gi57v8M6ZcQHdUBOFm?usp=drive_link)

## 📊 Entity Visualization
### Displacy
![Model Comparison (SM vs MD vs Custom)](image/ner_model_comparison.png)

## 📊 Model Performance Comparison  
| Model | Validation Accuracy | Test Accuracy | Remarks |
|:---------------------------|:----------------:|:----------------:|:----------------------|
| **Custom spaCy NER (trained on CoNLL-2003)** | 0.8533 | 0.8018 | 🏆 Fine-tuned NER built from scratch |
| en_core_web_sm | — | — | Pretrained baseline for comparison |
| en_core_web_md | — | — | Pretrained baseline for comparison |

## 🧠 Tech Stack & Tools:
- Python (Pandas, spaCy, Random, DisplaCy)
- Streamlit — for model deployment and visualization
- GitHub / Google Colab / Kaggle → for collaboration and experimentation

## 📦 Dependencies
Before running this project locally, ensure the following are installed:
- Python 3.x
- Pandas
- spaCy
- Streamlit (if deploying)

## Installing
To install Streamlit:
```sh
pip install streamlit
```
To install all required dependencies:
```sh
pip install -r requirements.txt
```
Or manually:
```
pip install spacy pandas streamlit
```
Then download spaCy models:
```
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md
```

## Running the Application Locally
```sh
streamlit run app.py
```
Then open the local URL (usually http://localhost:8501/) in your browser.

## Try the App Online
You can use the app directly here: [Named Entity Extraction](https://named-entity-extraction.streamlit.app/)<br>
Simply type or paste a news article to see recognized entities highlighted in color.

## 💡 Features
- Extracts and categorizes entities (People, Organizations, Locations, et.c)
- Compares small and medium spaCy models
- Visualizes entities with displaCy
- Includes rule-based and model-based NER approaches
- Deploy an interactive app via Streamlit

## 📂 Folder Structure
```
Product-Review-Sentiment-Analysis/
├── app.py               
├── model.joblib         
├── requirements.txt     
├── image/              
│   ├── ner_model_comparison.PNG            
└── README.md          
```

## ❓ Help
If you encounter any issues:
- Check the [Streamlit Documentation](https://docs.streamlit.io/)
- Search for similar issues or solutions on [Kaggle](https://www.kaggle.com/)
- Open an issue in this repository

## ✍️ Author
👤 Oluyale Ezekiel
- Email: ezekieloluyale@gmail.com
- LinkedIn: [Ezekiel Oluyale](https://www.linkedin.com/in/ezekiel-oluyale)
- GitHub: [Product Review Sentiment Analysis](https://github.com/amusEcode1/Product_Review_Sentiment_Analysis)
- Twitter: [@amusEcode1](https://x.com/amusEcode1?t=uHxhLzrA1TShRiSMrYZQiQ&s=09)

## 🙏 Acknowledgement
Thank you, Elevvo, for the incredible opportunity and amazing Internship.
