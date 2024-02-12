FROM openjdk:11
COPY . /src/api/api
WORKDIR /src/api/api
RUN javac api.java
CMD ["java", "api"]