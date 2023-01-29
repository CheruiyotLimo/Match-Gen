<<<<<<< HEAD
import random

aso = [1, 3, 5, 5, 2, 7, 9]
print(type(random.shuffle(aso)))

=======



list1 = ["afhas, aidwi", "ippow, aiiwpa"]
for i in list1:
    print(i.split(", "))
diagnoses = {}
drugs = {}
cohorts = {}

def cohorter(sample_list: list, l2: list, l3: list):
    for item in sample_list:
        x = item.split(", ")
        diagnoses[x[0]] = x[-1]
    print(diagnoses)
    for b in l2:
        y = b.split(", ")
        drugs[y[0]] = y[1]
    print(drugs)
    for c in l3:
        z = c.split(", ", 1)
        cohorts[z[0]] = z[1]
    print(cohorts)
    return

l1 = ["patient1 , melanoma", "patient2, glioblastoma", "patient3, melanoma"]
l2 = ["patient1, drug1", "patient2, drug1", "patient3, drug2", "patient3, drug1"]
l3 = ["melanoma, drug1", "drug1, glioblastoma", "melanoma, drug1, drug2"]
print(cohorter(l1, l2, l3))
>>>>>>> e2d2a83c227d1f20e0b5b505e2d31b84cd86bd7c
