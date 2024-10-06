import pandas as pd
from openai import OpenAI

# Initialize OpenAI client (make sure your OpenAI API key is configured in your environment or pass it as an argument)
client = OpenAI()

# Read the CSV file that contains the 'Town' and 'State' columns
# Replace 'input_towns.csv' with the path to your actual CSV file
df = pd.read_csv(r'C:\Users\jcordov2\OneDrive - Norwich University\monarch_data_2023_g1.csv')

# Create a new column 'County' to store the results
df['County'] = None

# Loop through each row in the dataframe
for index, row in df.iterrows():
    town = row['Town']
    state = row['State/Province']

    # Create the prompt for the OpenAI model
    user_message = f"Answer only with the name of the county where the city of '{town}', {state}. Add nothing else."

    # Get the response from OpenAI
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    # Extract the county name from the completion response
    county_name = completion.choices[0].message.content.strip()  # Remove any leading/trailing whitespace

    # Assign the county name back to the 'County' column
    df.at[index, 'County'] = county_name

    # Print progress
    print(f"Processed {town}, {state} -> {county_name}")

# Save the updated dataframe to a new CSV file
output_filename = 'towns_with_county2023_V1_FINAL.csv'
df.to_csv(output_filename, index=False)

print(f"County names have been added and saved to {output_filename}.")



