
# Clinical Event Extraction Evaluation Report

## Quantitative Evaluation Summary
The system was evaluated on a clinical event dataset.
The evaluation measured temporality classification, subject
identification, event date accuracy and attribute completeness.

The model achieved moderate accuracy with most errors
occurring in upcoming event classification.

## Error Heatmap

CURRENT : 0  
CLINICAL_HISTORY : 0  
UPCOMING : 1  

PATIENT : 0  
FAMILY_MEMBER : 0  

## Top Systemic Weaknesses

- Difficulty detecting future events
- Temporal context confusion
- Missing attributes in some records

## Proposed Guardrails

- Temporal keyword detection
- Validation layer for entity extraction
- Confidence threshold filtering
