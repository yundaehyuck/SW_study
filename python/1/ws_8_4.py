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

class Bus(PublicTransport):

    def __init__(self,name,fare,threshold):
        super().__init__(name,fare)
        self.threshold = threshold
    
    def get_in(self,passenger):
        
        PublicTransport.now_passenger += passenger

        if self.threshold < PublicTransport.now_passenger:

            return '더 이상 탑승할 수 없습니다.'
        
        else:
            
            PublicTransport.total_passenger += passenger
            
            print(f'현재 탑승자 수 : {PublicTransport.now_passenger}명')


bus = Bus(name='daehyuck',fare=1000,threshold=20)

bus.get_in(10)
bus.get_off(5)
bus.get_in(13)
bus.get_off(3)
bus.get_in(10)

print(f'최종수익 : {bus.profit()}원')
print(f'전체 탑승자 수: {bus.total_passenger}명')
