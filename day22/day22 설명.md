## 📘 문제 이름
내적

- 🧩 난이도: level 1
- 🛠 사용 언어: Python3
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/70128)

---

### 🧠 문제 설명
길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.

이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)

---

### 💡 아이디어
for문 사용
len 사용
range 사용
복합 연산자 사용
---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)
내적은 정동근 교수님께서 시험문제에 낸다고 하셔서 공부했었기 때문에 이건 사실 아는 문제다.
---

### 다른 사람의 풀이
def solution(a, b):
    return sum(x * y for x, y in zip(a, b))
이런 방식으로 푸는 사람도 있었다.
하지만 zip 방식은 잘 모르기 때문에 패스한다.