def bonAppetit(bill, k, b):
    # Write your code here
    not_eat=bill[k]
    total=0
    for i in bill:
        total+= i
    actual_share=int(total-not_eat)/2
    if b > actual_share  :
        valid_amount=int(b-actual_share)
        print(valid_amount)
    else:
        print("Bon Appetit")