import pyupbit

# Access Key, Secret Key
# 같은 디렉토리에 Access Key, Secret Key를 Key.txt로 저장
f = open("Key.txt", 'r')
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

# 업비트 로그인
upbit = pyupbit.Upbit(access, secret)