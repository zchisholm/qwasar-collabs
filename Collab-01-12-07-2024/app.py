# Import required libraries
import pandas as pd
import random
from faker import Faker
from faker.providers import BaseProvider

# Initialize Faker
fake = Faker()

# Create empty lists to store data
user_ids = []
names = []
emails = []
subscription_start_dates = []
subscription_types = []
countries = []
payment_methods = []

# Define subscription types and payment methods
#subscription_types_list = ['Basic', 'Standard', 'Premium']
payment_methods_list = ['Credit Card', 'PayPal', 'Bank Transfer']


class SubscriptionProvider(BaseProvider):
    def sub_type(self):
        subscription_types_list = ['Basic', 'Standard', 'Premium']
        return self.random_element(subscription_types_list)
    def payment_type(self):
        payment_methods_list = ['Credit Card', 'PayPal', 'Bank Transfer']
        return self.random_element(payment_methods_list)


fake.add_provider(SubscriptionProvider)

# Generate data for 1000 users
for i in range(1000):
    user_ids.append(i + 1)
    names.append(fake.name() if random.random() > 0.1 else None)  # 10% missing names
    emails.append(fake.email() if random.random() > 0.05 else "invalid_email")  # 5% invalid emails
    subscription_start_dates.append(fake.date())
    subscription_types.append(fake.sub_type())
    countries.append(fake.country() if random.random() > 0.02 else None)  # 2% missing countries
    payment_methods.append(fake.payment_type())

# Introduce some duplicate rows
for _ in range(10):
    idx = random.randint(0, 999)
    user_ids.append(user_ids[idx])
    names.append(names[idx])
    emails.append(emails[idx])
    subscription_start_dates.append(subscription_start_dates[idx])
    subscription_types.append(subscription_types[idx])
    countries.append(countries[idx])
    payment_methods.append(payment_methods[idx])

# Create a DataFrame and save to CSV
data = {
    'User ID': user_ids,
    'Name': names,
    'Email': emails,
    'Subscription Start Date': subscription_start_dates,
    'Subscription Type': subscription_types,
    'Country': countries,
    'Payment Method': payment_methods
}

df = pd.DataFrame(data)
df.to_csv('simple_stream_subscribers.csv', index=False)

print("Simple sample dataset created successfully!")