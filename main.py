#!/usr/bin/env python3
"""
Model Comparator CLI - Compare different LLM models
"""
import argparse
from pathlib import Path

# Import model handlers will be added here

def main():
    parser = argparse.ArgumentParser(description='Compare different LLM models')
    parser.add_argument('--prompt', type=str, help='Input prompt for the models')
    parser.add_argument('--models', nargs='+', help='List of models to compare')
    
    args = parser.parse_args()
    print("Model Comparator CLI")
    print("===================")

if __name__ == "__main__":
    main()
