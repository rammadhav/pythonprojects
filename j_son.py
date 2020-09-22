import json

def convert_ptoj():
    customer =[
        {
            "name": "bhaskar",
            "age": 30,
            "city": "New York",
            "skills":("python","javascript"),
        },
        {
            "name":"shyam",
            "age":"55",
            "city":"torento"
        }
    ]
    cost_data = json.dumps(customer)
    print(type(cost_data))
    print(cost_data)
    customer.append(cost_data)
    customers =[]
    customers.append(cost_data)
    print(customers)

def convert_jt0p():
    customer='[{"name": "bhaskar","age": 30, "city": "New York","skills": ["python", "javascript"]},{"name": "shyam","age": "55","city": "torento"}]'

    cost_data = json.loads(customer)
    cost_data[1]["skills"]=["java","c#"]
    print(type(cost_data))
    print(cost_data)



convert_ptoj()
convert_jt0p()
