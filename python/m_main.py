import func

# 사용자의 입력을 받아서 멜론 차트 출력 프로그램 만들기
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
        func.m_save("melon100.txt")
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")