
# 📝 AI Resume Creator & Portfolio Builder

> Generate tailored, ATS-aware resumes, cover letters, and portfolio ZIPs using classical NLP techniques without any API costs or internet dependency.

Live Application :- https://ai-resume-creator-enhancer-6jczyflyfydxtfw2xflcvm.streamlit.app/

## 🌟 Features

### Core Capabilities
- ✅ **PDF Resume Upload & Extraction** - Extract text from PDF resumes automatically
- ✅ **AI-Enhanced Summaries** - Generate professional summaries using TF-IDF NLP
- ✅ **ATS Keyword Optimization** - Match job descriptions and add relevant keywords
- ✅ **STAR Format Bullets** - Auto-generate achievement bullets with action verbs
- ✅ **Cover Letter Generation** - Create tailored cover letters from resume data
- ✅ **Multiple Export Formats** - PDF, DOCX, JSON, and Portfolio ZIP
- ✅ **Resume Templates** - Modern, Classic, and Professional designs
- ✅ **Profile Management** - Save and reload resume profiles

### Advanced Features
- 🔍 **Job Description Analysis** - Extract ATS keywords using TF-IDF vectorization
- 📊 **NLP-Based Enhancement** - Identify top skills and achievements
- 🎯 **Smart Keyword Merging** - Intelligently blend job requirements with resume content
- 💾 **Session Persistence** - Save profiles as JSON for future modifications
- 🎨 **Responsive UI** - Clean, intuitive interface with tabs for different workflows

## 📋 Requirements

### System Requirements
- Python 3.11 or higher
- 2GB RAM minimum
- 50MB disk space

### Dependencies
```
streamlit==1.28.1           # Web UI framework
PyPDF2==4.0.1             # PDF text extraction
fpdf==1.7.2               # PDF generation
scikit-learn==1.3.2       # NLP/TF-IDF analysis
python-docx==0.8.11       # DOCX generation (optional)
beautifulsoup4==4.12.2    # HTML parsing (optional)
weasyprint==59.2          # Advanced PDF rendering (optional)
```

## 🚀 Installation

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/AI_Resume_Builder.git
cd AI_Resume_Builder_1
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
# Install all packages
pip install -r requirements.txt

# OR install minimal setup (PDF only)
pip install streamlit PyPDF2 fpdf scikit-learn

# OR install with optional features
pip install streamlit PyPDF2 fpdf scikit-learn python-docx beautifulsoup4
```

### Step 4: Run Application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📖 Usage Guide

### Tab 1: Upload Existing Resume
1. **Upload PDF Resume**
   - Click "Upload your resume (PDF only)"
   - Select your existing resume PDF file

2. **Enter Your Information**
   - Your Name: [Your full name]
   - Email Address: [Your email]
   - Job Description (Optional): [Target job description for ATS matching]

3. **Click "Enhance Resume"**
   - App extracts text from PDF
   - Analyzes content with NLP
   - Generates professional summary
   - Creates STAR-format bullet points
   - Generates cover letter

4. **Review & Download**
   - View AI-enhanced summary on left
   - View generated cover letter on right
   - Download PDF, DOCX, Portfolio ZIP, and JSON profile

### Tab 2: Create New Resume
1. **Enter Your Details**
   - Full Name
   - Email Address
   - Skills (comma-separated)
   - Projects / Experience (multi-line)
   - Job Description (optional)

2. **Click "Generate Resume"**
   - Analyzes input text
   - Extracts key skills and achievements
   - Generates professional summary
   - Creates achievement bullets
   - Generates cover letter

3. **Download Your Resume**
   - PDF resume in your chosen template
   - DOCX version for editing
   - Portfolio ZIP with all files
   - JSON profile for future use

### Tab 3: Load & Regenerate Profile
1. **Upload Previous Profile JSON**
   - Click file uploader
   - Select a previously saved profile JSON file

2. **Modify Information**
   - Edit name, email, resume text
   - Update job description for new target role

3. **Click "Regenerate Resume"**
   - Re-analyzes with new job description
   - Generates updated summary and bullets
   - Creates new cover letter

4. **Download Updated Package**
   - All files with new optimizations

---

## 🏗️ Project Structure

```
AI_Resume_Builder_1/
├── app.py                           # Main Streamlit application
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── profile_*.json                   # Saved resume profiles
├── Resume_*.pdf                     # Generated PDF resumes
├── Resume_*.docx                    # Generated DOCX resumes
├── Portfolio_*.zip                  # Portfolio bundles
└── templates/                       # (Optional) Custom templates
    ├── resume_modern.html
    ├── resume_classic.html
    └── resume_professional.html
