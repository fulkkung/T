import pandas as pd

fnames = [
    "standard.csv",
    "standard_uoc.csv",
    "standard_eoc.csv",
    "tpqi_net_oc.csv",

    "tsco_occupation.csv",
    "isco_occupation.csv",
    "tsic_industry.csv",
    "tsco_unit.csv",
    "isco_group.csv",
    "tsic_class.csv",
]

for fname in fnames:
    df = pd.read_csv(f'../../_src/datasource/raw/{fname}', dtype=str, keep_default_na=False, lineterminator='\n')
    df = df.head(100)
    df.to_csv(f"{fname}", index=False)