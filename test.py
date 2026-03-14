import json

def evaluate(data):

    temporality_types = ["CURRENT","CLINICAL_HISTORY","UPCOMING","UNCERTAIN"]
    subject_types = ["PATIENT","FAMILY_MEMBER"]

    temporality_errors = {t:0 for t in temporality_types}
    temporality_total = {t:0 for t in temporality_types}

    subject_errors = {s:0 for s in subject_types}
    subject_total = {s:0 for s in subject_types}

    correct_dates = 0
    total_records = len(data["records"])

    attributes_total = 0
    attributes_extracted = 0

    for r in data["records"]:

        t_true = r["true_temporality"]
        t_pred = r["pred_temporality"]

        temporality_total[t_true] += 1
        if t_true != t_pred:
            temporality_errors[t_true] += 1

        s_true = r["true_subject"]
        s_pred = r["pred_subject"]

        subject_total[s_true] += 1
        if s_true != s_pred:
            subject_errors[s_true] += 1

        if r["true_date"] == r["pred_date"]:
            correct_dates += 1

        attributes_total += r["attributes_total"]
        attributes_extracted += r["attributes_extracted"]

    temporality_error_rate = {}
    for t in temporality_types:
        if temporality_total[t] == 0:
            temporality_error_rate[t] = 0
        else:
            temporality_error_rate[t] = round(
                temporality_errors[t] / temporality_total[t],2
            )

    subject_error_rate = {}
    for s in subject_types:
        if subject_total[s] == 0:
            subject_error_rate[s] = 0
        else:
            subject_error_rate[s] = round(
                subject_errors[s] / subject_total[s],2
            )

    result = {
        "temporality_error_rate": temporality_error_rate,
        "subject_error_rate": subject_error_rate,
        "event_date_accuracy": round(correct_dates / total_records,2),
        "attribute_completeness": round(attributes_extracted / attributes_total,2)
    }

    return result


with open("input.json") as f:
    data = json.load(f)

result = evaluate(data)

with open("output.json","w") as f:
    json.dump(result,f,indent=4)

print("Evaluation completed. Check output.json")