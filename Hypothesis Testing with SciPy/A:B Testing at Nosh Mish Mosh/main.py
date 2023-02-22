import noshmishmosh
import numpy as np

all_visitors = noshmishmosh.customer_visits
paying_visitors = noshmishmosh.purchasing_customers
paying_visitor_count = len(paying_visitors)
total_visitor_count = len(all_visitors)

baseline_percent = paying_visitor_count/total_visitor_count*100.0
print(baseline_percent)

#We’d like to know for sure that, with this change, we’ll be pulling in at least $1240 more every week.
payment_history = noshmishmosh.money_spent
average_payment = float(np.mean(payment_history))
new_customers_needed = np.ceil(1240/ average_payment)
print(new_customers_needed)

# I method of calculating lift
# percentage_point_increase = new_customers_needed/total_visitor_count*100.0
# print(percentage_point_increase)
# lift = percentage_point_increase/ baseline_percent
# print(lift)

# II method of calculating lift
lift = 100*(new_customers_needed + paying_visitor_count - paying_visitor_count)/paying_visitor_count
print(lift)

# baseline = 18.6
# significance threshold = 10
# minimum desired lift = 50.53

ab_sample_size = 494
