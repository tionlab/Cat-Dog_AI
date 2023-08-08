import tensorflow as tf
from tkinter import *
from PIL import ImageTk, Image

# ! 기본 표시 문구 선언
running = "\n결과를 계산중입니다..."

# ! 테스트 이미지 입력
image_path = "data/test/test.jpg"

# ! Tkinter = root 선언
root = Tk()

# ! 기본 배경 설정 및 프로그램 미씽 현상 대비 항상 위 고정
root.configure(bg='black')
root['bg'] = 'black'
root.wm_attributes("-topmost", 1)
root.geometry("400x400")
root.resizable(width=False, height=False)
label1 = Label(root, text="Tion", font=(
    "Century Gothic", 30), bg="black", fg="white")
label2 = Label(root, text="Cat Or Dog?", font=(
    "Tahoma", 50), bg="black", fg="white")
label1.pack()
label2.pack()
root.overrideredirect(True)
w = 800
h = 650
img1 = Image.open(image_path)
resize_image = img1.resize((300, 300))
img2 = ImageTk.PhotoImage(resize_image)
label3 = Label(root, bg="black", image=img2)
label3.pack()
label4 = Label(root, text=running, font=(
    "Tahoma", 20), bg="black", fg="white")
label4.pack()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# ! 이벤트 선언


def disable_event():
    pass


def close_app():
    root.destroy()


def refresh():
    # ! 표시 창 상태 변경
    img3 = Image.open(image_path)
    resize_image2 = img3.resize((300, 300))
    img4 = ImageTk.PhotoImage(resize_image2)
    label4.config(text=running)
    label3.configure(image=img4)
    label3.image = img4
    # ! AI 예측 모델 로드
    model = tf.keras.models.load_model("model-01")
    # ! 이미지 크기 설정
    img_width = 150
    img_height = 150
    # ! 테스트 이미지 예측
    test_image = tf.keras.preprocessing.image.load_img(
        image_path, target_size=(img_width, img_height))
    test_image = tf.keras.preprocessing.image.img_to_array(test_image)
    test_image = test_image / 255.0
    test_image = tf.expand_dims(test_image, 0)
    prediction = model.predict(test_image)
    # - print(prediction)
    if prediction < 0.5:  # * % 로 계산하는 모델이 아니므로 확률계산은 불가능합니다.
        res = '\n고양이'
        label4.config(text=res)
    else:
        res = '\n강아지'
        label4.config(text=res)


# ! 버튼 선언
btn2 = Button(root, text="새로 고침",
              bg="blue", font=("Tahoma", 10), fg="white", command=refresh)
btn2.pack(padx=50, pady=10)

btn = Button(root, text="종료 하기",
             bg="red", font=("Tahoma", 10), fg="white", command=close_app)
btn.pack(padx=50, pady=10)
root.protocol("WM_DELETE_WINDOW", disable_event)

# ! AI 예측 모델 로드
model = tf.keras.models.load_model("model-01")
# ! 이미지 크기 설정
img_width = 150
img_height = 150
# ! 테스트 이미지 예측
test_image = tf.keras.preprocessing.image.load_img(
    image_path, target_size=(img_width, img_height))
test_image = tf.keras.preprocessing.image.img_to_array(test_image)
test_image = test_image / 255.0
test_image = tf.expand_dims(test_image, 0)
prediction = model.predict(test_image)
# print(prediction)
# ! 예측결과 업데이트
if prediction < 0.5:  # * % 로 계산하는 모델이 아니므로 확률계산은 불가능합니다.
    res = '\n고양이'
    label4.config(text=res)
else:
    res = '\n강아지'
    label4.config(text=res)
root.mainloop()
