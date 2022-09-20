pr_flour = float(input())
kg_flour = float(input())
kg_sugar = float(input())
couple_eggs = int(input())
yeast = int(input())

pr_sugar = pr_flour * 0.75
pr_couple_eggs = pr_flour * 1.1
pr_yeast = pr_sugar * 0.2

total = pr_sugar * kg_sugar + pr_couple_eggs * couple_eggs + pr_yeast * yeast + pr_flour * kg_flour

print(f"{total:.2f}")