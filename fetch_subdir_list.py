import os

user_path = r'C:\Users\syki66\Desktop\연습용 최상위 디렉토리' # 사용자의 입력으로 바꾸기

file_count = 0
dir_count = 0

def fetch_sub_things(path):
    global dir_count
    global file_count
    dir_count += 1 # 폴더 수 카운트

    if (not os.path.exists(path)):
        print("경로가 존재하지 않습니다.")

    else:
        dir_list = os.listdir(path) # 하위 디렉토리의 파일 및 폴더 리스트
        subdir_list = [] # 하위 디렉토리 리스트
        subfile_list = [] # 하위 파일 리스트

        # 하위 폴더 및 파일들을 리스트에 절대경로로 넣어줌
        for subthing in dir_list:
            if (os.path.isdir(path + '\\' + subthing)):
                subdir_list.append(path + '\\' + subthing)
            
            elif (os.path.isfile):
                subfile_list.append(path + '\\' + subthing)
            
            else:
                print("알 수 없는 에러 발생")
        
        file_count += len(subfile_list) # 파일 수 카운트

        # 빈 폴더일 경우 디렉토리값을 출력
        if (not subfile_list): # 파일이 없을경우
            print(path)
        elif (not not subfile_list): # 파일이 존재할경우
            print(subfile_list)
        else:
            print("알수 없는 에러")
        
        # 하위 디렉토리가 존재한다면 재귀함수 호출
        if (not not subdir_list): # 빈리스트가 아니라면 실행
            for subdir in subdir_list:
                fetch_sub_things(subdir)


# 결과 보여주는 함수
def show_result():
    print(f'루트폴더를 제외한 전체 폴더 수 : {dir_count - 1}') # 루트 폴더를 제외한 폴더 수
    print(f'전체 파일 수 :{file_count}') # 전체 파일 수


fetch_sub_things(user_path)
show_result()