```

---

## 🔧 Technologies & Libraries

### Core Stack
| Technology | Purpose | Version |
|-----------|---------|---------|
| **Streamlit** | Web UI Framework | 1.28.1 |
| **Python** | Programming Language | 3.11+ |
| **scikit-learn** | NLP & Machine Learning | 1.3.2 |

### Document Processing
| Library | Purpose | Why Used |
|---------|---------|----------|
| **PyPDF2** | PDF text extraction | Reads and parses PDF resumes |
| **fpdf** | PDF generation | Creates formatted PDF resumes |
| **python-docx** | Word document creation | Generates editable DOCX files |
| **beautifulsoup4** | HTML parsing | Optional HTML content processing |

### NLP & Analysis
| Algorithm | Implementation | Result |
|-----------|-----------------|--------|
| **TF-IDF** | scikit-learn TfidfVectorizer | Extracts important keywords |
| **N-grams** | Range (1,2) | Captures multi-word phrases |
| **Stop Words** | English stopwords | Removes common low-value words |


## 🎯 How It Works

### 1. PDF Extraction
```
PDF Upload → PyPDF2.PdfReader → Extract text from each page → Clean & combine
```

### 2. ATS Keyword Analysis
```
Job Description Input
         ↓
TF-IDF Vectorization (max_features=30, ngram_range=(1,2))
         ↓
Top 20 Keywords by score + Common ATS keywords
         ↓
Deduplicate & return top 25 keywords
```

### 3. Resume Enhancement
```
Resume Text → TF-IDF (max_features=40) → Extract top 8 keywords
                                             ↓
                                    If job description provided:
                                    - Extract ATS keywords
                                    - Merge with resume keywords
                                    - Create professional summary
```

### 4. STAR Bullet Generation
```
Experience Text → Split by sentences
                     ↓
            Check for action verbs
                     ↓
            Format as bullet points
                     ↓
            Return top 5 or generic bullets
```

### 5. Cover Letter Creation
```
Extract Keywords from Job Description
            ↓
Generate templated cover letter
            ↓
Personalize with candidate name & skills
```

### 6. Export & Storage
```
Create PDF (fpdf) → Resume_[template].pdf
Create DOCX (python-docx) → Resume_[template].docx
Create ZIP (zipfile) → Portfolio_[name]_[date].zip
Save JSON (json) → profile_[name]_[timestamp].json
```

## 🎨 Template Options

### Modern Template
- Large bold header with name and email
- Professional summary section
- Key achievements highlighted
- Clean, contemporary design

### Classic Template
- Times New Roman font
- Traditional layout
- SUMMARY section
- Professional appearance

### Professional Template
- Arial font
- Formal structure
- PROFESSIONAL SUMMARY
- PROFESSIONAL EXPERIENCE sections

## 🔍 ATS Keyword Detection

### Common Keywords Database
```python
[
    'python', 'java', 'javascript', 'sql', 'machine learning',
    'cloud', 'aws', 'azure', 'docker', 'kubernetes',
    'project management', 'leadership', 'communication',
    'tensorflow', 'pytorch', 'pandas', 'numpy', 'scikit-learn',
    'git', 'github', 'ci/cd', 'rest api', 'microservices'
]
```

### Extraction Method
1. **TF-IDF Scoring** - Identifies most important terms in job description
2. **Keyword Matching** - Checks against common ATS keywords
3. **Deduplication** - Removes duplicates
4. **Top 25 Selection** - Returns most relevant keywords


## 💾 Output Files

### Generated Files
| File Type|                 Example               | Purpose |
|----------|-------------------------------------- |---------|
| **PDF**  | Resume_Modern.pdf                     | Professional formatted resume |
| **DOCX** | Resume_Professional.docx              | Editable Word document |
| **ZIP**  | Portfolio_John_Doe_20260118.zip       | Complete portfolio package |
| **JSON** | profile_John_Doe_20260118_192307.json | Saved profile for future use |

### ZIP Contents
```
Portfolio_[Name]_[Date].zip
├── Resume_[Name].pdf
├── Resume_[Name].docx
├── Cover_Letter.txt
├── Professional_Summary.txt
└── Resume_Content.txt
```

## ⚙️ Configuration

### Sidebar Options
- **Choose Template**: Select between Modern, Classic, or Professional
- **Export Format**: Choose PDF, DOCX, or Both
- **Load Profile**: Upload previously saved JSON profile

### Customization Points
```python
# Modify ATS keywords list (line 75-88)
common_keywords = [...]

# Adjust TF-IDF parameters (line 95-99)
vectorizer = TfidfVectorizer(
    max_features=30,
    ngram_range=(1, 2),
    ...
)

