FROM python:3.6-slim-stretch
ENV PORT=8008

RUN apt update
RUN apt install -y python3-dev gcc

# Install  fastai
RUN pip install fastai

# Install starlette and uvicorn
RUN pip install starlette uvicorn python-multipart aiohttp aiofiles

ADD predicter.py predicter.py
ADD server.py server.py
ADD model model
ADD static static



EXPOSE 8008

# Start the server
CMD ["python", "server.py", "serve"]