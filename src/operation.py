import pandas as pd
from pathlib import Path


def __get_data_frame():
    return pd.read_csv(str(Path.cwd()) + "/Ecommerce Purchases")


def define_companies():
    print("All Companies:")
    companies = dataFrame["Company"].unique()
    # for company in companies:
    #     print(company)
    for i in range(10):
        print(companies[i])
    print("." * 5)
    print("-" * 50)


def get_emails():
    print("All Emails:")
    emails = dataFrame["Email"].unique()
    # for email in emails:
    #     print(email)
    for i in range(10):
        print(emails[i])
    print("." * 5)
    print("-" * 50)


def get_max_purchase_price():
    print("Maximum Purchase Price", dataFrame["Purchase Price"].max())
    print("Full Info:")
    print(dataFrame[dataFrame["Purchase Price"] == dataFrame["Purchase Price"].max()])
    print("-" * 50)


def get_min_purchase_price():
    print("Minimum Purchase Price", dataFrame["Purchase Price"].min())
    print("Full Info:")
    print(dataFrame[dataFrame["Purchase Price"] == dataFrame["Purchase Price"].min()])
    print("-" * 50)


def get_purchase_price_average():
    print("Average Purchase Price", dataFrame["Purchase Price"].mean())
    print("-" * 50)


def get_user_info(email):
    employee = dataFrame[dataFrame["Email"] == email]
    print("Company:", employee.loc[employee.index[0], "Company"])
    print("Email:", employee.loc[employee.index[0], "Email"])
    print("Job:", employee.loc[employee.index[0], "Job"])
    print("Credit Card:", employee.loc[employee.index[0], "Credit Card"])
    print("CC Exp Date:", employee.loc[employee.index[0], "CC Exp Date"])
    print("CC Provider:", employee.loc[employee.index[0], "CC Provider"])
    print("Purchase Price:", employee.loc[employee.index[0], "Purchase Price"])
    print("-" * 50)


print("-" * 50)
# dataFrame = __getDataFrame().dropna()
dataFrame = __get_data_frame().fillna(value=0)
dataFrame.info()
print("-" * 50)
