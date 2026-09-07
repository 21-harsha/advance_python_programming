import re

def find_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    matches = re.findall(pattern, text)
    
    return matches

if __name__ == "__main__":
    text = input("Enter text: ")
    result = find_emails(text)
    print("Email addresses:", result)