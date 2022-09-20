btc = float(input())
uan = float(input())
tax = float(input()) / 100

btc_bgn = 1168
uan_dol = 0.15
dol_bgn = 1.76
eur_bgn = 1.95
eur_dol = eur_bgn / dol_bgn

btc_eur = btc * btc_bgn / eur_bgn
uan_eur = uan * uan_dol / eur_dol

final_btc = btc_eur * (1 - tax)
final_uan = uan_eur * (1 - tax)
amount = final_btc + final_uan
print(f'{amount:0.2f}')