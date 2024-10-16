import openai

# Example: Generate a report using GPT-3

openai.api_key = 'your-api-key'

def generate_report(epidemic_data):
    prompt = f"Create a detailed report on the following epidemic data: {epidemic_data}"
    
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=500
    )
    
    report = response.choices[0].text
    return report

# Example usage
data_for_report = {
    "region": "Rural Area",
    "outbreak": "Malaria",
    "cases": 150,
    "hospital_beds_needed": 50
}

report = generate_report(data_for_report)
print(report)
