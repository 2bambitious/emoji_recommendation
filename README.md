# 영어 채팅 이모티콘 추천 프로젝트

## 소개

<br/> 

> 카카오톡 이모티콘 플러스를 구매해야지만 쓸 수 있는 이모티콘 자동 추천 기능을 구현해보면 좋지 않을까?

카카오톡 이모티콘 플러스를 구매하면 사용자가 채팅방에 입력하는 글자에 따라 알맞은 이모티콘을 추천해주는 기능이 추가됩니다. 이를 영어 채팅으로 간단하게나마 구현해보고자 하는 프로젝트입니다.

---

## 기능

<br />
영어로 채팅하듯이 하고싶은 말을 입력하면, 그에 맞는 이모티콘이 추천되어 출력되는 프로젝트입니다.

--- 

## 구성 요소 설명

<br/> 

* **archive** : train, test, valid dataset이 있는 폴더
* **emoji** : 이모티콘 파일들의 폴더  

* **main.py** : 프로그램이 실행되는 파일
* **model.py** : 분류 모델 구현 파일 
* **word_preprocessing.py** : tokenizing, labelencoding등 전처리 관련 파일
* **emojiPrint.py** : 이모티콘 출력 담당 파일 

--- 


## 구동

<br/> 


1. git clone을 통해 레포지토리를 클론하거나 Code > Download ZIP을 통해 프로젝트 다운
2. SentimentalClassification.h5가 없는 경우, train.py 실행하여 모델 생성
3. main.py를 실행하여 영어로 하고싶은 말을 입력
4. 알맞은 이모티콘이 추천됨
5. 종료를 원할 경우, "terminate" 입력

---

## 구동결과

<br/> 

https://youtu.be/urbHt1kGXz4

---



## 참고문헌

<br/> 

* **dataset** : https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp
* https://www.kaggle.com/code/marawankhaled/emotion-detection-cnn-lstm
* 처음 배우는 딥러닝 챗봇 (조경래 저, 한빛미디어)
* 김기현의 자연어 처리 딥러닝 캠프 파이토치 편 (김기현 저, 한빛미디어)

