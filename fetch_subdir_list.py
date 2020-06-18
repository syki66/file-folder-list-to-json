import os

user_path = r'C:\Users\syki66\Desktop\exexxe' # 사용자의 입력으로 바꾸기

def fetch_sub_things(path):
    if (not os.path.exists(path)):
        print("경로가 존재하지 않습니다.")

    else:
        dir_list = os.listdir(path) # 하위 디렉토리의 파일 및 폴더 리스트
        subdir_list = [] # 하위 디렉토리 리스트
        subfile_list = [] # 하위 파일 리스트

        for subthing in dir_list:
            if (os.path.isdir(path + '\\' + subthing)):
                subdir_list.append(path + '\\' + subthing)
            
            elif (os.path.isfile):
                subfile_list.append(path + '\\' + subthing)
            
            else:
                print("알 수 없는 에러 발생")
        
        print(subfile_list)

        # 하위 디렉토리가 존재한다면 재귀함수 호출
        if (not not subdir_list):
            for subdir in subdir_list:
                fetch_sub_things(subdir)

fetch_sub_things(user_path)