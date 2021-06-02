class scheme:
    def __init__(self,scheme_id,scheme_name,outgoing_rate,message_charge):
        self.scheme_id=scheme_id
        self.scheme_name=scheme_name
        self.outgoing_rate=outgoing_rate
        self.message_charge=message_charge
        print("scheme id is :",self.scheme_id)
        print("scheme name is :", self.scheme_name)
        print("outgoing charge is :", self.outgoing_rate)
        print("message charge is :", self.message_charge)
class customer(scheme):
    def __init__(self,cust_id,name,mobile_no):
        self.cust_id=cust_id
        self.name=name
        self.mobile_no=mobile_no
        print("customer id is :", self.cust_id)
        print("customer name is :", self.name)
        print("customer mobile no. is :", self.mobile_no)
s=scheme(2021,"offer",0.05,1)
c=customer(15,"Manish",9714241051)