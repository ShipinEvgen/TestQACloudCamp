FROM python
WORKDIR /test_api/
COPY  . .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD python -m pytest /test_api/test_API.py
