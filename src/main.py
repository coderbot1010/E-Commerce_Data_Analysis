import src.operation as operation
import src.visualization as visualization

# ----------------------------------------------------- #

operation.get_emails()
operation.define_companies()
operation.get_max_purchase_price()
operation.get_min_purchase_price()
operation.get_purchase_price_average()

email = input("Enter User Email: ")
operation.get_user_info(email)

# ----------------------------------------------------- #

visualization.plot_purchase_price(operation.dataFrame)
visualization.heat_map(operation.dataFrame)
