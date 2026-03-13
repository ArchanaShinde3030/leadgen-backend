FROM python:3.13

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 7860

# Use the start.sh
CMD ["./start.sh"]