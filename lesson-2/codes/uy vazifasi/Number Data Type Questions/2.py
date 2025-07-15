#Write a Python file that asks for three numbers and outputs the largest and smallest.


birinchi_raqam = float (input("birinchi raqamni kiriting: "))
ikkinchi_raqam = float (input("ikkinchi raqamni kiriting: "))
uchunchi_raqam = float (input("uchunchi raqamni kiriting: "))
eng_katta_raqam = max (birinchi_raqam, ikkinchi_raqam, uchunchi_raqam)
eng_kichik_raqam = min(birinchi_raqam, ikkinchi_raqam, uchunchi_raqam)
print("Eng katta raqam = :", eng_katta_raqam)
print("Eng kichik raqam = :", eng_kichik_raqam)