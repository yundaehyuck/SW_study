
class PublicTransport:

    now_passenger = 0

    total_passenger = 0

    def __init__(self,name,fare):

        self.name = name
        self.fare = fare
    
    def get_in(self,passenger):

        PublicTransport.now_passenger += passenger
        PublicTransport.total_passenger += passenger

        print(f"현재 탑승자 수 : {PublicTransport.now_passenger}명")
    
    def get_off(self,passenger):

        PublicTransport.now_passenger -= passenger

        print(f"현재 탑승자 수 : {PublicTransport.now_passenger}명")
    
    def profit(self):

        return self.fare * PublicTransport.total_passenger

pt = PublicTransport('daehyuckho',1200)

pt.get_in(10)
pt.get_off(4)
pt.get_in(3)
pt.get_off(2)

print(f"최종수익: {pt.profit()}원")
print(f"전체 이용자:{pt.total_passenger}명")
