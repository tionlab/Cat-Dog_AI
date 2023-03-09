# Cat-Dog_AI (Cat Or Dog? [COD])
Tensorflowf를 사용한 강아지, 고양이 구별 AI

## FAST START
1. <a href="https://github.com/tionlab/Cat-Dog_AI/releases/tag/Stable1.0.0">Click here to download.</a> install tensor.zip
2. Run install.py (필수)
3. Change data\test\test.jpg (선택)
3. Run main.py
+ data\train 내부 파일을 변경후 train.py를 작동시 새로운 모델이 생성됨

## Introduce
Tensorflow를 활용한 강아지, 고양이 구별 AI 입니다!
사용한 모듈은 tensorflow, tkinter, PIL, keras_preprocessing(이)가 있습니다.
(tensorflow.keras.preprocessing 모듈이 작동이 안되어 찾아본 결과 StackOverFlow에서 Tensorflow 모듈 자체 버그라고 하여서 외부 모듈을 추가하였습니다. [keras_preprocessing])


강아지, 고양이 모델(model_01)이 기본 탑제되어있으며
이를 train.py로 다른 모델을 생성하여 다른 구별 AI 또한 제작할 수 있습니다.
(예시. [DataSet : 정상 안구 / 결막염 안구 JPG] -> train.py = 결막염 유무 판단 AI 제작 가능)

## Alert

- 기본 모델은 학습을 100회만 돌렸으며, 데이터셋도 사진 40장 밖에 되지 않기에 정확도는 떨어질수도 있습니다.
- Python 3.xx Require!! (Tested on 3.9.6)

## ScreenShot

<p align="center">
<img src="https://i.ibb.co/z4FqSFw/dsfgdh.png"></img>
</p>


## PIP install (install.py)

- pip install tensorflow
- pip install tkinter
- pip install PIL
- pip install keras_preprocessing
