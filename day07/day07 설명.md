## 📘 문제 이름
나머지가 1이 되는 수 찾기

- 🧩 난이도: level 1
- 🛠 사용 언어: Python3
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/87389)

---

### 🧠 문제 설명
자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.
---

### 💡 아이디어
def 함수를 통해서 soluton 정의하기
range를 사용해서 문제 풀이  
for문과 range를 융합해서 풀이
---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)
for문과 range문을 사용해서 나머지 구하기

---

### 다른 사람의 풀이
return [x for x in range(1,n+1) if n%x==1][0]
사람들은 한 줄로 끝내는걸 좋아하나보다. 간단할 수록 코드는 길어지는지라 
이득인지 잘 모르겠다.