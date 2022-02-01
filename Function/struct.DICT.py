money = {
    "Jan" : {
        "salary" : 1500,
        "expense" : 500
        },
    "Feb" : {
        "salary" : 1200,
        "expense" : 1700
        },
    "Mar" : {
        "salary" : 1700,
        "expense" : 700
        }
    }

for key in money:
    money[key]["balance"] = money[key]["salary"] - money[key]["expense"]
    print(money[key])

   
