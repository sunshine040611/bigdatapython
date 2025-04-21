import func
while True:
    print("===================")
    print("1. 멜론 100")
    print("2. 멜론 50")
    print("3. 멜론 10")
    print("4. AI 추천 노래")
    print("5. 가수 이름 검색")
    print("6. 파일에 저장(멜론100)")
    print("0. 종료")
    print("===================")

    choice = input("원하는 번호를 입력하세요: ")

    if choice == "1":
        func.m100("멜론 100")
    elif choice == "2":
        func.m50("멜론 50")
    elif choice == "3":
        func.m10("멜론 10")
    elif choice == "4":
        func.m_random("AI 추천 노래")
    elif choice == "5":
        name = input("가수 이름을 입력하세요: ")
        func.m_search(name)
    elif choice == "6":
        func.m_save("멜론100.txt")
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")
        # func.py

def m100(title):
    print(f"[{title}] 출력합니다.")
    # 여기에 실제 멜론 100 출력 코드 작성

def m50(title):
    print(f"[{title}] 출력합니다.")
    # 멜론 50

def m10(title):
    print(f"[{title}] 출력합니다.")
    # 멜론 10

def m_random(title):
    print(f"[{title}] 랜덤 추천입니다.")
    # 랜덤 추천 노래 출력

def m_search(name):
    print(f"{name}의 노래를 검색합니다.")
    # 검색 기능

def m_save(filename):
    print(f"{filename}으로 저장합니다.")
    # 파일 저장 기능