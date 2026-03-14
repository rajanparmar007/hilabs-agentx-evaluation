# HiLabs Agent-X Evaluation Pipeline

## Overview

This project implements an evaluation framework for a clinical event extraction system. The pipeline compares predicted entities with ground truth annotations and calculates performance metrics.

## Evaluation Metrics

The system evaluates extraction performance using the following metrics:

- Temporality Error Rate
- Subject Error Rate
- Event Date Accuracy
- Attribute Completeness

## Project Files

test.py – Python script used for evaluation 
input.json – Input dataset containing ground truth and predicted values  output.json – Generated evaluation results  report.md – Detailed evaluation report  

## How to Run
Run the evaluation script using Python:
python test.py input.json output.json
This command generates the evaluation metrics and saves them in `output.json`.

## Purpose

The goal of this project is to identify weaknesses in clinical event extraction systems and propose guardrails to improve reliability and robustness.

## Author

Rajan Parmar  Civil Engineering  Government Engineering College Bhuj
