# AniPunch
## 기술 스택
Python, Pygame, Design Pattern, Object-Oriented Programming
## 개요
Anipunch는 플레이어가 다양한 동물 캐릭터를 조작하여 목표물을 맞추는 아케이드 스타일의 게임입니다. 플레이어는 점수에 따라 게임 속도가 증가하고, 특정 점수에 도달하면 새로운 동물 캐릭터와 스킬이 추가됩니다.
## 기능
- 충돌 감지 및 처리: 미사일과 타겟 간의 충돌을 정확하게 감지하고, 충돌 시 타겟과 미사일을 삭제하여 점수 증가
- 스킬 변경 및 업그레이드: 사용자가 특정 키 입력을 통해 다양한 동물 캐릭터로 스킬을 변경할 수 있으며, 점수에 따라 새로운 스킬과 캐릭터가 추가
- 레벨 업 시스템: 일정 점수에 도달할 때마다 게임 속도가 증가하거나 새로운 캐릭터가 추가되는 레벨 업 시스템 구현
- 게임 오버 처리: 플레이어의 미스 횟수가 3번 이상일 경우 게임 오버 화면을 출력하고, 게임 종료 후 초기화
## 주요 업무
- 게임 로직 설계 및 구현: 충돌 감지, 캐릭터 이동, 타겟 생성 및 삭제 등 게임의 주요 기능을 Python과 Pygame을 사용하여 개발
- 디자인 패턴 적용: 코드의 유지보수성과 확장성을 높이기 위해 Prototype, Builder, Observer, Facade 패턴을 적용
- 오디오 및 비주얼 요소 통합: 게임 배경, 캐릭터, 타겟 등의 이미지와 효과음을 게임에 통합하여 플레이어의 몰입도 향상
- 사용자 입력 처리: 키보드와 마우스 입력을 통해 게임 캐릭터와 상호작용할 수 있도록 구현
## 클래스 다이어그램
![image](https://github.com/rlaxxwls13/AniPunch/assets/101396454/9ac0e801-d790-496a-a319-397118cae7fd)


## 동작
1. 시작페이지, 아무 곳이나 클릭하면 게임 시작
   
![image](https://github.com/rlaxxwls13/AniPunch/assets/101396454/2f456498-208e-4947-92ed-e2f6422f8cc1)

2. 게임 실행
   - 사용자의 초기 상태는 'kitty'이며 방향키를 누르면 'rabbit'으로 상태 변경 가능
     
![image](https://github.com/rlaxxwls13/AniPunch/assets/101396454/03209fa0-18d5-48c2-bb2a-9becf311cd4a) ![image](https://github.com/rlaxxwls13/AniPunch/assets/101396454/3ed14f30-271c-49d1-92d3-062acc28843a)

   - 스페이스바를 누르면 미사일 발사, 올바른 스킬로 올바른 타겟을 적중시키면 타겟이 제거됨

![image](https://github.com/rlaxxwls13/AniPunch/assets/101396454/1527ccbf-d44a-4b14-825e-3b2be1fc5e41) ![image](https://github.com/rlaxxwls13/AniPunch/assets/101396454/91fe43ec-b16f-497b-9700-d2d3501535d3)

   - 점수가 10점을 넘어갈 때마다 seepd up
     
![image](https://github.com/rlaxxwls13/AniPunch/assets/101396454/72214264-8a56-4770-bc58-2fede4bf3ad3)

   - 특별하게 점수가 20이 넘었을 때만 new animal 'puppy' 추가
     
![image](https://github.com/rlaxxwls13/AniPunch/assets/101396454/f24ac85b-8f4c-4ada-9b5c-8eda975fb3a6) ![image](https://github.com/rlaxxwls13/AniPunch/assets/101396454/cdd5096b-edbd-497f-80a1-740c80230b2f)

   - 제거하지 못한 타겟이 땅에 떨어지면 life가 하나씩 감소
     
![image](https://github.com/rlaxxwls13/AniPunch/assets/101396454/583c6de4-17b5-4980-8302-d27472593eab) ![image](https://github.com/rlaxxwls13/AniPunch/assets/101396454/a30ec68a-e034-407b-bcb3-246e12e93d20)


3. 게임 종료
   - life가 전부 소진되면 게임오버 사운드와 함께 게임 종료, 사운드가 종료되면 시작페이지로 전환

![image](https://github.com/rlaxxwls13/AniPunch/assets/101396454/4e412eab-b062-4eb2-abc5-a3074b4f5730) ![image](https://github.com/rlaxxwls13/AniPunch/assets/101396454/23e46682-6085-4d0b-8de3-9f070d762145)

 
