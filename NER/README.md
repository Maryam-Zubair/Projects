# Resume Entity Extractor

This project is a Resume Entity Extractor that utilizes a customized spaCy model for extracting general entities (e.g., name, phone, email, skills) and the Mistral model specifically tailored for extracting experience details from resumes.

## Features

- Entity extraction from resumes using a customized spaCy model.
- Specific extraction of Work Experience details using the Mistral model.
- Extracted entities include name, phone, email, skills, and more.

## Getting Started

### Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x: [Download Python](https://www.python.org/downloads/)
- spaCy: Install using `pip install spacy`
- Mistral: Follow Mistral's installation instructions ([Mistral GitHub](https://github.com/JohnSnowLabs/mistral))

### Installation

1. Clone the repository:

   ```bash
   git@github.com:Maryam-Zubair/Projects.NER.git
   ```
2. Download Spacy Model:
   
```bash
  python -m spacy download en_core_web_sm
```

