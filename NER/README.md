# Resume Entity Extractor

This project is a Resume Entity Extractor that utilizes a customized spaCy model for extracting general entities (e.g., name, phone, email, skills) and the Mistral model specifically tailored for extracting experience details from resumes.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Customized spaCy Model](#customized-spacy-model)
- [Mistral Model](#mistral-model)
- [Example](#example)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

- Entity extraction from resumes using a customized spaCy model.
- Specific extraction of experience details using the Mistral model.
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
   git clone https://github.com/your-username/resume-entity-extractor.git
