def calculate_salary(basic):
    hra = 0.20 * basic
    da = 0.50 * basic
    pf = 0.11 * basic
    net_salary = (basic + hra + da) - pf
    return hra, da, pf, net_salary


def main():
    name = input("Enter Employee Name: ")
    emp_id = input("Enter Employee ID: ")
    designation = input("Enter Designation: ")

    try:
        basic_salary = float(input("Enter Basic Salary: "))
    except:
        print("Invalid salary input!")
        return

    hra, da, pf, net = calculate_salary(basic_salary)

    print("\n----- PAY SLIP -----")
    print(f"Name        : {name}")
    print(f"Employee ID : {emp_id}")
    print(f"Designation : {designation}")
    print(f"Basic Salary: ₹{basic_salary:.2f}")
    print(f"HRA (20%)   : ₹{hra:.2f}")
    print(f"DA (50%)    : ₹{da:.2f}")
    print(f"PF (11%)    : ₹{pf:.2f}")
    print("--------------------")
    print(f"Net Salary  : ₹{net:.2f}")


if __name__ == "__main__":
    main()
