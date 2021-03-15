def send_email():
    """"
    :return :...
    """
    return "send success"
def save_database():
    """"
    :return :...
    """
    return "save success"
def created_facebook_account(email, name, phone,address="No data"):
    """"
    :param email : this is an email information from the form
    :param name : this is name
    :param phone : ...
    :return : No return value

    """
    print(address)
    if send_email()=="send success" and save_database()=="save success":
        return "account has been created"
    else:
        "account hasn't been create"
def xin_chao(*ten,loi_chao):
    for i in ten:
        print(loi_chao + i)

def my_title(value):
    v = value[0].upper()+value[1:len(value)]
    return v



