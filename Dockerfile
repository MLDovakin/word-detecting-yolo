FROM python:3.9

EXPOSE 8501

WORKDIR /app

COPY  requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt
RUN pip install -U pip setuptools wheel

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY . .

CMD streamlit run st_interface.py