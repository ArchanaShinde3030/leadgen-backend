FROM python:3.13

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 7860

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:7860