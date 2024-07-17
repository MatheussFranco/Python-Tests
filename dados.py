import pandas as pd
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import tabela.py


# Load the pre-trained model and tokenizer
model_name = "bert-base-uncased"  # Change to the desired model
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Define a list of input texts
input_texts = [
    "This is the first input text.",
    "Another example text for classification.",
    "And a third input for testing.",
]

# Initialize an empty DataFrame to collect the results
results_df = pd.DataFrame(columns=["Input Text", "Predicted Label", "Score"])

# Iterate through input texts and collect results
for text in input_texts:
    # Tokenize the input text and prepare it for the model
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    
    # Make predictions using the model
    with torch.no_grad():
        outputs = model(**inputs)

    # Get the predicted label (class with highest probability)
    predicted_label = torch.argmax(outputs.logits, dim=1).item()
    predicted_score = torch.softmax(outputs.logits, dim=1).max().item()

    # Add the results to the DataFrame
    results_df = results_df.append({"Input Text": text, "Predicted Label": predicted_label, "Score": predicted_score}, ignore_index=True)

# Print the results table
print(results_df)
