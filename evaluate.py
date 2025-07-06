import sqlite3
from main import get_sql_from_nl

def run_sql(sql):
    try:
        conn = sqlite3.connect("test.db")
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        return result
    except Exception as e:
        return str(e)

def test_cases():
    cases = [
        {
            "nl": "Show all customers from Delhi",
            "expected_sql": "SELECT * FROM customers WHERE city = 'Delhi'",
            "expected_result": [(1, 'Amit', 'Delhi'), (3, 'Neha', 'Delhi')]
        },
        {
            "nl": "Count the number of customers",
            "expected_sql": "SELECT COUNT(*) FROM customers",
            "expected_result": [(3,)]
        }
    ]

    for i, case in enumerate(cases, 1):
        print(f"\nTest Case {i}: {case['nl']}")
        predicted_sql = get_sql_from_nl(case["nl"])
        print("Predicted SQL:", predicted_sql)

        actual_result = run_sql(predicted_sql)
        print("Actual Result:", actual_result)

        print("Expected Result:", case["expected_result"])
        print("Match:", actual_result == case["expected_result"])

if __name__ == "__main__":
    test_cases()
