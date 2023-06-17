FROM python
WORKDIR /test/
COPY  . .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD python -m pytest /test/test.py
