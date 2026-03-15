FROM python
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app/writing-a-c-compiler-tests
RUN ./test_compiler --check-setup