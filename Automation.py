import re

def extract_emails(input_file, output_file):
    # Read the content of the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Use regex to find all email addresses
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

    # Save the emails to the output file
    with open(output_file, 'w') as file:
        for email in emails:
            file.write(email + '\n')

    print(f"Extracted {len(emails)} email(s) to '{output_file}'.")

# Example usage
extract_emails('sample.txt', 'emails.txt')
