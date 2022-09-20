workdays = int(input())
day_salary = float(input())
rate = float(input())

taxes = 1 - 25 / 100
m_salary = workdays * day_salary
bonus = 2.5 * m_salary
yearly_salary = m_salary * 12 + bonus
a_day_salary = ((yearly_salary * taxes) / 365) * rate

print(f'{a_day_salary:0.2f}')