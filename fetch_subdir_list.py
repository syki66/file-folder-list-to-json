import os
import datetime
import json

user_input = input("디렉토리 경로를 정확히 입력해주세요 : ")

user_path = user_input

json_path = "./test.json" # 이름 변경할수 있도록 하기
json_data = {}
json_data['sub_info'] = []
json_data['root_info'] = []

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
 
        # 하위 디렉토리가 존재한다면 재귀함수 호출
        if (not not subdir_list): # 빈리스트가 아니라면 실행
            for subdir in subdir_list:
                fetch_sub_things(subdir)


# 경로정보를 이용해서 json 만들기
def make_json(path_list):
    for path in path_list:
        if (os.path.isdir(path)):
            path_type = "directory"
            path_size = get_size(path)
        elif (os.path.isfile):
            path_type = "file"
            path_size = os.path.getsize(path)
        else:
            path_type = "unknown"

        json_data['sub_info'].append({
            "path" : path,
            "create_time" : str( datetime.datetime.fromtimestamp( (os.path.getctime(path)) ) ), # 만든시간을 타임 스탬프로 출력 후 실제시간으로 변환
            "modify_time" : str( datetime.datetime.fromtimestamp( (os.path.getmtime(path)) ) ), # 수정시간
            "access_time" : str( datetime.datetime.fromtimestamp( (os.path.getatime(path)) ) ), # 마지막 엑세스시간
            "size"        : path_size, # 크기
            "type"        : path_type # 폴더인지 파일인지
        })

        # 단순히 커맨드 창에서의 시각효과
        print(path)
        print(str( datetime.datetime.fromtimestamp( (os.path.getctime(path)) ) ))
        print(str( datetime.datetime.fromtimestamp( (os.path.getmtime(path)) ) ))
        print(str( datetime.datetime.fromtimestamp( (os.path.getatime(path)) ) ))
        print(path_size)
        print(path_type)


# 결과 보여주고 루트 디렉토리 정보 json으로 넣어주는 함수
def show_result():
    json_data['root_info'].append({
        "path"    : user_path,
        "folders" : dir_count - 1,
        "files"   : file_count,
        "create_time" : str( datetime.datetime.fromtimestamp( (os.path.getctime(user_path)) ) ), # 만든시간을 타임 스탬프로 출력 후 실제시간으로 변환
        "modify_time" : str( datetime.datetime.fromtimestamp( (os.path.getmtime(user_path)) ) ), # 수정시간
        "access_time" : str( datetime.datetime.fromtimestamp( (os.path.getatime(user_path)) ) ), # 마지막 엑세스시간
        "size"        : get_size(user_path), # 크기
        "type"        : "directory"
        
    })

    print(f'\n위치         : {user_path}')
    print(f'전체 폴더 수 : {dir_count - 1}') # 루트 폴더를 제외한 폴더 수
    print(f'전체 파일 수 : {file_count}') # 전체 파일 수
    print(f'크기         : {get_size(user_path)}')
    print(f'만든 날짜    : {str( datetime.datetime.fromtimestamp( (os.path.getctime(user_path)) ) )}')
    print(f'수정한 날짜  : {str( datetime.datetime.fromtimestamp( (os.path.getmtime(user_path)) ) )}')
    print(f'엑세스 날짜  : {str( datetime.datetime.fromtimestamp( (os.path.getatime(user_path)) ) )}')
    print(f'타입         : 폴더')


# 하위 디렉토리 크기까지 합산해서 현재 디렉토리 크기 계산
def get_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size




if (os.path.isdir(user_path)):

    fetch_sub_things(user_path)
    show_result()

    # json 파일 생성
    with open(json_path, 'w', encoding="utf-8") as outfile:
        json.dump(json_data, outfile, ensure_ascii=False, indent=4)

else:
    print("디렉토리 경로명을 정확히 입력해주세요")


input("\n엔터를 누르면 프로그램이 종료됩니다.")