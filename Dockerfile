FROM python:latest

WORKDIR /aws-ci-cd-demo

RUN python -m venv venv

RUN . venv/bin/activate

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app ./app

EXPOSE 8810

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8810"]