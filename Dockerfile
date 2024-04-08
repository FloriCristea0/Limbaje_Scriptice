FROM python:3.11-slim
WORKDIR /app
COPY . . 
EXPOSE 8000
RUN pip install -r requirements.txt
CMD python3 main.py

# docker build -t api . 
# docker images
# pt sters cointainer docker stop api; docker rm api
# docker run -it -d -p 8000:8000 --name api api uvicorn main:app --host 0.0.0.0