from django.utils.formats import number_format

from outflows.models import Outflow
from products.models import Product


def get_product_metrics():
    products = Product.objects.all()
    total_cost_price = sum(product.cost_price *
                           product.quantity for product in products)
    total_selling_price = sum(
        product.selling_price * product.quantity for product in products)
    total_quanity = sum(product.quantity for product in products)
    total_profit = total_selling_price - total_cost_price

    return dict(
        total_cost_price=number_format(
            total_cost_price, decimal_pos=2, force_grouping=True),

        total_selling_price=number_format(
            total_selling_price, decimal_pos=2, force_grouping=True),

        total_quanity=total_quanity,

        total_profit=number_format(
            total_profit, decimal_pos=2, force_grouping=True),
    )


def get_sales_metrics():
    sales = Outflow.objects.all()
    total_sales = sales.count()
    total_products_sold = sum(sale.quantity for sale in sales)
    total_sales_value = sum(sale.product.selling_price *
                            sale.quantity for sale in sales)
    total_sales_cost = sum(sale.product.cost_price *
                           sale.quantity for sale in sales)
    total_sales_profit = total_sales_value - total_sales_cost

    return dict(
        total_sales=total_sales,
        total_products_sold=total_products_sold,
        total_sales_value=number_format(
            total_sales_value, decimal_pos=2, force_grouping=True),
        total_sales_profit=number_format(
            total_sales_profit, decimal_pos=2, force_grouping=True)
    )
