# The Stack Processed v2

**104,885 curated code samples from The Stack dataset**
questo è un dataset in try version di un datest enterprice da 1,4Tb

[![HuggingFace](https://img.shields.io/badge/🤗%20Dataset-Hugging%20Face-yellow)](https://huggingface.co/datasets/vinsblack/The_Stack_Processed-v2)
[![License](https://img.shields.io/badge/License-Commercial-blue)](LICENSE.md)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Quality](https://img.shields.io/badge/Quality-Curated-green)](examples/basic_usage.py)

A professionally curated subset of The Stack v2 dataset, processed and cleaned for machine learning applications. Ideal for code completion, language detection, and AI model training.

## 🚀 Quick Start

```python
from datasets import load_dataset

# Load the full dataset
dataset = load_dataset("vinsblack/The_Stack_Processed-v2")
print(f"Total samples: {len(dataset['train'])}")

# Filter by language
python_samples = dataset['train'].filter(lambda x: x['language'] == 'python')
print(f"Python samples: {len(python_samples)}")

# Access quality scores
high_quality = dataset['train'].filter(lambda x: x['quality_score'] > 0.9)
print(f"High quality samples: {len(high_quality)}")
```

## 📊 Dataset Overview

- **Total samples**: 104,885
- **Format**: Parquet (260MB, optimized for ML)
- **Source**: Curated from The Stack v2 (BigCode)
- **Fields**: `content`, `language`, `quality_score`
- **Languages**: Python, JavaScript, Java, C++, Go, Rust

## 🌍 Language Distribution

> **Note**: Run `python examples/basic_usage.py` to generate precise statistics

| Language | Samples | Percentage | Quality Avg |
|----------|---------|------------|-------------|
| Python | *calculating...* | *calculating...* | *calculating...* |
| JavaScript | *calculating...* | *calculating...* | *calculating...* |
| Java | *calculating...* | *calculating...* | *calculating...* |
| C++ | *calculating...* | *calculating...* | *calculating...* |
| Go | *calculating...* | *calculating...* | *calculating...* |
| Rust | *calculating...* | *calculating...* | *calculating...* |

*Statistics automatically generated from dataset analysis*

## ⭐ Quality Metrics

Our curation pipeline ensures high-quality code samples:

- **Syntax Validation**: AST parsing for Python/JavaScript
- **Content Filtering**: Removed empty files and minimal snippets
- **Deduplication**: Hash-based duplicate removal across the dataset
- **Quality Scoring**: Multi-factor scoring (0.0-1.0) based on:
  - Code length and complexity
  - Comment-to-code ratio
  - Syntax validity
  - Language-specific best practices

**Quality Score Distribution**:
- High (>0.9): *calculating...*
- Medium (0.7-0.9): *calculating...*
- Acceptable (0.5-0.7): *calculating...*

## 🎯 Use Cases

This dataset excels in:

### **Code Completion & Generation**
- Training small to medium-scale language models
- Fine-tuning existing models for specific languages
- Code suggestion systems

### **Language Detection & Analysis**
- Programming language classification
- Code quality assessment
- Syntax pattern recognition

### **Research & Education**
- Academic ML research projects
- Educational AI/ML curricula
- Rapid prototyping with clean data

### **Commercial Applications**
- IDE plugins and extensions
- Code review automation
- Developer productivity tools

## 📥 Installation & Setup

### Option 1: Quick Install
```bash
pip install datasets pandas numpy
python examples/basic_usage.py
```

### Option 2: Full Environment
```bash
git clone https://github.com/vinsblack/The_Stack_Processed-v2
cd The_Stack_Processed-v2
pip install -r requirements.txt
python setup.py --profile full --test
```

### Option 3: Production Use
```bash
pip install datasets>=2.0.0 pandas>=1.5.0 numpy>=1.21.0
# Load dataset directly in your application
```

## 📂 Repository Structure

```
The_Stack_Processed-v2/
├── README.md                   # This documentation
├── LICENSE.md                  # Commercial license terms
├── CHANGELOG.md                # Version history
├── requirements.txt            # Python dependencies
├── setup.py                    # Installation helper
├── data/
│   ├── train.parquet          # Main dataset (260MB, Git LFS)
│   └── dataset_info.json      # HuggingFace metadata
├── examples/
│   └── basic_usage.py         # Usage examples and statistics
└── ISSUE_TEMPLATE/
    └── bug_report.md          # Issue reporting template
```

## 🔧 Performance & Compatibility

- **Loading time**: 2-5 seconds on standard hardware
- **Memory usage**: ~500MB when fully loaded in memory
- **Streaming**: Supports HuggingFace streaming for large-scale processing
- **Compatibility**: Python 3.8+, Windows/macOS/Linux
- **Frameworks**: Compatible with HuggingFace, Pandas, PyTorch, TensorFlow

## ⚖️ Licensing

Commercial license with flexible pricing tiers:

- **Academic**: €500-1,000/year (research & education)
- **Startup**: €1,000-5,000/year (companies <€2M revenue)
- **Professional**: €5,000-15,000/year (full commercial rights)

See [LICENSE.md](LICENSE.md) for complete terms and contact information.

## 🚨 Limitations & Considerations

**Dataset Size**: 104K samples is suitable for small-to-medium scale models. For large language models, consider this as a high-quality subset or evaluation set.

**Language Coverage**: Focuses on 6 major languages. May not represent all coding patterns or domain-specific languages.

**Bias Inheritance**: Inherits potential biases from the original Stack dataset. Review samples before production use.

**Processing Constraints**: Automated curation may miss context-specific quality factors. Manual review recommended for critical applications.

## 📈 Benchmarks & Validation

Run benchmarks and validate the dataset:

```bash
python examples/basic_usage.py          # Generate statistics
python examples/quality_analysis.py     # Detailed quality metrics  
python examples/language_detection.py   # Test classification accuracy
```

## 📚 Citation

```bibtex
@dataset{stack_processed_v2_2025,
  title={The Stack Processed v2: Curated Code Dataset for Machine Learning},
  author={VinsBlack},
  year={2025},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/vinsblack/The_Stack_Processed-v2},
  note={Commercial license available}
}
```

## 🤝 Support & Contact

- 📧 **General**: vincenzo.gallo77@hotmail.com
- 💼 **Licensing**: vincenzo.gallo77@hotmail.com
- 🛠️ **Technical**: vincenzo.gallo77@hotmail.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/vinsblack/The_Stack_Processed-v2/issues)

## 🙏 Acknowledgments

This dataset builds upon [The Stack](https://huggingface.co/datasets/bigcode/the-stack) by BigCode. We thank the open-source community for making this foundation possible.

---

**Ready to start?** 
1. Check the [license terms](LICENSE.md)
2. Run `python examples/basic_usage.py` 
3. Explore the data and build amazing AI applications! 🚀
