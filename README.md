# Chatbot_for_CDP_assingment2
# **CDP Chatbot**

## **Overview**
The **CDP Chatbot** is an interactive web application designed to assist users in finding relevant answers to "how-to" questions related to Customer Data Platforms (CDPs) such as **Segment**, **mParticle**, **Lytics**, and **Zeotap**. The chatbot utilizes a **pre-trained SentenceTransformer model** to deliver contextually relevant information based on user queries.

---

## **Key Features**
- **User Query Processing**: Accepts natural language questions from users and retrieves relevant answers.
- **Pre-trained NLP Model**: Utilizes the `paraphrase-MiniLM-L6-v2` model for semantic search.
- **Streamlit Integration**: Offers a simple and interactive user interface for querying and displaying results.
- **Documentation Insights**: Extracts and presents the most relevant pieces of documentation for user queries.

---

## **Key Technologies**
- **Streamlit**: Powers the user interface, allowing for interactive text input and result display.
- **SentenceTransformers**: Provides state-of-the-art embeddings for semantic similarity tasks.
- **PyTorch**: Used internally by SentenceTransformers for efficient similarity computations.
- **Python**: The core programming language for logic and implementation.

---

## **Streamlit Usage**
- **Text Input Field**: Allows users to input their queries.
- **Submit Button**: Triggers the query processing and retrieves results.
- **Results Display**: Lists the most relevant documentation snippets in an easy-to-read format.
- **Interactive UI**: Streamlit simplifies deploying and testing the chatbot with minimal configuration.

---

## **How It Works**
1. **Input Query**: Users type a natural language question in the provided input field.
2. **Query Encoding**: The chatbot encodes the query using the `SentenceTransformer` model.
3. **Similarity Computation**: Computes cosine similarity between the query and predefined documentation snippets.
4. **Result Display**: Shows the top three most relevant results ranked by similarity score.

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.8 or later installed on your machine.
- Basic familiarity with Python and Streamlit.

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cdp-chatbot.git
   cd cdp-chatbot
   streamlit run app.py

