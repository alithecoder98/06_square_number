FROM  python
WORKDIR /app
COPY . /app.py
CMD [ "python","app.py" ]