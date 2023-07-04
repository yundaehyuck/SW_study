# 여기에 필요한 모듈을 추가합니다.
import random
import json

class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        
        self.number_lines = []

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        
        for i in range(n):
            
            self.number_lines.append(sorted(random.sample(range(1,46),6)))
        
        return None

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        
        year,month,day = self.get_draw_date(draw_number)

        alpha_line = ['A','B','C','D','E']

        print('======================================================================')
        print(f'제 {draw_number} 회 로또'.center(66))
        print('======================================================================')
        print(f'추첨일 : {year}/{month}/{day} (토)')
        print('======================================================================')

        for alpha,line in zip(alpha_line[:len(self.number_lines)],self.number_lines):

            print(f'{alpha} : {line}')
        
        """for ind,line in enumerate(self.number_lines):

            print(f'{alpha_line[ind]} : {line}')"""
        
        """for ind,line in enumerate(self.number_lines):

            print(f'{chr(65+ind)} : {line}')"""
        
        return None



    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        
        main_numbers,bonus_number = self.get_lotto_numbers(draw_number)

        alpha_line = ['A','B','C','D','E']

        print('======================================================================')
        print(f'당첨 번호 : {main_numbers} + {bonus_number}')
        print('======================================================================')

        for alpha,line in zip(alpha_line,self.number_lines):

            same_main_counts,is_bonus = self.get_same_info(main_numbers,bonus_number,line)

            ranking = self.get_ranking(same_main_counts,is_bonus)

            if is_bonus:

                if ranking != -1:

                    print(f'{alpha} : {same_main_counts}개 + 보너스 일치 ({ranking}등 당첨!)')
                
                else:
                    print(f'{alpha} : {same_main_counts}개 + 보너스 일치 (낙첨)')
            
            else:

                if ranking != -1:

                    print(f'{alpha} : {same_main_counts}개 일치 ({ranking}등 당첨!)')
                
                else:

                    print(f'{alpha} : {same_main_counts}개 일치 (낙첨)')

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        
        target_dir = f"data\lotto_{draw_number}.json"

        lotto_file = open(target_dir)
        lotto_json = json.load(lotto_file)

        draw_day = lotto_json['drwNoDate']

        year,month,day = draw_day.split('-')

        return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        
        target_dir = f"data\lotto_{draw_number}.json"

        lotto_file = open(target_dir)
        lotto_json = json.load(lotto_file)

        main_numbers = []

        for key in lotto_json.keys():

            if key.startswith('drwt'):

                main_numbers.append(lotto_json[key])
        
        #main_numbers = [lotto_json[key] for key in lotto_json.keys() if key.startswith('drwt')]

        return sorted(main_numbers), lotto_json['bnusNo']

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        
        same_main_counts = 0

        for main_num,my_num in zip(main_numbers,line):

            if main_num == my_num:

                same_main_counts += 1
        
        #same_main_counts = len(set(main_numbers) & set(line))
        
        if bonus_number in line:

            is_bonus = True
        
        else:
            is_bonus = False


        return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        
        if same_main_counts == 6:

            ranking = 1
        
        elif same_main_counts == 5 and is_bonus:

            ranking = 2
        
        elif same_main_counts == 5:

            ranking = 3
        
        elif same_main_counts == 4:

            ranking = 4
        
        elif same_main_counts == 3:

            ranking = 5
        
        else:
            ranking = -1
        
        return ranking
