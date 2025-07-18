#!/usr/bin/env python3
"""
Simple Setup Script for The Stack Processed v2
Installation and basic usage utilities.
"""

import sys
import subprocess
import argparse

__version__ = "2.0.0"
__author__ = "VinsBlack"

# Installation profiles
INSTALL_PROFILES = {
    "basic": [
        "datasets>=2.0.0",
        "pandas>=1.5.0", 
        "numpy>=1.21.0"
    ],
    "full": [
        "datasets>=2.0.0",
        "pandas>=1.5.0",
        "numpy>=1.21.0",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.0",
        "scikit-learn>=1.1.0",
        "transformers>=4.20.0"
    ]
}

def install_profile(profile: str):
    """Install packages for a specific profile."""
    if profile not in INSTALL_PROFILES:
        print(f"❌ Unknown profile: {profile}")
        return False
    
    packages = INSTALL_PROFILES[profile]
    print(f"📦 Installing {profile} profile ({len(packages)} packages)...")
    
    for package in packages:
        print(f"Installing {package}...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", package], 
                         capture_output=True, check=True)
            print(f"✅ {package} installed")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")
            return False
    
    print(f"🎉 {profile} profile installed successfully!")
    return True

def test_dataset_access():
    """Test basic dataset access."""
    print("🔍 Testing dataset access...")
    try:
        from datasets import load_dataset
        dataset = load_dataset("vinsblack/The_Stack_Processed-v2", split="train[:10]")
        print(f"✅ Successfully loaded {len(dataset)} samples")
        print(f"📊 Sample fields: {list(dataset[0].keys())}")
        return True
    except Exception as e:
        print(f"❌ Dataset access failed: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Setup The Stack Processed v2")
    parser.add_argument("--profile", "-p", default="basic", 
                       choices=["basic", "full"],
                       help="Installation profile")
    parser.add_argument("--test", action="store_true",
                       help="Test dataset access")
    
    args = parser.parse_args()
    
    print("🚀 The Stack Processed v2 - Setup")
    print(f"Version: {__version__}")
    print()
    
    if not install_profile(args.profile):
        sys.exit(1)
    
    if args.test:
        if not test_dataset_access():
            sys.exit(1)
    
    print("\n✅ Setup completed!")
    print("\n📚 Next steps:")
    print("1. python examples/basic_usage.py")
    print("2. Check README.md for documentation")

if __name__ == "__main__":
    main()
