bread = int(input())
couple_eggs = int(input())
kg_biscuits = int(input())
eggs = couple_eggs * 12
total = bread * 3.20 + couple_eggs * 4.35 + kg_biscuits * 5.4 + eggs * 0.15

print(f"{total:.2f}")