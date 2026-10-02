
#nested if:

age = 18
has_id = True

if age>=18:
    print("age eligible")
    if has_id:
        print("id eligibel")
    else:
        print("not id eligible")

else:
    print("age not eligible")            