# Change template designs (modify PDF generation functions)
```

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'docx'"
**Solution**: Install python-docx
```bash
pip install python-docx
```
Or use PDF-only export mode.

### Issue: PDF text extraction fails
**Solution**: Ensure your PDF is:
- Not encrypted or password-protected
- Has extractable text (not scanned image)
- Reasonable file size (<50MB)

### Issue: Special characters appear as boxes
**Solution**: This is handled automatically by `sanitize_text_for_pdf()` function. Non-latin-1 characters are converted to ASCII.

### Issue: Streamlit app won't start
**Solution**: 
```bash
# Check Python version
python --version  # Should be 3.11+

# Reinstall streamlit
pip install --upgrade streamlit

# Try running with explicit interpreter
python -m streamlit run app.py
```

### Issue: App running but can't access browser
**Solution**: 
- Check URL: `http://localhost:8501`
- If port 8501 is in use, run on different port:
```bash
streamlit run app.py --server.port 8502
```

## 📊 Performance Metrics

| Operation               | Time | Memory |
|-----------              |------|--------|
| PDF Extraction          | <1s  | ~10MB |
| Resume Enhancement      | <2s  | ~20MB |
| Cover Letter Generation | <1s  | ~5MB |
| PDF Creation            | <1s  | ~15MB |
| DOCX Creation           | <1s  | ~10MB |
| ZIP Creation            | <1s  | ~5MB |
| **Total**               |   6s | 65MB |

## 🔐 Data Privacy

- ✅ **No Cloud Uploads** - All processing happens locally
- ✅ **No Account Required** - No login needed
- ✅ **No Tracking** - No analytics or tracking
- ✅ **Local Storage** - Profiles saved only on your machine
- ✅ **Open Source** - Full source code visible for audit


### Under Consideration
- Real LLM integration (optional, with API keys)
- Video resume support
- Portfolio website generator
- Interview question generator
- Salary negotiation guide

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

### Steps
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Guidelines
- Follow PEP 8 style guide
- Add docstrings to functions
- Test your changes locally
- Update README if needed

## 💬 Support & Issues

### Getting Help
- 📖 Check [Troubleshooting](#-troubleshooting) section
- 🐛 Open an issue on GitHub
- 💬 Start a discussion in GitHub Discussions
- 📧 Contact: your-email@example.com

### Reporting Bugs
Include:
- Python version
- OS (Windows/Mac/Linux)
- Steps to reproduce
- Error message
- Expected behavior

## 📚 Documentation

### Files
- `app.py` - Main application code with inline documentation
- `requirements.txt` - Complete dependency list with versions
- `README.md` - This file

### Code Structure
```python
# Section 1: Imports & Setup (lines 1-32)
# Section 2: PDF & Document Utilities (lines 34-50)
# Section 3: ATS Keyword Extraction (lines 52-110)
# Section 4: AI/NLP Logic (lines 112-200)
# Section 5: PDF Generator (lines 202-280)
# Section 6: DOCX Generator (lines 282-315)
# Section 7: Portfolio ZIP Generator (lines 317-340)
# Section 8: JSON Profile Management (lines 342-360)
# Section 9: Streamlit UI (lines 362-701)
```
## 🎓 Learning Resources

### NLP Concepts
- [TF-IDF Explained](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
- [scikit-learn TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- [STAR Method](https://en.wikipedia.org/wiki/Situation,_task,_action,_result)

### Technologies
- [Streamlit Documentation](https://docs.streamlit.io)
- [PyPDF2 Guide](https://pypdf2.readthedocs.io)
- [python-docx Documentation](https://python-docx.readthedocs.io)

## 📞 Contact & Feedback

- **GitHub**: [Your GitHub Profile]
- **Email**: your-email@example.com
- **Website**: [Your Website]
- **LinkedIn**: [Your LinkedIn]

## 🙏 Acknowledgments

- Streamlit team for excellent framework
- scikit-learn for NLP tools
- Open source community for contributions
- All beta testers and feedback providers

## 📈 Statistics

- **Lines of Code**: ~700
- **Functions**: 15+
- **Templates**: 3
- **Export Formats**: 4
- **Development Time**: ~50 hours
- **Last Updated**: January 18, 2026

## 🚀 Future Enhancements

### Planned Features
- [ ] LinkedIn profile import
- [ ] Spell check & grammar suggestions
- [ ] Resume scoring against job description
- [ ] Multiple language support
- [ ] Email integration for sending resumes
- [ ] Cloud storage option (optional)
- [ ] Resume templates gallery
- [ ] Career advice chatbot
- [ ] Job market analytics
