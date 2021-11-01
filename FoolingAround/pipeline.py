# Reading the csv file using generators pipeline
lines = (line for line in open("sample.csv"))
list_line = (line.strip().split(",") for line in lines)

cols = next(list_line)

# print(cols)
# squirel_dict = (dict(zip(cols, data) for data in list_line))
company_dicts = (dict(zip(cols, data)) for data in list_line)

funding = (
    (company_dict["company"], int(company_dict["raisedAmt"]))
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
for fund in funding:
    print(fund[0], fund[1])