from math import floor

hours = int(input())
minutes = int(input())

h_minutes = (minutes + 15) // 60
m_minutes = (minutes + 15) % 60
t_hours = hours + h_minutes
m_minutes = floor(m_minutes)

if t_hours < 24:
    if m_minutes < 10:
        print(f'{t_hours}:0{m_minutes}')
    else:
        print(f'{t_hours}:{m_minutes}')

else:
    if m_minutes < 10:
        print(f'0:0{m_minutes}')
    else:
        print(f'0:{m_minutes}')