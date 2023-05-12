# 전화번호부

def solution (phone_book):
    #hash data map 만들기, 처음에는 빈 배열로 초기화
    hash_data = {}
    for phone_number in phone_book:
        #파라미터 값을 넣어주기 ex) {"119" : 1, "97674223" : 1, "1195524421" : 1}
        hash_data[phone_number] = 1
        
    for phone_number in phone_book:
        #접두어 빈 문자열로 초기화해주기
        prefix = ''
        #번호 한자릿수씩 저장해 나가기
        for number in phone_number:
            prefix += number
            #해시 맵 안에 있는지 확인하고, 전화번호와 동일하면 안대는 걸로 조건 걸기
            if prefix in hash_data and prefix != phone_number:
                return False
    return True
