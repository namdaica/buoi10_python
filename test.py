import  main as ma
import re
# print(ma.created_facebook_account(1,2,3))
# y = ma.created_facebook_account(phone="phone",email="email",name="name",address="14 phan ton")
# print(y)

# print(ma.xin_chao(list[0],loi_chao="Hello "))

# print(ma.my_title("nam"))
def mytitle2(srt):
    s1 = ""
    srt2 = re.findall("[^-@,\s]+",srt.lower()) # tim chuoi con bang reg
    print(srt2) #in test
    for l in srt2:
        s1 = s1+ (ma.my_title(l)) + " " #cong chuoi thanh ket qua
    return s1
print(mytitle2("phan hoang Nam"))

