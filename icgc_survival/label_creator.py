def extract_survival_labels(features, labels):
    donors = labels.set_index("icgc_donor_id")
    feature_donors = features.index
    labels = donors.loc[feature_donors, ["donor_survival_time", "donor_vital_status"]]
    labels["donor_survival_time"] = labels["donor_survival_time"]/365
    labels["donor_survival_time"] = labels["donor_survival_time"].apply(lambda x: round(x, 2))
    labels["donor_survival_time"] = labels["donor_survival_time"].astype("float16")
    labels["donor_vital_status"] = labels["donor_vital_status"].replace({"alive": 0, "deceased": 1})
    labels = labels.dropna()
    labels["donor_vital_status"].astype("int8")

    features = features.loc[labels.index, :]

    return labels, features
