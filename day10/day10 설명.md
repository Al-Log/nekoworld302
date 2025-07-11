## 📘 문제 이름
문자열 내 p와 y의 개수

- 🧩 난이도: level 1
- 🛠 사용 언어: Python3
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12916)

---

### 🧠 문제 설명
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

---

### 💡 아이디어
def 함수를 통해서 soluton 정의하기
lower를 이용해서 모두 소문자로 변경하기
count로 개수 구하기
---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)
기존에 하던거라 함수 형식이 점점 익숙해지고있다.
---

### 다른 사람의 풀이
다른 사람은 리턴값에 함수를 그냥 완성해버렸다.
s.lower().count('p') 방식으로 했는데, 그냥 한줄 추가되냐 안되냐 그 차이다.