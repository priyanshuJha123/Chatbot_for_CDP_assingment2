import streamlit as st
from sentence_transformers import SentenceTransformer, util

# Load the pre-trained SentenceTransformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Function to retrieve relevant context
def retrieve_relevant_context(query, model, text_chunks, top_k=3):
    # Generate the embedding for the query
    query_embedding = model.encode([query], convert_to_tensor=True)

    # Create the embeddings for the text chunks
    text_embeddings = model.encode(text_chunks, convert_to_tensor=True)

    # Calculate cosine similarity between the query and text chunks
    scores = util.pytorch_cos_sim(query_embedding, text_embeddings)

    # Get the top-k results
    top_results = scores.topk(top_k)

    # Retrieve the corresponding text chunks
    relevant_chunks = [text_chunks[i] for i in top_results.indices[0]]
    
    return relevant_chunks

# Sample text chunks from documentation
text_chunks = [
    "To set up a new source in Segment, go to the Sources tab.",
    "You can integrate various platforms with Segment by adding a new source.",
    "First, log into Segment and click on 'Add Source' to begin the setup process.",
    "Setting up Segment involves configuring your API keys and sources.",
    "In mParticle, you can create user profiles by importing data and syncing it with other tools.",
    "To create a user profile in mParticle, click on the 'Profiles' section and fill out the necessary details.",
    "Lytics allows you to build audience segments based on various criteria and behaviors.",
    "To create an audience segment in Lytics, go to the Audience tab and select 'Create Segment'.",
    "Zeotap allows you to integrate your data with various ad platforms for targeted marketing.",
    "To integrate your data with Zeotap, navigate to the 'Integrations' section in the Zeotap dashboard."
]

# Streamlit UI elements
st.title("Priyanshu jha cdp chatbot")

st.write(
    "This is a chatbot that can help you with how-to questions related to CDPs like Segment, mParticle, Lytics, and Zeotap."
)

# Text input field for the user to ask questions
query = st.text_input("Ask your question:")

# Button to submit the question
if st.button("Submit"):
    if query:
        # Retrieve the relevant context based on the query
        relevant_context = retrieve_relevant_context(query, model, text_chunks)
        
        # Display the relevant context
        st.write("Here are the most relevant answers from the documentation:")
        for idx, context in enumerate(relevant_context, 1):
            st.write(f"{idx}. {context}")
    else:
        st.write("Please enter a question.")
