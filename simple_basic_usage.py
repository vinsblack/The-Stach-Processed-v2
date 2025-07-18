#!/usr/bin/env python3
"""
Basic Usage Examples for The Stack Processed v2

Simple examples for loading and exploring the dataset.
Dataset: 104,885 high-quality code samples

Author: VinsBlack
License: Commercial License (see LICENSE file)
"""

from datasets import load_dataset
import pandas as pd
from collections import Counter

def main():
    print("🚀 The Stack Processed v2 - Basic Usage")
    print("=" * 50)
    
    # Load dataset
    print("📥 Loading dataset...")
    try:
        dataset = load_dataset("vinsblack/The_Stack_Processed-v2")
        train_data = dataset['train']
        print(f"✅ Loaded {len(train_data)} samples")
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return
    
    # Basic statistics
    print("\n📊 Dataset Overview:")
    print(f"Total samples: {len(train_data):,}")
    
    # Language distribution
    languages = Counter(sample['language'] for sample in train_data)
    print(f"\n🌍 Language Distribution:")
    for lang, count in languages.most_common():
        percentage = (count / len(train_data)) * 100
        print(f"  {lang}: {count:,} samples ({percentage:.1f}%)")
    
    # Quality statistics
    quality_scores = [sample['quality_score'] for sample in train_data]
    avg_quality = sum(quality_scores) / len(quality_scores)
    high_quality = sum(1 for score in quality_scores if score > 0.95)
    
    print(f"\n⭐ Quality Metrics:")
    print(f"  Average quality: {avg_quality:.3f}")
    print(f"  High quality (>0.95): {high_quality:,} samples ({(high_quality/len(train_data)*100):.1f}%)")
    print(f"  Min quality: {min(quality_scores):.3f}")
    print(f"  Max quality: {max(quality_scores):.3f}")
    
    # Sample by language
    print(f"\n🐍 Python Sample:")
    python_samples = [s for s in train_data if s['language'] == 'python']
    if python_samples:
        sample = python_samples[0]
        print(f"Quality Score: {sample['quality_score']:.3f}")
        print("Code Preview:")
        print("-" * 40)
        print(sample['content'][:300] + "...")
    
    # Filter high-quality samples
    print(f"\n🎯 High-Quality Filtering:")
    high_quality_samples = [s for s in train_data if s['quality_score'] > 0.95]
    print(f"High-quality samples: {len(high_quality_samples):,}")
    
    # Export sample to CSV for analysis
    print(f"\n💾 Exporting sample data...")
    sample_data = []
    for i, sample in enumerate(train_data):
        if i >= 1000:  # First 1000 samples
            break
        sample_data.append({
            'language': sample['language'],
            'quality_score': sample['quality_score'],
            'code_length': len(sample['content']),
            'line_count': len(sample['content'].split('\n'))
        })
    
    df = pd.DataFrame(sample_data)
    df.to_csv('dataset_sample.csv', index=False)
    print(f"✅ Exported sample data to dataset_sample.csv")
    
    print(f"\n🎉 Basic usage completed!")
    print(f"\n📚 Next steps:")
    print(f"  1. Explore the CSV file")
    print(f"  2. Filter by your preferred language")
    print(f"  3. Train your models with high-quality data")

if __name__ == "__main__":
    main()
