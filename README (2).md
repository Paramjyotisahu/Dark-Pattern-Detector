
# Dark Pattern Detector
The Dark Pattern Detector is a Python tool designed to analyze web pages for the presence of dark patterns. Dark patterns are design choices that manipulate, deceive, or coerce users into taking actions they may not want to take. This tool helps identify such patterns using both BERT-based classification and keyword matching techniques.


## Features
1.BERT-based Dark Pattern Detection: Utilizes BERT (Bidirectional Encoder Representations from Transformers) for deep learning-based detection of dark patterns within web page text.

2.Keyword-based Detection: Employs keyword matching to identify common dark pattern indicators within web page content.

3.Real-time Alerts: Sends instant WhatsApp messages to alert users when dark patterns are detected on a website.

4.GUI Interface: Provides a user-friendly interface using Tkinter for inputting website URLs and phone numbers, and displaying analysis results.
## Installation
1. Clone the repository:
   git clone https://github.com/Paramjyotisahu/dark-pattern-detector.git

2. Install the required Python packages:
    pip install -r requirements.txt
3. Ensure you have the Chrome browser installed, as the tool utilizes Selenium WebDriver with Chrome
## Usage
1. Run the dark_pattern_detector.py script:
 python dark_pattern_detector.py
 
2. Enter the website URL and your phone number in the respective fields.
3. Click on the "Run Analysis" button to start the detection process.
4. View the analysis results in the output window. If dark patterns are detected, you will receive a WhatsApp message alert.
## Dependencies
-Python 3.x 

-Tkinter

-Beautiful Soup

-Selenium

-Transformers

-PyWhatKit