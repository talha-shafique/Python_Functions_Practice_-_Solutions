def average_salary(salaries):
    return sum(salaries) / len(salaries)


employee_salaries = [35000, 42000, 50000, 60000, 45000]  # Salaries of 5 employees
result = average_salary(employee_salaries)
print(f"The average salary is: {result}")
