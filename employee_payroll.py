
def calculate_hra(basic_salary):
    return basic_salary * 0.20


def calculate_da(basic_salary):
    return basic_salary * 0.10


def calculate_pf(basic_salary):
    return basic_salary * 0.12


def calculate_salary(basic_salary):
    hra = calculate_hra(basic_salary)
    da = calculate_da(basic_salary)
    pf = calculate_pf(basic_salary)

    gross_salary = basic_salary + hra + da
    net_salary = gross_salary - pf

    return hra, da, pf, gross_salary, net_salary


def display_salary(name, employee_id, basic_salary):
    hra, da, pf, gross, net = calculate_salary(basic_salary)

    print("\n===== EMPLOYEE PAYSLIP =====")
    print("Employee Name:", name)
    print("Employee ID:", employee_id)
    print("Basic Salary: Rs.", basic_salary)
    print("HRA: Rs.", hra)
    print("DA: Rs.", da)
    print("PF Deduction: Rs.", pf)
    print("----------------------------")
    print("Gross Salary: Rs.", gross)
    print("Net Salary: Rs.", net)


def main():
    name = input("Enter employee name: ")
    employee_id = input("Enter employee ID: ")
    basic_salary = float(input("Enter basic salary: Rs. "))

    if basic_salary < 0:
        print("Salary cannot be negative.")
        return

    display_salary(name, employee_id, basic_salary)


main()
