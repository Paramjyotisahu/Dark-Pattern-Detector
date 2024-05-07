import tkinter as tk
from tkinter import scrolledtext
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from transformers import BertTokenizer, BertForSequenceClassification
import pywhatkit
from datetime import datetime  # Import the datetime module

def detect_dark_pattern_bert(text):
    # BERT-related steps (unchanged)
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased')
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    outputs = model(**inputs)
    logits = outputs.logits
    predictions = logits.argmax(dim=1)

    return predictions.item()

def detect_dark_pattern_keywords(text):
    # Define dark pattern keywords with categories (unchanged)
    dark_patterns = {
        'Urgency or Scarcity': ['limited time offer', 'act now', 'only', 'hurry, ends soon'],
        'Misleading Discount Claims': ['50% off','60% off','70% off','80% off', 'exclusive discount', 'huge savings', 'special offer'],
        'Subscription Tricks': ['free trial', 'subscribe and save', 'auto-renewal'],
        'Hidden Fees or Charges': ['additional charges apply', 'service fee', 'processing fee'],
        'Tricky Opt-In/Opt-Out': ['pre-selected checkboxes', 'opt-out instead of opt-in', 'sneaky wording for consent'],
        'False Social Proof': ['fake reviews', 'fabricated testimonials', 'bogus user statistics'],
        'Difficulty in Unsubscribing': ['unsubscribe process', 'confusing cancellation policies'],
        'Bait-and-Switch': ['offering a product/service, but delivering another', 'hidden terms and conditions'],
        'Misleading Copy': ['using ambiguous language', 'fine print disclaimers'],
        'Manipulative Design Elements': ["misleading buttons", "deceptive pop-ups and notifications"]
    }

    # Iterate through dark patterns and check for keywords
    detected_patterns = []
    for category, keywords in dark_patterns.items():
        for keyword in keywords:
            if keyword.lower() in text.lower():
                detected_patterns.append(category)

    return detected_patterns

def get_website_text_and_analyze(url, phone_number):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    try:
        # ... (unchanged)
        driver.get(url)
        WebDriverWait(driver, 20).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        extracted_text = soup.get_text(separator=' ', strip=True)

        # Detect dark patterns using BERT
        bert_prediction = detect_dark_pattern_bert(extracted_text)

        # Detect dark patterns using BERT and keyword matching
        keyword_patterns = detect_dark_pattern_keywords(extracted_text)

        result_text = "BERT Prediction: {}\n".format(bert_prediction)

        if bert_prediction == 1:
            current_time = datetime.now().strftime('%H:%M')
            result_text += f"Dark pattern detected on {url} at {current_time}! Take caution\n"
            send_whatsapp_message(phone_number, f"Dark pattern detected on {url} at {current_time}! Take caution")

        result_text += "Keyword-based Dark Patterns: {}\n".format(keyword_patterns)

        if keyword_patterns:
            result_text += f"Dark patterns detected using keyword matching: {len(keyword_patterns)}\nNumber of dark patterns detected: {len(keyword_patterns)}\nDark patterns detected: {keyword_patterns}\n"
            send_whatsapp_message(phone_number, f"Dark patterns detected: {len(keyword_patterns)}\nNumber of dark patterns detected: {len(keyword_patterns)}\nDark patterns detected: {keyword_patterns}")

        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result_text)
        output_text.config(state=tk.DISABLED)

    except TimeoutException:
        print("Timed out waiting for page to load")

    finally:
        driver.quit()

def send_whatsapp_message(phone_number, message):
    # Add your country code to the phone number
    country_code = "+91"  # Change this to the appropriate country code
    phone_number_with_code = country_code + phone_number

    # Send WhatsApp message
    pywhatkit.sendwhatmsg_instantly(phone_number_with_code, message)

# Tkinter GUI (unchanged)
root = tk.Tk()
root.title("Dark Pattern Detector")

url_label = tk.Label(root, text="Enter website URL:")
url_label.pack()

url_entry = tk.Entry(root)
url_entry.pack()

phone_label = tk.Label(root, text="Enter phone number:")
phone_label.pack()

phone_entry = tk.Entry(root)
phone_entry.pack()

run_button = tk.Button(root, text="Run Analysis", command=lambda: get_website_text_and_analyze(url_entry.get(), phone_entry.get()))
run_button.pack()

output_text = scrolledtext.ScrolledText(root, width=60, height=10, wrap=tk.WORD, state=tk.DISABLED)
output_text.pack()

root.mainloop()
