# SW_study

## 1. django 시작하기

### 가상환경 생성

$python -m venv venv

### 가상환경 시작

$source venv/Scripts/activate

### requirements 설치

$pip install -r requirements.txt

### requirements 생성

$pip freeze > requirements.txt

### django 설치

$pip install django==3.2.13

### django 프로젝트 만들기

$django-admin startproject my_pjt .

### 앱 만들기

$python manage.py startapp my_app

### 서버 실행

$python manage.py runserver