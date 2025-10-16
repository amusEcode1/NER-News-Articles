import streamlit as st
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy.language import Language
from spacy import displacy

# Streamlit Page Config
st.set_page_config(page_title="NER Visualizer", page_icon="📰", layout="wide")
st.title("📰 Named Entity Recognition (NER) from News Articles")

# Model Selection
model_choice = st.selectbox(
    "Select a model:",
    ["Small Model (with Rules)", "Medium Model (from SpaCy)", "Custom Trained Model"]
)

# Rule-Based Matcher Setup
def create_rule_based_matcher(nlp_sm):
    matcher = Matcher(nlp_sm.vocab)

    # Money patterns
    money_patterns = [
        [{'TEXT': {'REGEX': '^\$'}}, {'LIKE_NUM': True}],
        [{'LOWER': {'IN': ['usd', 'eur', 'gbp']}}, {'LIKE_NUM': True}],
    ]

    # Date pattern
    date_pattern = [
        {'SHAPE': 'dddd'},
        {'TEXT': '-'},
        {'SHAPE': 'dd'},
        {'TEXT': '-'},
        {'SHAPE': 'dd'}
    ]

    # Time patterns
    time_patterns = [
        [{'SHAPE': 'dd'}, {'TEXT': ':'}, {'SHAPE': 'dd'}],
        [{'SHAPE': 'd'}, {'TEXT': ':'}, {'SHAPE': 'dd'}, {'LOWER': {'IN': ['am', 'pm']}}],
        [{'SHAPE': 'dd'}, {'TEXT': ':'}, {'SHAPE': 'dd'}, {'LOWER': {'IN': ['am', 'pm']}}],
        [{'SHAPE': 'dd'}, {'TEXT': 'h'}, {'SHAPE': 'dd'}]
    ]

    # Company patterns
    company_patterns = [
        [{'IS_TITLE': True, 'OP': '+'}, {'LOWER': {'IN': ['inc', 'inc.', 'ltd', 'ltd.', 'corp', 'corp.', 'plc', 'llc', 'gmbh', 's.a.', 'co.']}}],
        [{'LOWER': {'IN': ['company', 'corporation', 'enterprise', 'group']}}],
        [{'IS_TITLE': True, 'OP': '+'}, {'LOWER': 'company'}]
    ]

    # Add patterns to matcher
    matcher.add('MONEY', money_patterns)
    matcher.add('DATE', [date_pattern])
    matcher.add('TIME', time_patterns)
    matcher.add('ORG', [[{'LOWER': 'ngos'}]])
    matcher.add('MISC', [[{'LOWER': 'governments'}]])
    matcher.add('ORG', company_patterns)

    return matcher

# Load small model for rules
nlp_sm = spacy.load("en_core_web_sm")
matcher = create_rule_based_matcher(nlp_sm)

@Language.component("rule_based_ner")
def rule_based_ner(doc):
    matches = matcher(doc)
    spans = []
    for match_id, start, end in matches:
        label = nlp_sm.vocab.strings[match_id]
        spans.append(Span(doc, start, end, label=label))
    all_spans = list(doc.ents) + spans
    all_spans = spacy.util.filter_spans(all_spans)
    doc.ents = all_spans
    return doc

# Load Models
@st.cache_resource
def load_model(choice):
    if choice == "Small Model (with Rules)":
        # Load your saved rule-based model
        nlp = spacy.load("rule_based_ner_sm.zip")
        return nlp
    elif choice == "Medium Model (from SpaCy)":
        return spacy.load("en_core_web_md")
    else:
        # Load custom trained model
        return spacy.load("ner_conll_model.zip")

nlp = load_model(model_choice)
st.success(f"✅ Loaded: {model_choice}")

# Text Input
text = st.text_area(
    "Enter text for NER:",
    "Apple plans to open a new office in Nigeria by 2026."
)

# Analyze Button
if st.button("Analyze"):
    if not text.strip():
        st.warning("Please enter some text")
    else:
        doc = nlp(text)

        # Render entities visually
        html = displacy.render(doc, style="ent", page=False)
        st.markdown(html, unsafe_allow_html=True)

        # Optional: show entities in table
        if doc.ents:
            entities = [{"Text": ent.text, "Label": ent.label_} for ent in doc.ents]
            st.table(entities)
        else:
            st.info("No entities found.")
