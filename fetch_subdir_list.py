import os
import datetime
import json


user_path = r'D:\' # 사용자의 입력으로 바꾸기


json_path = "./test.json"
json_data = {}
json_data['info'] = []

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

        # 경로 리스트를 대입해서 json 파일 생성
        make_json(subfile_list)
        make_json(subdir_list)

        '''
        # 빈 폴더일 경우 디렉토리값을 출력
        if (not subfile_list): # 파일이 없을경우
            print(path)
        elif (not not subfile_list): # 파일이 존재할경우
            print(subfile_list)
        else:
            print("알수 없는 에러")

        '''     
        # 하위 디렉토리가 존재한다면 재귀함수 호출
        if (not not subdir_list): # 빈리스트가 아니라면 실행
            for subdir in subdir_list:
                fetch_sub_things(subdir)


# 폴더, 파일 정보 알려주는 함수
def make_json(path_list):
    for path in path_list:
        json_data['info'].append({
            "path" : path,
            "create_time" : (os.path.getctime(path)), # 만든시간을 타임 스탬프로 출력 후 실제시간으로 변환
            "modify_time" : (os.path.getmtime(path)), # 수정시간
            "access_time" : (os.path.getatime(path)), # 마지막 엑세스시간
            "file_size"   : os.path.getsize(path) # 파일크기
        })


# 결과 보여주는 함수
def show_result():
    print(f'루트폴더를 제외한 전체 폴더 수 : {dir_count - 1}') # 루트 폴더를 제외한 폴더 수
    print(f'전체 파일 수 :{file_count}') # 전체 파일 수


fetch_sub_things(user_path)

with open(json_path, 'w', encoding="utf-8") as outfile:
    json.dump(json_data, outfile, ensure_ascii=False, indent=4)


# print(json.dumps(json_data, ensure_ascii=False, indent="\t"))

show_result()