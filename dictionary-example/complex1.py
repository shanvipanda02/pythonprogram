complex_dict = {
    "company": {
        "name": "TechCorp",
        "location": "San Francisco",
        "employees": [
            {
                "name": "Alice",
                "age": 30,
                "department": "Engineering",
                "skills": ["Python", "C++", "Machine Learning"],
                "address": {
                    "street": "123 Tech Lane",
                    "city": "San Francisco",
                    "state": "CA",
                    "zipcode": 94105
                },
                "projects": [
                    {"name": "Project A", "status": "Completed", "budget": 100000},
                    {"name": "Project B", "status": "Ongoing", "budget": 200000}
                ]
            },
            {
                "name": "Bob",
                "age": 25,
                "department": "Marketing",
                "skills": ["SEO", "Content Creation"],
                "address": {
                    "street": "456 Market St",
                    "city": "San Francisco",
                    "state": "CA",
                    "zipcode": 94107
                },
                "projects": [
                    {"name": "Campaign X", "status": "Completed", "budget": 50000},
                    {"name": "Campaign Y", "status": "Planning", "budget": 80000}
                ]
            }
        ]
    },
    "financials": {
        "2023": {
            "revenue": 1000000,
            "expenses": 750000,
            "profit": 250000
        },
        "2024": {
            "revenue": 1200000,
            "expenses": 800000,
            "profit": 400000
        }
    },
    "products": [
        {"name": "Product 1", "category": "Software", "price": 299.99},
        {"name": "Product 2", "category": "Hardware", "price": 199.99}
    ],
    "partners": {
        "Partner A": {
            "type": "Supplier",
            "contact": {
                "name": "John Doe",
                "email": "john.doe@example.com"
            }
        },
        "Partner B": {
            "type": "Distributor",
            "contact": {
                "name": "Jane Smith",
                "email": "jane.smith@example.com"
            }
        }
    }
}

# Accessing data within the complex dictionary
print(complex_dict["company"]["employees"][0]["name"])  # Output: Alice
print(complex_dict["financials"]["2023"]["profit"])      # Output: 250000
print(complex_dict["products"][1]["price"])              # Output: 199.99
print(complex_dict["partners"]["Partner A"]["contact"]["email"])  # Output: john.doe@example.com

