# nhan_doi = lambda a:a*2
# print(nhan_doi(2))

list_goc = [1,2,3,4,5,6,7,8,9,10]

list_moi = list(filter(lambda a:a%2==0,list_goc))

print(list_moi)

list_moi2 = list(map(lambda a:a*2,list_goc))
#hàm filter có chức năng là kiểm tra từng phần tử trong danh sách(list_goc), ứng với
# từng phần tử là tham số a, và a này sẽ mang đi kiểm tra xem có chia hết cho 2 hay không?
# nếu s chia hết cho 2 thì sẽ được add vào interable và sau đó chuyển sang kiểu list
print(list_moi2)





